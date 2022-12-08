#! /usr/bin/env python3

import numpy as np
import re

from utils import load_input


def main(practice=False):
    tty = load_input(practice=practice)
    
    dir_size = {}
    current_dir = []
    for line in tty:
        if re_match := re.match(r"\$ cd (\w+|/)", line):
            current_dir.append(re_match.groups()[0])
            dir_size["".join(current_dir)] = 0
        elif line.startswith("$ cd .."):
            current_dir.pop()
        elif re_match := re.match(r"\d+", line):
            filesize = int(re_match.group())
            for i in range(1, len(current_dir)+1):
                dir_size["".join(current_dir[:i])] += filesize
    
    dir_sizes = np.array(list(dir_size.values()))
    sum_of_small_dirs = dir_sizes[dir_sizes <= 100000].sum()
    print(sum_of_small_dirs)
    return sum_of_small_dirs


if __name__ == "__main__":
    main()
