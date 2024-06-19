#!/usr/bin/env python3
# ifs_hexagonal.py

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem
import numpy as np

ifs = IteratedFunctionSystem()


def rgb():
    colors = [0] * 3
    while colors == ([0] * 3):
        colors = [
            np.random.randint(0, 256) for i in range(3)
        ]  # randomly generates three rgb values, in list, every time function
        # is called
    return colors


def plot_ifs(ss):
    iterations = 200_000  # iterate 200,000 times
    x, y = 0, 0

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)  # reach stable orbit

    for _ in range(iterations):  # plot 200,000 additional orbits
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    ifs.set_base_frame(0, 0, 30, 30)  # specify size of base frame

    p = 1 / 6  # 6 transforms, equal probability
    ifs.add_mapping(25, 15, 15, 15, 20, (15 + 5 * np.sqrt(3)), rgb(), p)  # COD
    ifs.add_mapping(
        20, (15 + 5 * np.sqrt(3)), 15, 15, 10, (15 + 5 * np.sqrt(3)), rgb(), p
    )  # DOE
    ifs.add_mapping(10, (15 + 5 * np.sqrt(3)), 15, 15, 5, 15, rgb(), p)  # EOF
    ifs.add_mapping(5, 15, 15, 15, 10, (15 - 5 * np.sqrt(3)), rgb(), p)  # FOA
    ifs.add_mapping(
        10, (15 - 5 * np.sqrt(3)), 15, 15, 20, (15 - 5 * np.sqrt(3)), rgb(), p
    )  # AOB
    ifs.add_mapping(20, (15 - 5 * np.sqrt(3)), 15, 15, 25, 15, rgb(), p)  # BOC

    ifs.generate_transforms()  # solves linear algebra problem

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(1000, 1000),  # 1000^2 pixels
        draw_function=plot_ifs,
        title="Colorful Soccer Ball",
    )
    ss.show()


if __name__ == "__main__":
    main()
