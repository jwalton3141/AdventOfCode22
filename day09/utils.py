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


def simulate_rope(head_locs, rope_length=1):
    locs = head_locs.copy()
    for _ in range(rope_length):
        locs = follow(locs)
    return locs


def follow(ahead_locs):
    behind_locs = np.array([[0, 0]])
    behind_loc = behind_locs[0]

    for ahead_loc in ahead_locs:
        TH = ahead_loc - behind_loc  # noqa: N806
        d = np.abs(TH).sum()

        # Don't move
        if d < 2:
            continue
        # If a vertical or horizontal move
        elif 0 in TH:
            behind_loc = (ahead_loc + behind_loc) // 2
        # Diagonal move
        elif d > 2:
            behind_loc += np.sign(TH)

        behind_locs = np.vstack([behind_locs, behind_loc])

    return behind_locs
