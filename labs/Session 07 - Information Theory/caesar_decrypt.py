#!/usr/bin/env python3
# caesar_decrypt.py

import sys
import os

def main(file_name, key_shift):
    with open(
        file_name, "rb"
    ) as f_in:  # with is a context manager, open file and reads
        # binary, gives alias f_in
        f_bytes = bytearray(f_in.read())  # read f_in, put in bytearray

        for i in range(0, len(f_bytes)):  # iterate through 0 to len(f_bytes) - 1
            f_bytes[i] = (f_bytes[i] + key_shift) % 256  # for every byte in file we
            # we overwrite according to key_shift

        print(f_bytes.decode())  # print decoded message


if __name__ == "__main__":  # run from command line
    file_name = None
    if len(sys.argv) == 1:  # if filename wasn't provided
        print("You must provide a filename and a key value")
    else:
        file_name = sys.argv[1]  # filename is second item in argument vector
        key_shift = int(sys.argv[2])  # keyshift is the third item in argument vector
        main(file_name, key_shift)  # pass in file_name and key_shift
        with open(os.path.dirname(sys.argv[0]) + "/decrypted_ciphertext2.txt", 'w') as f:
            f.write(main('caesar_decrypt.py', 154))
