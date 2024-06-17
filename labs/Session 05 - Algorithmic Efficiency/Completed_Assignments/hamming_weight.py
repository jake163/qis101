#!/usr/bin/env python3
# hamming_weight.py


def pop_count(
    binary_string: list,
) -> int:  # pass binary string (a list), output is integer
    population = 0  # counter is 0 to start
    for i in range(
        len(binary_string)
    ):  # iterate from 0 to the length of binary string - 1
        if binary_string[i] == "1":
            population += 1  # if binary string has a 1 at the given index, we add one to the counter
    return population


def main():  # executable from command line
    number = 95_601  # number we want to find hamming weight of
    binary_string = format(number, "b")  # convert number into binary string

    print(f"The integer {number} is the binary {binary_string}")
    print(f"{binary_string} has a population count of {pop_count(binary_string)}")


if __name__ == "__main__":
    main()
