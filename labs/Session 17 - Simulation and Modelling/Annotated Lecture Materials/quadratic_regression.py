#!/usr/bin/env python3
# quadratic_regression.py


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import sys
import os


def fit_linear(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    model = LinearRegression().fit(vec_x, vec_y)
    m = model.coef_
    b = model.intercept_
    return m, b


def fit_quadratic(vec_x, vec_y):
    sum_x = sum(vec_x)
    sum_x2 = sum(vec_x**2)
    sum_x3 = sum(vec_x**3)
    sum_x4 = sum(vec_x**4)

    sum_y = sum(vec_y)
    sum_xy = sum(vec_x * vec_y)
    sum_x2y = sum(vec_x**2 * vec_y)

    coeffs = np.array(
        [[sum_x4, sum_x3, sum_x2], [sum_x3, sum_x2, sum_x], [sum_x2, sum_x, len(vec_x)]]
    )

    vals = np.array([sum_x2y, sum_xy, sum_y])

    det_coeffs = np.linalg.det(coeffs)  # determinants of coeff matrices

    mat_a = np.copy(coeffs)
    mat_a[:, 0] = vals  # 1st column of mat_a is vals
    det_a = np.linalg.det(mat_a)  # compute det of mat a

    mat_b = np.copy(coeffs)
    mat_b[:, 1] = vals
    det_b = np.linalg.det(mat_b)  # det of mat b

    mat_c = np.copy(coeffs)
    mat_c[:, 2] = vals
    det_c = np.linalg.det(mat_c)  # det of mat c

    a = det_a / det_coeffs  # compute coefficients with cramers rule
    b = det_b / det_coeffs
    c = det_c / det_coeffs

    return a, b, c


def f(a, b, c, x):
    return a * x**2 + b * x + c


def plot(ax):
    vec_x = np.array([1, 2, 3, 4, 5, 6, 7, 8])  # number of mins * 10
    vec_y = np.array([205, 430, 677, 945, 1233, 1542, 1872, 2224])
    # tape counter reading

    x = np.linspace(np.min(vec_x), np.max(vec_x), 1000)  # x to range from
    # min x value to max x value, 1000 subintervals

    a, b, c = fit_quadratic(vec_x, vec_y)  # calculate partial sums, find coeffs
    # put into array, do cramers rule
    ax.plot(x, a * x**2 + b * x + c, label="Quadratic")  # plot quadratic curve

    print(f"y = ({a:.4f})x^2 + ({b:.4f})x + ({c:.4})")
    print(f"Tape counter at 65 mins = {f(a,b,c,6.5):,.4f}")  # shows the point
    # at 65 mins

    m, b = fit_linear(vec_x, vec_y)  # show the linear curve of x and y
    ax.plot(x, m * x + b, label="Linear")

    ax.scatter(vec_x, vec_y, color="red")  # plot the points in red

    ax.set_title("Tape Counter Per Minute")
    ax.set_xlabel("Elapsed time x10 (min)")
    ax.set_ylabel("Tape Counter")
    ax.legend()


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)
    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
