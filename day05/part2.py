#! /usr/bin/env python3

from utils import load_input, get_top_crates


def move_stacks(moves, stacks):
    for i, move in moves.iterrows():
        for i in range(move["n"] - 1, -1, -1):
            stacks[move["to"]].insert(0, stacks[move["from"]].pop(i))
    return stacks


def main(practice=False):
    moves, stacks = load_input(practice=practice)
    stacks = move_stacks(moves, stacks)
    top_crates = get_top_crates(stacks)

    print(f"After rearrangement, we should pass the elves the message {top_crates}.")
    return top_crates


if __name__ == "__main__":
    main()
