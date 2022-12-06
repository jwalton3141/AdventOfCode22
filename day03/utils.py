import pandas as pd
import string


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        rucksacks = [line.strip() for line in f.readlines()]
    return rucksacks


def sum_priorities(items):
    letters = list(string.ascii_lowercase + string.ascii_uppercase)
    priorities = pd.Series(range(1, 53), index=letters)
    return priorities[items].sum()
