#! /usr/bin/env python3

from utils import load_input


def main(practice=False):
    calories = load_input(practice=practice)

    running_total = [0, 0, 0]
    current_total = 0
    # Appending an empty entry helps handle the last elf
    for calorie in calories + [""]:
        if calorie:
            current_total += int(calorie)
        else:
            if current_total > min(running_total):
                running_total[0] = current_total
            current_total = 0
            running_total.sort()

    sum_running_total = sum(running_total)
    print(f"The greediest three elves stockpiled {sum_running_total} calories.")

    return sum_running_total


if __name__ == "__main__":
    main()
