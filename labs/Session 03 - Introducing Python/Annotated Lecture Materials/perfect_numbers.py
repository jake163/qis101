#!/usr/bin/env python3
# perfect_numbers.py


def is_perfect_number(n):
    # define a function that takes a integer n (has a scope ":")
    sum_of_factors = 1
    # assign integer value to variable "sum_of_factors"
    for factor in range(2, n):
        # "factor" is an integer in list going from 2 to n-1, step of 1
        if n % factor == 0:
            # if checks that the given factor from range(2, n) has a remainder
            #  of zero w.r.t. n
            sum_of_factors += factor
            # if true, sum_of_factors = sum_of_factors + factor
    if sum_of_factors == n:
        # checking if n is a perfect number or not
        return True
    else:
        return False


def main():
    for n in range(2, 10_000):
        # n goes from 2 to 9,999, 10,000 has optional underscore
        if is_perfect_number(n):
            # does "is_perfect_number" return true with inputed n?
            # if so, then...
            print(f"{n:,} is a perfect number")
            # ... n, via a placeholder (commas used), is printed in
            # above f string


if __name__ == "__main__":
    main()
