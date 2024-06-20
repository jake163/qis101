#!/usr/bin/env python3
# maxwell_boltzmann.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import os
import sys

# check out https://mathworld.wolfram.com/MaxwellDistribution.html for the equations I use to calculate mean and std. dev.


def max_bolt_pdf(
    a: int, x: float
) -> float:  # maxwell boltzmann probability for given x and a
    pde = np.sqrt(2 / np.pi) * (x**2 / a**3) * np.exp(-(x**2) / (2 * a**2))
    return pde


def plot(ax):
    x = np.linspace(
        0, 20, 1000
    )  # array of x's from 0 to 20, chopped into 1000 subdomains
    y = max_bolt_pdf(1, x)  # pdf for a = 1
    ax.plot(
        x,
        y,
        label=f"a = 1 \nmean = {(2*np.sqrt(2 / np.pi)):.3f},"  # this label includes the mean and standard deviation, both
        # a function of a. Placeholder goes to three decimal places
        f" std. dev. = {np.sqrt(3 - (8 / np.pi)):.4f}",  # placeholder goes to four decimal places
    )

    y = max_bolt_pdf(2, x)
    ax.plot(
        x,
        y,
        label=f"a = 2 \nmean = {(4*np.sqrt(2 / np.pi)):.3f},"
        f" std. dev. = {np.sqrt(12 - (32 / np.pi)):.4f}",
    )

    y = max_bolt_pdf(5, x)
    ax.plot(
        x,
        y,
        label=f"a = 5 \nmean = {(10*np.sqrt(2 / np.pi)):.3f},"
        f" std. dev. = {np.sqrt(75 - (200 / np.pi)):.4f}",
    )

    ax.set_title("Maxwell-Boltzmann PDF")
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")
    ax.xaxis.set_major_locator(MultipleLocator(2.5))  # ticks on x axis separated by 2.5
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.legend()  # legend for the graph


def main():
    fig = plt.figure(
        os.path.basename(sys.argv[0])
    )  # the identifier for this figure, here it is the script path
    gs = fig.add_gridspec(1, 1)  # 1 by 1 figure space
    ax = fig.add_subplot(gs[0, 0])  # first (only) plot in the figure space
    plot(ax)  # pass in ax, executes plot(ax)
    plt.show()  # show the plot


if __name__ == "__main__":
    main()
