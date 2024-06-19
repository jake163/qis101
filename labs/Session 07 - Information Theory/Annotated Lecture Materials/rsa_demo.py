#!/usr/bin/env python3
# rsa_demo.py

import numpy as np


def extended_euclidean(a, b):  # perform extended euclidean algorithm to perform GCD
    swapped = False
    if a < b:
        a, b = b, a
        swapped = True
    ca = (1, 0)  # initial values
    cb = (0, 1)
    while b != 0:
        k = a // b
        a, b, ca, cb = (
            b,
            a - b * k,
            cb,
            (ca[0] - k * cb[0], ca[1] - k * cb[1]),
        )  # iteration
        # procedure
    if swapped:
        return (ca[1], ca[0])
    else:
        return ca


def power_modulus(b, e, n):  # lets us raise a number to a power and take modulus
    r = 1
    for i in range(e.bit_length(), -1, -1):
        r = (r * r) % n
        if (e >> i) & 1:
            r = (r * b) % n
    return r


def generate_keys(p, q):  # pass in two prime numbers
    n = p * q
    totient = (p - 1) * (q - 1)
    # e = public encryption exponent (a prime number), gcd of e and totient is 1 and e is
    # in between 1 and the totient
    e = 35537
    # d = private encryption exponent
    d = extended_euclidean(e, totient)[0]  # de mod totient = 1
    if d < 0:
        d += (
            totient  # force d to be positive, this is okay as de mod totient is still 1
        )
    return {"priv": (d, n), "pub": (e, n)}  # print private and public key, pass in
    # corresponding numbers


def encrypt(m, public_key):  # pass in m and public_key for c = m^e mod n
    e = public_key[0]
    n = public_key[1]
    return power_modulus(m, e, n)  # returns cyphertext int


def decrypt(m, private_key):  # pass in m and public_key for m = c^d mod n
    d = private_key[0]
    n = private_key[1]
    return power_modulus(m, d, n)  # returns plaintext int


def main():
    # Pick two prime numbers
    p = 31337
    q = 31357

    keys = generate_keys(p, q)  # make encryption/decryption keys
    print(f"RSA Encryption Keys: {keys}")

    private_key = keys["priv"]  # two keys, public and private
    public_key = keys["pub"]

    plaintext = "Hi!"
    print(f"Plaintext = {plaintext}")

    b = bytearray(plaintext, encoding="utf-8")  # convert plaintext to bytes
    plaintext_int = int.from_bytes(
        b, "big"
    )  # tell python how to interpret the byte ordering
    print(f"Plaintext as Integer = {plaintext_int}")

    ciphertext_int = encrypt(
        plaintext_int, private_key
    )  # raises plaintext up to e key, mod
    # n
    print(f"Ciphertext as Integer = {ciphertext_int}")  # print out encrypted text

    plaintext_int = decrypt(
        ciphertext_int, public_key
    )  # take cyphertext, raise up to d
    # key (private), mod n
    print(f"Plaintext as Integer = {plaintext_int}")  # print decrypted text as string

    b = plaintext_int.to_bytes(3, "big")
    plaintext = b.decode(encoding="utf-8")
    print(f"Plaintext = {plaintext}")


if __name__ == "__main__":
    main()
