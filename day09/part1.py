#! /usr/bin/env python3

import numpy as np

from utils import load_input


def main(practice=False):
    head_locs = load_input(practice=practice)

    tail_locs = np.array([[0, 0]])
    tail_loc = tail_locs[0]
    for head_loc in head_locs:
        TH = head_loc - tail_loc
        d = np.abs(TH).sum()

        # Don't move
        if d < 2:
            continue
        # If a vertical or horizontal move
        elif 0 in TH:
            tail_loc = (head_loc + tail_loc) // 2
        # Diagonal move
        elif d > 2:
            tail_loc += np.sign(TH)

        tail_locs = np.vstack([tail_locs, tail_loc])

    unique_locs = np.unique(tail_locs, axis=0).shape[0]

    print(f"The tail visited {unique_locs} unique positions.")
    return unique_locs


if __name__ == "__main__":
    main()
