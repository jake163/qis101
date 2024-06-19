#!/usr/bin/env python3
# sum_squares.py
def sum(n):  # takes natural number n as input
    s = 0  # initial a variable of 0
    for k in range(1, n + 1):  # iterate through first 1000 natural numbers
        s += k**2  # add n squared to sum, for each natural number up to 1000
    return s


def main():
    terms = 1000  # define n
    sigma = sum(terms)
    gauss_sum = int(
        (2 * terms**3 + 3 * terms**2 + terms) / 6
    )  # want integer output
    print(f"Sum of first {terms:,} natural numbers squared = {sigma:,}")
    print(f"Gauss Sum of first {terms:,} natural numbers squared = {gauss_sum:,}")


if __name__ == "__main__":
    main()
