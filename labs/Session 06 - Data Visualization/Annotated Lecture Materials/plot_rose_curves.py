#!/usr/bin/env python3
# plot_rose_curves.py

import matplotlib.pyplot as plt
import numpy as np
import sys
import os


def plot(ax):
    theta = np.linspace(0, 4 * np.pi, 1000) #array of thetas, theta ranges from 0 to 4pi,
    #1000 subdomains (array has 1000 elements)
    radius_1 = 4 + 4 * np.cos(4 * theta) #first curve, swing twice around 
    #circle , r = 4cos(4theta) + 4
    radius_2 = 3 + 3 * np.cos(4 * theta + np.pi)
    radius_3 = 5 + 5 * np.cos(3 / 2 * theta)
    #radius_4 = 7 + 7 * np.cos(5 * theta) * np.sin(11 * theta)

    ax.plot(theta, radius_1, color="blue") #plot radius_1 in blue
    #ax.plot(theta, radius_2, color="green") #different color to superimpose this plot on 
    # radius_1
    #ax.plot(theta, radius_3, color="red") 
    #ax.plot(theta, radius_4, color="black")

    ax.set_aspect("equal") #x and y resolutions equal for laptop display
    ax.axis() #overlay x and y axes


def main():
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"}) #change projection to be
    #polar, dictionary data type
    fig.canvas.set_window_title(os.path.basename(sys.argv[0])) #give the figure 
    #the filename
    plot(ax) #make graph
    plt.show() #show graph


if __name__ == "__main__":
    main()
