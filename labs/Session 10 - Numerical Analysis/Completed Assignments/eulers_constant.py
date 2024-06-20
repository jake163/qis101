#!/usr/bin/env python3
# eulers_constant.py

import numpy as np
import scipy.integrate as itg
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import sys


def euler(x: float) -> float:  # integrand for euler's constant integral
    f = -(np.log(np.log(1 / x)))
    return f


def calc_e_const() -> float:  # compute euler's constant integral, from 0 to 1
    e_const = itg.quad(euler, 0, 1)[0]
    return e_const


def harmonics(x: int) -> float:  # compute list of harmonic numbers up to 1/x
    harms = [0] * x  # array of zeros
    harms[0] = 1  # first element is 1
    if x == 1:  # if x equals 1, then we don't need to to anything
        pass
    if x > 1:
        for i, num in enumerate(range(2, x + 1)):  # generate list of harmonic numbers
            harm = 1 / num
            harms[i + 1] = harms[i] + harm
    return harms


def plot(ax):
    x = np.linspace(
        1, 50, 1000
    )  # array of x's from 0 to 50, chopped into 1000 subdomains
    y = calc_e_const() + np.log(x)  # compute specified curve
    ax.plot(x, y, label=rf"$\gamma + \ln(x)$")

    x = np.linspace(1, 50, 50)  # x goes from 1 to 50, 50 subdomains
    y = harmonics(50)  # harmonic numbers up to 50
    ax.step(x, y, label=rf"$H_n$")

    y = harmonics(50) - np.log(x)

    ax.plot(x, y, label=rf"$H_n-\ln(x)$")  # The harmonic numbers curve Hn approaches
    # (ln(x)+ gamma) as n approaches infinity
    ax.set_title(rf"$H_n \ and \ \gamma + \ln(x)$", fontsize=20)
    ax.set_xlabel("x", fontsize=16)
    ax.set_ylabel("f(x)", fontsize=16)
    ax.xaxis.set_major_locator(MultipleLocator(10))  # ticks on x axis separated by 10
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.plot(
        1, calc_e_const(), color="red", marker="o", label=rf"$\gamma$"
    )  # show gamma on
    # graph
    ax.axhline(calc_e_const(), color="grey", linestyle="--")  # gamma line
    ax.legend()  # legend for the graph


def main():
    fig = plt.figure(
        os.path.basename(sys.argv[0])
    )  # the identifier for this figure, here it is the script path
    gs = fig.add_gridspec(1, 1)  # 1 by 1 figure space
    ax = fig.add_subplot(gs[0, 0])  # first (only) plot in the figure space
    plot(ax)  # pass in ax, executes plot(ax)
    plt.show()  # show the plot
    print(f"Euler's Constant is estimated to be {calc_e_const():.5f}")


if __name__ == "__main__":
    main()
