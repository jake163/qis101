#!/usr/bin/env python3
# pells_equation.py

import math
import numba as nb  # import module as alias


@nb.njit(locals={"x": nb.uint64, "y": nb.uint64})  # @ symbol is decorator,
# compile this just in time (j.i.t.), no python (n)
def pell_solution(n):
    x = 1
    while x < 70_000:
        x2 = x * x
        y = 1
        y_max = math.floor(math.sqrt((x2 - 1) / n))  # math.floor gives lower
        # bound on the decimal input
        while y <= y_max:
            y2 = y * y
            if x2 - n * y2 == 1:  # checks that our values satisfy equality
                return x, y  # python allows us to return multiple values
            y += 1
        x += 1
    return None, None  # None means nothing, no value


def main():  # executable from command line
    print(f"{'n':>4}{'x':>8}{'y':>8}")
    print(f"{'='*3:>4}{'='*6:>8}{'='*6:>8}")

    for n in range(2, 71):  # iterate over number list, 2 to 70
        x, y = pell_solution(n)  # for each n, plug into pell_soln() and set
        # equal to x and y
        if x == None:  # what to print if we didn't get a solution
            print(f"{n:>4}{'-':>8}{'-':>8}")
        else:
            print(f"{n:>4}{x:>8}{y:>8}")


if __name__ == "__main__":
    main()
