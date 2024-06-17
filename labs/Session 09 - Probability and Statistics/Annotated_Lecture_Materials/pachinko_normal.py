#!/usr/bin/env python3
# pachinko_normal.py

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import scipy.stats as stats
from numba import jit
import os
import sys


def stegun_normal(
    mean, std_dev
):  # function to take a uniform curve and convert to normal
    q = 1 - np.random.random()
    p = q if q < 0.5 else 1 - q
    t = np.sqrt(np.log(1 / p**2))
    x = t - (2.515517 + 0.802853 * t + 0.010328 * (t * t)) / (
        1 + 1.432788 * t + 0.189269 * (t * t) + 0.001308 * (t * t * t)
    )
    x = x if q < 0.5 else -x
    return x * std_dev + mean


@jit(nopython=True)
def pachinko_normal(num_balls, num_levels):  # simulate a pachinko game
    np.random.seed(2016)  # random number generator, initial value of 2016
    balls = np.zeros(num_balls, dtype=np.int32)  # array of zeros, has length num_balls
    for ball_num in range(num_balls):  # iterate through balls
        slot = 0
        for _ in range(
            num_levels
        ):  # for each ball, iterate through the number of levels
            slot += (
                -1 if np.random.rand() < 0.5 else 1
            )  # ternary operator, if random number
            # generator give number less than 0.5, add negative one to slot, else (random
            # number output > 0.5) add positive 1
        balls[ball_num] = slot // 2  # slot numbers are half of slot
    return balls


def plot(ax):
    num_levels = 80  # 40 #20 #10
    num_balls = 1_000_000  # 100_000 #10_000 #1_000

    balls = pachinko_normal(num_balls, num_levels)  # get balls from pachinko_normal()

    slots = np.zeros(num_levels + 1)
    first_slot = num_levels // 2
    for ball_num in range(num_balls):
        slot_num = int(
            first_slot + balls[ball_num]
        )  # count how many balls fell in slot
        slots[slot_num] += 1
    slots = slots / num_balls  # we know how many balls fell into each slot, normalized

    x = np.linspace(
        -num_levels // 2, num_levels // 2, num_levels + 1
    )  # plot above result
    ax.plot(x, slots, color="blue", linewidth=2, label="Pachinko")

    mu = np.mean(balls)  # calculate statistical parameters
    sigma = np.std(balls)
    norm_x = np.linspace(-num_levels // 2, num_levels // 2, 100)
    norm_y = stats.norm(mu, sigma).pdf(norm_x)  # superimpose normal distribution
    ax.plot(
        norm_x, norm_y, color="red", linewidth=2, label="Normal"
    )  # plot with red line

    ax.set_title(
        f"Pachinko vs. Normal PDF ({num_levels:,} levels : " f"{num_balls:,} balls)"
    )
    ax.set_xlabel("Slot Number")
    ax.set_ylabel("Probability")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
