#!/usr/bin/env python3
# euler_totient.py


def gcd(a: int, b: int) -> int:
    # defined a function gcd with two integer inputs, gives integer output
    while b > 0:
        a, b = b, a % b
        # tuple packing and unpacking, where a is assigned b and b is assigned
        # the mod of a and b. Stops iterating at b = 0 and returns a.
    return a


def totient(n: int) -> int:
    # optional hint tells you the type of the function input (:integer)
    # while the -> tells you the type of the output
    sum = 1
    # assign value of 1 to variable "sum", two numbers always have a totient
    # of 1
    for i in range(2, n):
        # range of numbers from 2 to n-1, which is convenient for our purposes
        if gcd(i, n) == 1:
            # looking for i in range (2, n) with gcd of 1 w.r.t. the n specified
            # in the below main() function
            sum += 1
            # when gcd(i,n) (defined above) is equal to one we add 1 to sum,
            # for each value of i.
    return sum


def main():
    print("Natural numbers between 2 and 100", end=" ")
    # prints the string with an end space
    print("that exceed their totient by one:")
    # prints the string

    for n in range(2, 101):
        # for loop, number in integer list running from 2 to 100, step 1.
        if n == totient(n) + 1:
            # checks if n in range(2, 101) is equal to the
            # output of the totient function with "n" input plus one
            print(n, end=" ")
            # if true, then that n is printed with an appended space


if __name__ == "__main__":
    main()
