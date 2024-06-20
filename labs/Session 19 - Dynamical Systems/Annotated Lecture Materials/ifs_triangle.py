#!/usr/bin/env python3
# ifs_triangle.py

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 200_000  # iterate 200,000 times
    x, y = 0, 0

    # # Iterate (but don't draw) to let IFS reach its stable orbit
    # for _ in range(100):
    #     x, y, color = ifs.transform_point(x, y) #reach stable orbit

    for _ in range(iterations):  # plot 200,000 additional orbits
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    ifs.set_base_frame(0, 0, 30, 30)  # specify size of base frame

    p = 1 / 3  # 3 transforms, equal probability
    ifs.add_mapping(0, 0, 15, 0, 0, 15, "red", p)
    ifs.add_mapping(15, 0, 30, 0, 15, 15, "green", p)  # define mappings
    ifs.add_mapping(7.5, 15, 22.5, 15, 7.5, 30, "blue", p)

    ifs.generate_transforms()  # solves linear algebra problem

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(1000, 1000),
        draw_function=plot_ifs,
        title="Sierpinksi Triangle",
    )
    ss.show()


if __name__ == "__main__":
    main()
