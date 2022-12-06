#! /usr/bin/env python3

from utils import load_input


def main(practice=False):
    sections = load_input(practice=practice)

    # First elf _within_ second elf
    first_within_second = (sections[0] >= sections[2]) & (sections[1] <= sections[3])
    # Second elf _within_ first elf
    second_within_first = (sections[0] <= sections[2]) & (sections[1] >= sections[3])
    total = (first_within_second + second_within_first).sum()

    print(f"In {total} assignment pairs one range fully contains the other.")
    return total


if __name__ == "__main__":
    main()
