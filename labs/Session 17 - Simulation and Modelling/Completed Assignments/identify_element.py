#!/usr/bin/env python3
# quadratic_regression_sklearn.py


import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import sys
import os
from statistics import mean


def fit_linear(vec_x, vec_y):  # linear fit function, pass in vec_x and vec_y
    vec_x = vec_x.reshape(-1, 1)  # put each element in an array
    model = LinearRegression().fit(vec_x, vec_y)  # pass in indep and dep,
    # output is a tuple
    m = model.coef_  # unpack tuple element
    b = model.intercept_
    return m, b


def fit_quartic(vec_x, vec_y):
    vec_x = vec_x.reshape(-1, 1)
    transformer = PolynomialFeatures(degree=4, include_bias=False)
    # degree four is the degree of our polynomial fit function, multiply
    # x values so they are close in range to y, then later
    # undoes that, so we can minimize roundoff error.
    transformer.fit(vec_x)
    vec_x_ = transformer.transform(vec_x)
    model = LinearRegression().fit(vec_x_, vec_y)
    d, c, b1, a = model.coef_  # coefficients of quartic polynomial
    e = model.intercept_  # intercept of the quartic polynomial
    return a, b1, c, d, e


def slope_from_quartic(vec_x, vec_y, b2):  # vectorized, at each point we take
    # three derivatives of the quartic polynomial and solve for slope (in this
    # case m=n)
    return (vec_y - 6 * b2) / vec_x


def plot_fits(ax, vec_x, vec_y, a, b1, c, d, e):
    x = np.linspace(np.min(vec_x), np.max(vec_x), 1000)  # make our x range from
    # the lowest x to the highest x, chopped into 1000 intervals

    ax.plot(
        x, a * x**4 + b1 * x**3 + c * x**2 + d * x + e, label="Quartic Fit"
    )  # ax.plot(x, f(x), label)

    print(
        f"\n Quartic fit: y = ({a:.4f})x^4 + ({b1:.4f})x^3 + ({c:.4})x^2 + ({d:.4f})x + ({e:.4f}) \n"
    )

    m, b = fit_linear(vec_x, vec_y)
    ax.plot(x, m * x + b, label=r"$PV = nRT$")

    ax.scatter(vec_x, vec_y, color="red")

    ax.set_title(r"$ PV \ Vs. RT$", fontsize=20)
    ax.set_xlabel(r"$ RT \ (\frac{atm \cdot L}{mol})$", fontsize=16)
    ax.set_ylabel(r"$ PV \ (atm \cdot L)$", fontsize=16)
    ax.legend()


def main():
    x = np.array([-50, 0, 50, 100, 150])  # raw x
    y = np.array([11.6, 14, 16.2, 19.4, 21.8])  # raw y
    vec_x = 0.082057 * (273.15 + x)  # proper x (x = R * T(kelvin))
    vec_y = 2.00 * y  # proper y (y = P * V)
    a, b1, c, d, e = fit_quartic(vec_x, vec_y)  # unpack tuple outputted
    # from fit_quartic()

    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot_fits(ax, vec_x, vec_y, a, b1, c, d, e)

    print(
        f"The average molar mass was found to be {50 / mean(slope_from_quartic(vec_x, vec_y, b1)):.3f} grams per mole."
        f" The molar mass of Argon is 39.948 grams per mole. Therefore the mystery gas is Ar with a relative error of"
        f" {(50 / mean(slope_from_quartic(vec_x, vec_y, b1)) - 39.948) / 39.948 * 100:.3f}%."
    )  # each element has a unique molar mass (g / mol), which can be calculated
    # since we found the average number of moles and we were given the mass.
    # Also, since significant figures are a thing, the final result should
    # technically be 41 g / mol because I used a number with at most two sig figs
    # for the calculation (50).

    plt.show()


if __name__ == "__main__":
    main()
