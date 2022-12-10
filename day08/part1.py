#! /usr/bin/env python3

from itertools import product
import numpy as np

from utils import load_input


def get_visibility(trees):
    nrows, ncols = trees.shape

    is_visible = np.zeros((nrows, ncols), dtype=int)
    is_visible[[0, -1]] = 1
    is_visible.T[[0, -1]] = 1

    for i, j in product(range(1, nrows - 1), range(1, ncols - 1)):
        tree = trees[i, j]
        row, col = trees[i], trees[:, j]
        # left, right, top, bottom
        for neighbours in row[:j], row[j + 1 :], col[:i], col[i + 1 :]:
            if np.all(neighbours < tree):
                is_visible[i, j] = True
                continue

    return is_visible


def main(practice=False):
    trees = load_input(practice=practice)
    is_visible = get_visibility(trees)
    total_visible = is_visible.sum()

    print(f"{total_visible} trees are visible from outside the grid.")
    return total_visible


if __name__ == "__main__":
    main()
