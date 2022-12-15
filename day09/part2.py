#! /usr/bin/env python3

import numpy as np

from utils import load_input, simulate_rope


def main(practice=False):
    head_locs = load_input(practice=practice)
    locs = simulate_rope(head_locs, rope_length=9)
    locs = np.unique(locs, axis=0).shape[0]
    print(f"The tail visited {locs} unique positions.")
    return locs


if __name__ == "__main__":
    main()
