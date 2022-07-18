#!/usr/bin/env python3
# updated_gen_continued_fractions.py

import math

MAX_TERMS = 20


def decode_gencf(a0, b0, Ai, Bi, Ci, Di, Ei):
    an, bn = a0, b0  # inputted initial parameters
    hn, kn = 0, 0  # n starts at 0
    b_1, h_1, k_1 = 1, 1, 0  # initial parameters of the algorithm
    h_2, k_2 = 0, 1  # inital parameters of the algorithm
    for n in range(1, MAX_TERMS):  # continued fractions algorithm, loop to n = 19
        hn = an * h_1 + b_1 * h_2
        kn = an * k_1 + b_1 * k_2
        b_1 = bn
        h_1, h_2 = hn, h_1
        k_1, k_2 = kn, k_1
        an = Di * n + Ei
        bn = Ai * n * n + Bi * n + Ci
    return hn / kn


def print_rel_error(
    estimated, actual
):  # estimated: decode_gcf(), actual: exact decimal value of pi
    print(f"Est.        : {estimated}")
    print(f"Act.        : {actual}")
    print(
        f"Rel. % Err  : {(actual - estimated)/actual:.14%}\n"
    )  # relative error of Pi estimate to 14 digits after decimal


def main():
    print(f"Euler's Generalized Continued Fraction for Pi")
    x = decode_gencf(3, 1, 4, 4, 1, 0, 6)
    print_rel_error(x, math.pi)

    print(f"GCF #1 for Pi")  # GCF #1 estimation of Pi
    y = decode_gencf(3, 1, 8, 0, -7, 8, -1)  # enter continued fractions parameters
    print_rel_error(y, math.pi)  # Print error relative to exact decimal value of Pi

    print(f"GCF #2 for Pi")
    z = decode_gencf(2, 8, 4, 8, 0, 4, 2)
    print_rel_error(z, math.pi)


if __name__ == "__main__":
    main()
