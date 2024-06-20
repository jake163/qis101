#!/usr/bin/env python3
# common_statistics.py

import numpy as np
import statistics
from collections import Counter


def mean(samples):  # pass in samples from main()
    return np.sum(samples) / samples.size  # calculate main of samples with numpy


def median(samples):
    s = np.sort(samples)  # sort the sample by size with numpy
    i = s.size // 2  # divide sample size in half, round down
    if s.size % 2 == 1:
        # Use middle element if length is odd
        m = s[i]
    else:
        # Use mean of middle two items if length is even
        m = (s[i - 1] + s[i]) / 2
    return m


def mode(samples):
    # Create a dictionary to tally the occurrence of each value
    count = Counter(sorted(samples))
    # count is a dictionary: value and frequency of value
    # Find the maximum count of all keys (samples)
    max_count = max(count.values())
    # Select the keys which have that max count
    m = [k for k, v in count.items() if v == max_count]
    # give back frequency of the max count number(s)
    return m


def pop_variance(samples):
    m = mean(samples)
    # Numpy n-dimensional arrays are inherently vectorized
    # so element-level arithmetic can be expressed at the array-level
    # without having to loop through each element individually
    v = sum((samples - m) ** 2) / samples.size
    return v


def main():
    np.random.seed(2021)
    samples = np.random.randint(0, 100, 30)  # random integer from 0 to 99, 30 of them
    print(f"Samples      = {samples.tolist()}")  # print list of samples
    print()

    print(f"Mean         = {mean(samples):.4f}")  # print mean() output, ten thousandths
    print(
        f"Mean         = {np.mean(samples):.4f}"
    )  # print output of numpy mean function,
    # thousandths
    print()

    print(f"Median       = {median(samples):.4f}")  # Median() output
    print(f"Median       = {np.median(samples):.4f}")  # numpy median function output
    print()

    print(f"Mode         = {mode(samples)}")  # mode() output
    print(
        f"Mode         = {sorted(statistics.multimode(samples))}"
    )  # output of mode function
    # that isn't numpy
    print()

    v = pop_variance(samples)
    print(
        f"Pop Variance = {v:.4f}"
    )  # print output of variance function that was written
    print(f"Pop Variance = {np.var(samples):.4f}")  # print numpy's variance
    print()

    print(f"Pop Std. Dev = {np.sqrt(v):.4f}")  # print std. dev. output of our function
    print(f"Pop Std. Dev = {np.std(samples):.4f}")  # print numpy's output


if __name__ == "__main__":
    main()
