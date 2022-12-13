import numpy as np
import pandas as pd


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    motions = pd.read_csv(
        filename, sep=" ", header=None, names=["direction", "distance"]
    )
    head_locs = motions_to_locs(motions)
    return head_locs


def motions_to_locs(motions):
    # Form a single string representing the moves. eg. RRRULDL
    repeated_directions = (motions["direction"] * motions["distance"]).sum()

    direction_to_vector = {
        "R": [1, 0],
        "L": [-1, 0],
        "U": [0, 1],
        "D": [0, -1],
    }
    head_moves = np.array(
        [direction_to_vector[direction] for direction in repeated_directions]
    )
    head_locs = head_moves.cumsum(0)
    return head_locs
