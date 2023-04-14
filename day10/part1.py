#! /usr/bin/env python3

from utils import load_input


def main(practice=False):
    program = load_input(practice=practice)
    cycles = list(range(20, 221, 40))

    register = 1
    cycle_num = 1
    line_num = 0
    signal_strength_sum = 0
    while cycle_num < max(cycles)+1:
        instruction = program[line_num]
        cycle_num += 1

        if cycle_num in cycles:
            signal_strength_sum += register * cycle_num

        if instruction.startswith("addx"):
            cycle_num += 1
            register += int(program[line_num].split()[1])
            if cycle_num in cycles:
                signal_strength_sum += register * cycle_num

        line_num += 1

    print(f"The sum of the signal strength at cycles {cycles} is {signal_strength_sum}.")
    return signal_strength_sum


if __name__ == "__main__":
    main()
