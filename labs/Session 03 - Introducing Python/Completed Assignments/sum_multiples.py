#!/usr/bin/env python3
# sum_multiples.py


def sum_m(n):
    s = 0  # define 0 variable
    for k in range(1, n):  # list of numbers up to 1900 exclusive
        if k % 7 == 0 and k % 11 == 0:  # selecting numbers divisible only by 7 and 11
            s += k  # add those numbers together
    return s


def main():
    n = 1900  # define n
    sigma = sum_m(n)  # pass n through sum_n function
    print(f"Sum of first {n:,} natural numbers divisible by 7 and 11 = {sigma:,}")


if __name__ == "__main__":
    main()
