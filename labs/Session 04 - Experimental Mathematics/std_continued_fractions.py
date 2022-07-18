#!/usr/bin/env python3
# std_continued_fractions.py

import math

MAX_TERMS = 20  # global variable


def normalize_cf(cf):
    if len(cf) > 2:
        if cf[-1] == 1 and cf[-2] != 1:
            cf[-2] += 1
            cf.pop(-1)  # drop the 1 out of the list
    return cf


def encode_cf(x):  # Here encode_cf() is defined
    cf = []  # declaring cf as an empty list
    while len(cf) < MAX_TERMS:  # global variable MAX_TERMS dictates final length
        # of list
        cf.append(math.floor(x))  # add the floor value to the empty list
        x = x - math.floor(x)  # compute new x
        if x < 1e-11:
            break  # jump out of loop when error is sufficiently low
        x = 1 / x
    return normalize_cf(cf)  # last number in sequence can't be 1


def decode_cf(cf):  # define decode_cf()
    hn, kn = 0, 0
    b_1, h_1, k_1 = 1, 1, 0  # tuple packing
    h_2, k_2 = 0, 1
    for term in cf:  # for each term, get h/k
        an, bn = term, 1
        hn = an * h_1 + b_1 * h_2
        kn = an * k_1 + b_1 * k_2
        b_1 = bn
        h_1, h_2 = hn, h_1
        k_1, k_2 = kn, k_1
    return hn / kn


def eval_cf(x):  # compute cf for x input
    cf = encode_cf(x)  # find the a values for the continued fraction
    x2 = decode_cf(cf)  # convert cf to rational number or decimal
    print(f"{x} -> {cf} -> {x2}")


def main():  # This function is executable via command line
    eval_cf(3.245)  # cf function for 3.245 input
    eval_cf(math.sqrt(2))
    eval_cf(math.sqrt(113))

    golden_ratio = (1 + math.sqrt(5)) / 2
    eval_cf(golden_ratio)


if __name__ == "__main__":
    main()
