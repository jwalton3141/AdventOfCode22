#! /usr/bin/env python3

from utils import load_input, first_chunk_without_repeats


def main(practice=False):
    msg = load_input(practice=practice)
    pos = first_chunk_without_repeats(msg, 14)
    print(f"The start-of-message marker was detected at position {pos}.")
    return pos


if __name__ == "__main__":
    main()
