#! /usr/bin/env python3

import pandas as pd

from utils import load_input


def decode_strategy(their_plays, outcomes):
    shape_decoder = dict(zip(["A", "B", "C"], ["rock", "paper", "scissors"]))
    outcome_decoder = dict(zip(["X", "Y", "Z"], ["loss", "draw", "win"]))
    return their_plays.map(shape_decoder), outcomes.map(outcome_decoder)


def score_outcomes(outcomes):
    outcome_scorecard = {"loss": 0, "draw": 3, "win": 6}
    return (outcomes.value_counts() * pd.Series(outcome_scorecard)).sum()


def score_shapes(their_plays, outcomes):
    shape_to_beat = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
    shape_scorecard = {"rock": 1, "paper": 2, "scissors": 3}

    score = 0
    for their_play, outcome in zip(their_plays, outcomes):
        if outcome == "draw":
            shape_to_play = their_play
        elif outcome == "win":
            shape_to_play = shape_to_beat[their_play]
        else:
            shape_to_play = shape_to_beat[shape_to_beat[their_play]]

        score += shape_scorecard[shape_to_play]

    return score


def main(practice=False):
    their_plays, outcomes = load_input(practice=practice)
    their_plays, outcomes = decode_strategy(their_plays, outcomes)

    score = score_outcomes(outcomes)
    score += score_shapes(their_plays, outcomes)

    print(f"We scored {score} points.")

    return score


if __name__ == "__main__":
    main()
