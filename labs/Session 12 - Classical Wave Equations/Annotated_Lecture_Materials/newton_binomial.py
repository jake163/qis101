#!/usr/bin/env python3
# newton_binomial.py

import matplotlib.pyplot as plt
import numpy as np
import sympy
import sys
import os


def printM(expr, num_digits):
    return expr.xreplace(
        {
            n.evalf(): n if type(n) == int else sympy.Float(n, num_digits)
            for n in expr.atoms(sympy.Number)
        }
    )


def calc_coeff(a, b, r, n):
    i = 1
    for m in range(n):
        i = i * (r - m) / (m + 1)
    i = i * pow(a, r - n)
    i = i * pow(b, n)
    return i


def binomial_expand(a, b, c, r, max_t):
    x = sympy.symbols("x")
    poly = 0
    for t in range(max_t):
        poly += calc_coeff(a, b, r, t) * x ** (c * t)
    return poly, sympy.lambdify(x, poly.as_expr(), modules="numpy")


def plot(ax):
    x = np.linspace(0, 10, 1000) #domain from 0 to 10, 1000 subdomains

    ax.plot(x, 1 / np.power(2 * np.power(x, 2) + 7, 2 / 3), label="Exact") #plot y vs. x

    print(f"{'Terms':>5}   Binomial Expansion")
    for t in range(2, 8): #going from 2 terms to 8 terms
        eqn = binomial_expand(7, 2, 2, -2 / 3, t)
        print(f"{t:>5} = {printM(eqn[0], 5)}")
        ax.plot(x, np.array(list(map(eqn[1], x))), label=f"{t} terms") #print result

    ax.set_title(r"Binomial Expansion of $y = \sqrt[-2/3]{(2x^2+7)}$") #print LaTeX string
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_ylim(0, 0.3)
    ax.legend(loc="upper right")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
