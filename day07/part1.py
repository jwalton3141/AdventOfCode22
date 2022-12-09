#! /usr/bin/env python3

import numpy as np

from utils import load_input, get_dir_sizes


def main(practice=False):
    tty = load_input(practice=practice)

    dir_sizes = get_dir_sizes(tty)
    sizes = np.array(list(dir_sizes.values()))
    sum_of_small = sizes[sizes <= 100000].sum()

    print(f"The sum total of the directories smaller than 100000 is {sum_of_small}")
    return sum_of_small


if __name__ == "__main__":
    main()
