#!/usr/bin/env python3
# werner_formula.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
import sys
import os

a = 0.8 #define k's 
b = 0.5


def f1(x):
    return np.sin(a * x)


def f2(x):
    return np.sin(b * x)


def f3(x):
    return (np.sin(a * x)) * (np.sin(b * x)) #product of two sin waves, different k's


def f4(x):
    return (np.cos((a - b) * x) - np.cos((a + b) * x)) / 2 #werner's sum formula, important
#for fourier analysis


def plot(ax):
    x = np.linspace(-3 * np.pi, 3 * np.pi, 1000) #specified interval, 1000 subdomains
    y = f1(x)
    line1 = ax.plot(x, y, label=r"$f(x) = \sin{0.8x}$")

    y = f2(x)
    line2 = ax.plot(x, y, label=r"$f(x) = \sin{0.5x}$")

    y = f3(x)
    line3 = ax.plot(
        x, y, label=r"$f(x) = \sin({0.8x})\sin({0.5x})$", color="black", linewidth=2.5
    )

    x = np.linspace(-3 * np.pi, 3 * np.pi, 140) #different subdomain number, had to be
    #careful to avoid aliasing
    y = f4(x)
    line4 = ax.plot(
        x,
        y,
        label=r"$f(x) = \frac{\cos({a-b}) - \cos({a+b})}{2}$",
        linestyle="dotted",
        color="yellow", #it's a dotted line that connects markers, yellow
        marker="o",
        markersize=5,
    )

    ax.set_title("Sin/Cos Waves")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.xaxis.set_minor_locator(AutoMinorLocator()) #automatically place tick marks
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend(loc="upper left", bbox_to_anchor=(-0.17, 1.16))  # legend for the graph, 
    #bbox_to_anchor allows you to presicely control where the legend is in terms of cartesian
    #coordinates


def main():
    fig = plt.figure(os.path.basename(sys.argv[0])) #name of the graph is basically the name
    #of the .py file the code is on
    gs = fig.add_gridspec(1, 1) #1 x 1 "figure space"

    ax = fig.add_subplot(gs[0, 0]) #the top left (only) figure in the "figure space"
    plot(ax)  # pass in ax, executes plot(ax)
    plt.show()  # show the plot


if __name__ == "__main__":
    main()
