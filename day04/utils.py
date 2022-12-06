import numpy as np
import re


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        sections = [re.split(",|-", line.strip()) for line in f.readlines()]
    return np.array(sections, dtype=int).T
