#!/usr/bin/env python3
# aes_demo.py

import aes
import os


def main():
    # The secret key is 16 bytes long
    # os.urandom() generates a string of certain byte size
    secret_key = os.urandom(16)
    print(f"Secret key = {bytearray(secret_key).hex()}\n")

    # iv = (Random) initialization vector which ensures
    # the same value encrypted multiple times, even with the
    # same secret key, will not always result in the same encrypted value
    iv = os.urandom(16)  # analogous to a seed for a random number generator

    plaintext = b"Attack at dawn"  # b means string is interpreted as ascii bytes
    print(f"plaintext = {plaintext}\n")

    ciphertext = aes.AES(secret_key).encrypt_ctr(
        plaintext, iv
    )  # encrypt plain text using
    # key
    print(f"ciphertext = {ciphertext}\n")  # \x means hexadecimal number

    plaintext = aes.AES(secret_key).decrypt_ctr(
        ciphertext, iv
    )  # take encrypted text and
    # decrypt it back
    print(f"plaintext = {plaintext}\n")


if __name__ == "__main__":
    main()
