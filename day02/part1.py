#! /usr/bin/env python3

import pandas as pd

from utils import load_input


def decode_strategy(their_plays, our_plays):
    shapes = ["rock", "paper", "scissors"]
    decoder = dict(zip(["A", "B", "C", "X", "Y", "Z"], shapes * 2))
    return their_plays.map(decoder), our_plays.map(decoder)


def score_shapes(our_plays):
    shape_scorecard = {"rock": 1, "paper": 2, "scissors": 3}
    return (our_plays.value_counts() * pd.Series(shape_scorecard)).sum()


def score_outcomes(their_plays, our_plays):
    shape_to_beat = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

    score = 0
    for their_play, our_play in zip(their_plays, our_plays):
        if our_play == their_play:
            score += 3
        elif our_play == shape_to_beat[their_play]:
            score += 6

    return score


def main(practice=False):
    their_plays, our_plays = load_input(practice=practice)
    their_plays, our_plays = decode_strategy(their_plays, our_plays)

    score = score_shapes(our_plays)
    score += score_outcomes(their_plays, our_plays)

    print(f"We scored {score} points.")

    return score


if __name__ == "__main__":
    main()
