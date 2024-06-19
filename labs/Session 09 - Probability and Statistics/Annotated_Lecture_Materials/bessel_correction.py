#!/usr/bin/env python3
# bessel_correction.py

import numpy as np
from numpy.random import (
    seed,
    randint,
    choice,
)  # import these three functions from module
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from numba import jit
import pickle  # module can read and write binary
import os
import sys


@jit(nopython=True)  # convert this function to compiler code
def get_bsv(arr):
    mean = np.mean(arr)  # numpy can do vectorized operations on array
    bsv = np.sum((arr - mean) ** 2) / len(arr)  # calculate biased std dev
    return bsv


@jit(nopython=True)
def get_sample_bsv(population, sample_size):
    num_trials = 20_000  # N = 20,000
    total_bsv = 0
    for _ in range(num_trials):  # iterate through to 20,000
        samples = choice(
            population, sample_size, replace=False
        )  # pass in array, and desired
        # size of sample
        total_bsv += get_bsv(samples)  # find bsv of all samples, add to a counter
    mean_bsv = total_bsv / num_trials  # find average bsv of each sample
    return mean_bsv


def run_trials():
    seed(2021)
    population = randint(0, 1000, 7000)
    pop_var = get_bsv(population)

    max_sample_size = 20

    print(
        f"{'Sample Size':^11}" f"{'Sample Var':^21}" f"{'Pop Var':^18}" f"{'Ratio':^8}"
    )

    results = []
    for sample_size in range(2, max_sample_size + 1):
        sample_bsv = get_sample_bsv(population, sample_size)
        ratio = sample_bsv / pop_var
        results.append((sample_size, sample_bsv, pop_var, ratio))
        print(
            f"{sample_size:^11}" f"{sample_bsv:>16,.4f}" f"{pop_var:>18,.4f}",
            f"{ratio:^15.4f}",
        )
    return results


def plot_ratio(ax, results):
    x = [r[0] for r in results]
    y = [r[3] for r in results]
    ax.plot(x, y, label="BSV/PV")

    x = np.linspace(2, 20, endpoint=True)
    y = (x - 1) / x
    ax.plot(x, y, label=r"$\frac{n-1}{n}$")

    ax.set_title("BSV over PV compared to Hyperbola (n-1) over n")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Biased Sample Var / Population Var")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(0.05))
    ax.legend()


def plot_ubsv(ax, results):
    x = [r[0] for r in results]
    y = [r[2] for r in results]
    ax.plot(x, y, label="Pop Var")

    y = [r[1] for r in results]
    ax.plot(x, y, label="BSV")

    for i, v in enumerate(y):
        y[i] = y[i] * x[i] / (x[i] - 1)
    ax.plot(x, y, label="UBSV")

    ax.set_title("Variance: Population v. Biased Sample v. Unbiased Sample")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Variance")
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.legend()


def main():
    file_name = (
        os.path.dirname(sys.argv[0]) + "/bessel.pickle"
    )  # file_name has '' string
    # at the end
    if not os.path.exists(file_name):  # if the file doesn't yet exist
        results = run_trials()  # run function that gives us results
        with open(file_name, "wb") as file_out:  # binary file, context manager prevents
            # data corruption if there is an error
            pickle.dump(
                results, file_out, pickle.HIGHEST_PROTOCOL
            )  # dump info into file as
            # binary
        fig = plt.figure(os.path.basename(sys.argv[0]))
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        plot_ratio(ax, results)
        plt.show()
    else:
        with open(file_name, "rb") as file_in:  # if the file exists, we read them in
            results = pickle.load(file_in)

        print(
            f"{'Sample Size':^11}"
            f"{'Sample Var':^21}"
            f"{'Pop Var':^16}"
            f"{'UBSV':^12}"
        )
        for r in results:
            sample_size, sample_bsv, pop_var, _ = r  # unpack each column tuple
            ubsv = (
                sample_bsv * sample_size / (sample_size - 1)
            )  # implement bessel's correction
            # for each sample size
            print(
                f"{sample_size:^11}" f"{sample_bsv:>16,.4f}" f"{pop_var:>18,.4f}",
                f"{ubsv:^18,.4f}",
            )

        fig = plt.figure(os.path.basename(sys.argv[0]))
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        plot_ubsv(ax, results)
        plt.show()


if __name__ == "__main__":
    main()
