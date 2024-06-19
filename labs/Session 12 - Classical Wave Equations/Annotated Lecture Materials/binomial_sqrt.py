#!/usr/bin/env python3
# binomial_sqrt.py

import sympy


def printM(expr, num_digits):
    return expr.xreplace(
        {
            n.evalf(): n if type(n) == int else sympy.Float(n, num_digits)
            for n in expr.atoms(sympy.Number)
        }
    )


def calc_coeff(a, b, r, n):  # coefficients in front of terms
    i = 1
    for m in range(n):
        i = i * (r - m) / (m + 1)
    i = i * pow(a, r - n)
    i = i * pow(b, n)
    return i


def binomial_expand(a, b, c, r, max_t):  # do binomial expansion symbolically
    x = sympy.symbols("x")  # generates symbolic expression
    poly = 0
    for t in range(max_t):
        poly += calc_coeff(a, b, r, t) * x ** (
            c * t
        )  # add terms using newton's equation,
        # t incrementally increases c
    return poly, sympy.lambdify(
        x, poly.as_expr(), modules="numpy"
    )  # return a callable function


def heron(s):
    x = s / 2
    t = 1
    while x**2 - s > 1e-14:  # iterate until we go below 1e-14
        x = (s / x + x) / 2
        t += 1
    return t, x


def main():
    print(f"{'Terms':>5}{'Estimate':>18}{'Binomial Expansion':>21}")
    for t in range(1, 21):  # go to 20 terms
        eqn = binomial_expand(1, -1, 1, 1 / 2, t)
        print(f"{t:>5}  {3 * eqn[1](2/9):.14f}", end="")  # print out the first 7 terms
        if t < 8:
            print(f" = {printM(eqn[0], 5)}", end=" ")
        print()

    t, x = heron(7)  # compare to heron's method
    print("Heron's Method")
    print(f"{t:>5}  {x:.14f}", end="")


if __name__ == "__main__":
    main()
