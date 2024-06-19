#!/usr/bin/env python3
# reverse.py


def reverse_str(a):  # reverse string a
    b = ""  # b is an empty string, local variable
    for i in range(
        len(a) - 1, -1, -1
    ):  # range starts at end of string a, stops at i = 0
        # for a step value of -1 (go backwards)
        b += a[i]  # add character at location i, add to end of b
    return b


def reverse_str2(a):  # reverse string a
    b = ""  # b is an empty string, local variable
    for i in reversed(
        range(len(a))
    ):  # range starts at end of string a, goes backward to
        # index 0
        b += a[i]  # for each i, we add the character at that location to the end of b
    return b


def reverse_str3(a):  # reverse string a
    b = ""  # b is an empty string
    for c in a:  # for index in a
        b = c + b  # prepend character from a to b
    return b


def main():
    s = "Forever Young"
    print(s)
    print(f"Number of characters: {len(s)}")

    print(reverse_str(s))
    print(reverse_str2(s))
    print(reverse_str3(s))

    print("".join(reversed(s)))  # concatenate reversed s to empty string
    print(s[::-1])  # reverse the order of s, array slicing


if __name__ == "__main__":
    main()
