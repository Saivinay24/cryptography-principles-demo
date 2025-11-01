# Cryptography Principles Demonstration

This project is a hands-on demonstration of two core principles of modern cryptography: **Confidentiality** and **Integrity**.

## 1. Confidentiality (The Speck Cipher)

This part of the project demonstrates how data can be kept secret from unauthorized parties using encryption.

* [cite_start]**File:** `speck_cipher.py` [cite: 4]
* [cite_start]**What it is:** This is a Python implementation of the **Speck 32/64 block cipher**[cite: 4]. Speck is a lightweight cipher developed by the NSA.
* [cite_start]**How it works:** The script defines functions for encryption (`speck_encrypt`), decryption (`speck_decrypt`), and generating round keys (`speck_key_schedule`)[cite: 4]. [cite_start]When run, it takes a sample plaintext, encrypts it, and then decrypts the resulting ciphertext to prove that the original message is recovered successfully[cite: 4].

### How to Run

1.  Ensure you have Python 3 installed.
2.  From your terminal, simply run the script:
    ```bash
    python speck_cipher.py
    ```
3.  [cite_start]The script will print the original plaintext, the key, the resulting ciphertext, and the final decrypted text to show it matches[cite: 4].

## 2. Integrity (SHA-256 Hashing)

This part of the project demonstrates how to verify that data has not been altered, tampered with, or corrupted.

* [cite_start]**Files:** `secret.txt`, `decrypted_secret.txt` [cite: 3][cite_start], `original_hash.txt` [cite: 2]
* **What it is:** This section uses the **SHA-256 hash algorithm**. A hash function creates a unique, fixed-length digital fingerprint (a "hash") for a piece of data.
* **How it works:**
    1.  A secret message (`secret.txt`) is created.
    2.  [cite_start]Its SHA-256 hash is calculated (the first hash in `original_hash.txt`)[cite: 2].
    3.  [cite_start]The file `original_hash.txt` [cite: 2] shows that this hash matches, proving the file is intact.
    4.  [cite_start]It then shows a *different* hash and states "doesnt match...." This demonstrates the key property of hashes: **if even one character in the file changes, the resulting hash will be completely different**[cite: 2]. This allows us to detect any tampering.

[cite_start]*Note: The `secret.enc` file [cite: 1] is a binary encrypted version of `secret.txt`, likely created using OpenSSL.*
