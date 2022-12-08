import numpy as np
import pandas as pd
import re


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        puzzle_input = f.readlines()

    stack_drawing = []
    instructions = []
    for line in puzzle_input:
        if "[" in line:
            stack_drawing.append(line)
        elif line.startswith("move"):
            instructions.append(line)

    moves = parse_instructions(instructions)
    stacks = parse_stack_drawing(stack_drawing)

    return moves, stacks


def parse_instructions(instructions):
    move_numbers = re.findall(r"\d+", "".join(instructions), flags=re.MULTILINE)
    moves = pd.DataFrame(
        np.array(move_numbers, dtype=int).reshape(len(move_numbers) // 3, 3),
        columns=["n", "from", "to"],
    )
    return moves


def parse_stack_drawing(stack_drawing):
    stack_array = np.array([list(stack) for stack in stack_drawing]).T
    stacks_with_empties = stack_array[1:-1:4].tolist()
    stacks = {
        i + 1: list("".join(stack).strip())
        for i, stack in enumerate(stacks_with_empties)
    }
    return stacks


def get_top_crates(stacks):
    return "".join([stack[0] for stack in stacks.values()])
