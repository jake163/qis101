#!/usr/bin/env python3
# logistics_map.py

import numpy as np
from simple_screen import SimpleScreen  # simplescreen is a shimlayer that lets

# user do math in world coordinates, convert to screen coordinates


def plot_logistics_map(ss):  # pass in simplescreen
    for sx in range(ss.screen_width):  # iterate from 2.5 to 4
        x = ss.world_x(sx)
        y = np.random.random()  # pick random y

        # Iterate (but don't draw) to reach a stable orbit
        for i in range(500):
            y = x * y * (1 - y)  # output becomes the input

        for i in range(500):
            y = x * y * (1 - y)
            ss.set_world_pixel(x, y, "blue")  # when you get x and y, set
            # the point as a world pixel


def main():
    ss = SimpleScreen(
        world_rect=((2.5, 0), (4.0, 1)),  # (xmin, ymin), (xmax, ymax)
        draw_function=plot_logistics_map,
        screen_size=(1080, 1080),  # specify screen pixel size, keep square
        title="Logistics Map",
    )
    ss.show()  # calls plotting function


if __name__ == "__main__":
    main()
