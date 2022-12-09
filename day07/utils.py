import re


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        tty = [line.strip() for line in f.readlines()]
    return tty


def get_dir_sizes(tty):
    dir_sizes = {}
    current_dir = []
    for line in tty:
        if re_match := re.match(r"\$ cd (\w+|/)", line):
            current_dir.append(re_match.groups()[0])
            dir_sizes["".join(current_dir)] = 0
        elif line.startswith("$ cd .."):
            current_dir.pop()
        elif re_match := re.match(r"\d+", line):
            filesize = int(re_match.group())
            for i in range(1, len(current_dir) + 1):
                dir_sizes["".join(current_dir[:i])] += filesize
    return dir_sizes
