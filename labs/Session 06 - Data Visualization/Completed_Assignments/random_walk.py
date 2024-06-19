#!/usr/bin/env python3
# random_walk.py

import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import random


def plot(ax):  # pass in ax
    x_array = []
    y_array = []
    counter = 0
    while counter <= 10_000:  # iterating to obtain 10,000 (x,y) points
        theta = random.uniform(0.00, 6.28)  # randomly generated theta, inclusive exclusive
        if counter == 0:
            x = np.cos(theta)  # calculate random x, r = 1
            y = np.sin(theta)  # calculate random y, r = 1
            x_array.append(x)  # add x to x_array
            y_array.append(y)
        
        if counter > 0:
            x += np.cos(theta)
            y += np.sin(theta)
            x_array.append(x)  
            y_array.append(y)
        
        counter += 1 
    
    ax.plot(x_array, y_array)
    ax.set_title("Random Walk")
    ax.set_xlabel("x")  
    ax.set_ylabel("y")
    ax.axhline(linewidth=1, color="black")  # make the x axis line black
    ax.axvline(linewidth=1, color="black")
    ax.set_aspect("equal")

def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))

    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
