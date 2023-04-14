#! /usr/bin/env python3

"""
Incomplete solution.
"""

import numpy as np

from utils import load_input


def punch_pixel(cycle_num, register, screen):
    if cycle_num in [register-1, register, register+1]:
        row = (cycle_num - 1) // screen.shape[1]
        col = (cycle_num - 1) % screen.shape[1]
        screen[row, col] = 1


def main(practice=False):
    program = load_input(practice=practice)

    screen_width = 40
    screen_height = 6
    screen = np.zeros((screen_height, screen_width), dtype=int)

    register = 1
    cycle_num = 1
    for instruction in program:
        punch_pixel(cycle_num, register, screen)
        cycle_num += 1
        punch_pixel(cycle_num, register, screen)

        if instruction.startswith("addx"):
            cycle_num += 1
            punch_pixel(cycle_num, register, screen)

            register += int(instruction.split()[1])
            punch_pixel(cycle_num, register, screen)

    return screen


if __name__ == "__main__":
    main(practice=True)
