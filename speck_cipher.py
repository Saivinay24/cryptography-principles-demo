

def rotate_right(x, r, word_size):
    mask = (1 << word_size) - 1
    return ((x >> r) | ((x << (word_size - r)) & mask)) & mask

def rotate_left(x, r, word_size):
    mask = (1 << word_size) - 1
    return (( (x << r) & mask) | (x >> (word_size - r))) & mask

def speck_rounds_and_masks(word_size=16):
    rounds = 22  # Speck32/64
    mask = (1 << word_size) - 1
    alpha = 7
    beta = 2
    return rounds, mask, alpha, beta

def speck_key_schedule(key_words, word_size=16):
    
    rounds, mask, alpha, beta = speck_rounds_and_masks(word_size)
    
    m = len(key_words)
    if m < 2:
        raise ValueError("Need at least 2 key words")
    l = key_words[:m-1][:]   
    k = [key_words[m-1]]     
    for i in range(rounds - 1):
        
        new_l = ( (rotate_right(l[i], alpha, word_size) + k[i]) & mask ) ^ i
        new_l &= mask
        l.append(new_l)
        new_k = rotate_left(k[i], beta, word_size) ^ l[-1]
        new_k &= mask
        k.append(new_k)
    return k  

def speck_encrypt(plaintext, key_words, word_size=16):
    
    rounds, mask, alpha, beta = speck_rounds_and_masks(word_size)
    k = speck_key_schedule(key_words, word_size)
    x, y = plaintext
    x &= mask
    y &= mask
    for i in range(rounds):
        x = ( (rotate_right(x, alpha, word_size) + y) & mask ) ^ k[i]
        y = rotate_left(y, beta, word_size) ^ x
        x &= mask
        y &= mask
    return (x, y)

def speck_decrypt(ciphertext, key_words, word_size=16):
    rounds, mask, alpha, beta = speck_rounds_and_masks(word_size)
    k = speck_key_schedule(key_words, word_size)
    x, y = ciphertext
    x &= mask
    y &= mask
    for i in range(rounds - 1, -1, -1):
        y = rotate_right(y ^ x, beta, word_size) & mask
        x = rotate_left(((x ^ k[i]) - y) & mask, alpha, word_size) & mask
    return (x, y)

if __name__ == "__main__":
    
    plaintext = (0x6565, 0x6877)         
    key = [6424, 4368, 2312, 256]         
    print("Plaintext:", (hex(plaintext[0]), hex(plaintext[1])))
    print("Key words:", [hex(k) for k in key])

    ciphertext = speck_encrypt(plaintext, key, word_size=16)
    print("Ciphertext:", (hex(ciphertext[0]), hex(ciphertext[1])))

    decrypted = speck_decrypt(ciphertext, key, word_size=16)
    print("Decrypted:", (hex(decrypted[0]), hex(decrypted[1])))
    assert decrypted == plaintext, "Decryption failed: output does not match plaintext"
    print("Success: decrypted text matches plaintext")