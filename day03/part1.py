#! /usr/bin/env python3

from utils import load_input, sum_priorities


def get_misfiled_items(rucksacks):
    misfiled_items = [""] * len(rucksacks)
    for i, rucksack in enumerate(rucksacks):
        items_per_compartment = len(rucksack) // 2
        compartments = [
            set(rucksack[:items_per_compartment]),
            set(rucksack[items_per_compartment:]),
        ]
        misfiled_items[i] = compartments[0].intersection(compartments[1]).pop()

    return misfiled_items


def main(practice=False):
    rucksacks = load_input(practice=practice)
    misfiled_items = get_misfiled_items(rucksacks)
    summed_priorities = sum_priorities(misfiled_items)

    print(
        f"The sum of priorities of items in both compartments is {summed_priorities}."
    )
    return summed_priorities


if __name__ == "__main__":
    main()
