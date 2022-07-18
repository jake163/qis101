#!/usr/bin/env python3
# goldbach_conjecture.py


import numpy as np
from sympy import prime  # import prime function from sympy module
from itertools import combinations_with_replacement  # from itertools module

# import combinations_with_replacement function


def main():
    n = 100  # assign 100 to variable n

    print(
        f"Verifying Goldbach's conjecture " f"for every even integer between 2 and {n}:"
    )

    # Use a list comprehension to generate a list of first 'n' primes
    ## list comprehension: primes = [a,b,c,..]
    primes = [prime(n) for n in range(2, n)]

    # Generate all pairs of primes (with repetition)
    ## e.g. we can have pair of 7,11 and 11,7
    prime_pairs = [*combinations_with_replacement(primes, 2)]
    ## "*" give every grouping of primes immediately

    # Create sorted list containing the sum of each pairwise primes
    ## sum each pair in the list of prime pairs, and sort them
    summed_pairs = np.sort([sum(pair) for pair in prime_pairs])

    # Determine which EVEN integers > 2 are NOT in the list of summed prime pairs
    # The numpy function setdiff1d() returns any elements in the first list
    # that are not also in the second list
    violations = np.setdiff1d(range(6, n + 2, 2), summed_pairs)
    ## make list of even numbers from 6 to 100 in increment of 2, and look
    ## for items in range that can't be found in "summed_pairs"

    if len(violations) == 0:  ##how many items in the "violations" list? 0?
        print("No Goldbach violations were found")  # printed message for no
        # violations
    else:
        print(f"Found these violations: {violations}")  # printed message if there
        # are 1 or more violations; show the violations


if __name__ == "__main__":
    main()
