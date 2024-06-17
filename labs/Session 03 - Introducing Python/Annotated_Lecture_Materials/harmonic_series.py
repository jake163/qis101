#!/usr/bin/env python3
# above line lets one run a py script directly from command line
# harmonic_series.py


def sum(n):
    # introduce or define a function with the name "sum",
    # () inbound parameters, ":" opens scope
    s = 0
    # statement within scope, indented
    for k in range(1, n + 1):
        # scope within a scope
        # list goes from 1 to n
        # assume a step of "1"
        s += 1 / k
        # s = s + 1/k
        # s is accumulated
    return s
    # function returns "s" (doesn't just print it)


def main():

    for terms in range(1000, 11000, 1000):
        # range of 1000 to 10,000, increments of 1000 (endpoint is exclusive)
        sigma = sum(terms)
        # every "term" is passed into sum function defined above
        print(f"Sum of first {terms:>7,} terms = {sigma:.14f}")
        # Prints string with variable "terms" which is right justified
        # (using commas), sigma variable has 14 digits after decimal.


if __name__ == "__main__":
    main()
# above line tells python interpreter what function to call (execute) when
# script is run directly (not imported)
