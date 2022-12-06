#! /usr/bin/env python3

from utils import load_input, sum_priorities


def get_badges(rucksacks):
    n_groups = len(rucksacks) // 3
    badges = [""] * n_groups
    for i in range(n_groups):
        group = rucksacks[3 * i : 3 * (i + 1)]
        badges[i] = (
            group[0].intersection(group[1]).intersection(group[2]).pop()
        )

    return badges


def main(practice=False):
    rucksacks = [set(rucksack) for rucksack in load_input(practice=practice)]
    badges = get_badges(rucksacks)
    summed_priorities = sum_priorities(badges)

    print(f"The sum of the priorities of the badges is {summed_priorities}.")
    return summed_priorities


if __name__ == "__main__":
    main()
