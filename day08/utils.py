import numpy as np


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        trees = [list(row.strip()) for row in f.readlines()]
    return np.array(trees, dtype=int)
