#! /usr/bin/env python3

from itertools import product
import numpy as np

from utils import load_input


def get_scores(trees):
    nrows, ncols = trees.shape
    scores = np.ones((nrows, ncols), dtype=int)

    # Loop over trees
    for i, j in product(range(nrows), range(ncols)):
        tree = trees[i, j]
        row, col = trees[i], trees[:, j]

        left, right, top, bottom = (
            row[:j][::-1],
            row[j + 1 :],
            col[:i][::-1],
            col[i + 1 :],
        )
        for neighbours in left, right, top, bottom:
            # If no neighbours
            if not len(neighbours):
                pass

            blockers = neighbours >= tree
            # If no blockers
            if np.all(~blockers):
                scores[i, j] *= len(blockers)
            else:
                scores[i, j] *= np.argmax(blockers) + 1

    return scores


def main(practice=False):
    trees = load_input(practice=practice)
    scores = get_scores(trees)
    max_score = scores.max()

    print(f"{max_score} is the highest scenic score possible.")
    return max_score


if __name__ == "__main__":
    main()
