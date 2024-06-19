#!/usr/bin/env python3
# freq_histogram.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from typing import (
    Counter,
)  # give array, returns tuple which has character and frequency
import os
import sys


def plot(ax, file_name):
    f_in = open(
        file_name, "rb"
    )  # open file_name, read in binary format, store as local
    # variable f_in
    f_bytes = bytearray(
        f_in.read()
    )  # create array of bites based on the reading of f_in
    file_size = (
        f_in.tell()
    )  # tell just tells size of file, could also get length of array
    f_in.close()  # close file

    ticks = []  # empty list
    char_count = np.zeros(256)  # make an array of counts, initialize to zero
    for char, count in Counter(
        f_bytes
    ).items():  # pass in byte array to Counter(), tally
        # how many time each character appears, unpack tuple
        char_count[char] = count
        if count / file_size > 0.06:  # don't add to ticks unless freq > 6%
            ticks.append(char)  # append to tick

    base = os.path.basename(file_name)  # path
    text_name = os.path.splitext(base)[0]  # split pathname into root and ext
    ax.set_title(f"Frequency Analysis ({text_name})")
    ax.set_xlabel("ASCII Value")
    ax.set_ylabel("Count")

    ax.bar([*range(256)], char_count)  # make bar chart

    ax.xaxis.set_ticks(ticks)  # set axis based on ticks
    ax.xaxis.set_tick_params(rotation=90)
    ax.yaxis.set_minor_locator(AutoMinorLocator())


def main(file_name):  # define main argument, takes file_name input
    fig = plt.figure(os.path.basename(sys.argv[0]))
    fig.set_size_inches(12, 8)  # set size of display
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax, file_name)  # pass file_name into plot function
    plt.show()


if __name__ == "__main__":  # run script from command line
    file_name = None  # local variable file_name is None
    if len(sys.argv) == 1:  # no second argument, no filename.
        print("You must provide a filename")
    else:
        file_name = sys.argv[
            1
        ]  # the second argument in argument vector is the filename
        main(file_name)  # pass that into main
