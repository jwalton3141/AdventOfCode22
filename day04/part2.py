#! /usr/bin/env python3

from utils import load_input


def main(practice=False):
    sections = load_input(practice=practice)

    # Find cases with no overlap at all
    all_smaller = sections[1] < sections[2]
    all_greater = sections[0] > sections[3]
    # Cases with any overlap is total minus cases with no overlap
    total = sections.shape[1] - (all_greater + all_smaller).sum()

    print(f"In {total} assignment pairs the ranges overlap.")
    return total


if __name__ == "__main__":
    main()
