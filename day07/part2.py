#! /usr/bin/env python3

import numpy as np

from utils import load_input, get_dir_sizes


def main(practice=False):
    tty = load_input(practice=practice)

    dir_sizes = get_dir_sizes(tty)

    total_disk = 70000000
    required_unused = 30000000
    max_size = total_disk - required_unused
    min_to_rm = dir_sizes["/"] - max_size

    sizes = np.array(list(dir_sizes.values()))
    smallest_fix = sizes[sizes >= min_to_rm].min()

    print(f"The smallest directory removable to fix the system is {smallest_fix}.")
    return smallest_fix


if __name__ == "__main__":
    main()
