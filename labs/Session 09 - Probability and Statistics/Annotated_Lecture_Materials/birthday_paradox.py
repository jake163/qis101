#!/usr/bin/env python3
# birthday_paradox.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from numba import jit
import os
import sys


@jit(nopython=True)  # below function is in compiler code
def shared_birthdays(
    class_size,
):  # pass in class size, returns true if there are shared
    # birthdays
    birthdays = np.random.randint(
        0, 365, class_size
    )  # generate array with class size, birth
    # day is random for each
    for i in range(birthdays.size - 2):  # go up to a student i
        for j in range(i + 1, birthdays.size):  # then look for another student
            if (
                birthdays[i] == birthdays[j]
            ):  # if a student has same birthday as student i
                return True  # it means we did
    return False  # otherwise, we didn't


@jit(nopython=True)
def calc_probabilities(num_classes, max_class_size):  # calculate probabilities, pass in
    # num_classes and max_class_size
    prob = np.zeros(
        max_class_size
    )  # to start, probability is array of zeros up to length
    # of max_class_size
    for class_size in range(max_class_size):  # iterate through class sizes
        count = 0
        for _ in range(num_classes):
            if shared_birthdays(class_size):
                count += 1  # add 1 to counter when shared_birthdays returns true
        prob[class_size] = (
            count / num_classes
        )  # we put the probability in the appropriate
        # location in the prob array
    return prob  # outputs prob


def plot(ax):
    np.random.seed(2021)

    num_classes = 10_000
    max_class_size = 80
    prob = calc_probabilities(
        num_classes, max_class_size
    )  # plot probability as class size
    # increases

    ax.step(  # step chart, fixed y value across discrete interval
        range(max_class_size),
        prob,  # get back array of probabilities
        color="black",
        linewidth=3,
        label="Estimated Probability",
    )

    min_class_size = np.where(prob > 0.50)[0][
        0
    ]  # for min_class_size for shared birthday,
    # is there such a class? return index number (class size)
    p = prob[min_class_size]
    ax.vlines(
        min_class_size, 0, prob[min_class_size], color="red"
    )  # plot as vertical line
    # red

    # See https://en.wikipedia.org/wiki/Birthday_problem #rigorous way to solve this problem
    x = np.linspace(0, 80, 200)
    y = 1 - np.exp(-(x**2) / 730)
    ax.plot(x, y, color="blue", label=r"Approximated: $1-{\rm e}^-\frac{x^2}{365*2}$")
    # superimpose above data
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1.0)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.grid()
    ax.set_title(f"Birthday Paradox ({num_classes:,} classes)")
    ax.set_xlabel("Class Size")
    ax.set_ylabel("Probability")
    ax.legend()

    ax.annotate(
        f"Min Class Size = {min_class_size}",
        xy=(min_class_size, p),
        xytext=(28, 0.45),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
