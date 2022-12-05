import pandas as pd


def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    strategy = pd.read_csv(filename, header=None, sep=" ")
    return strategy[0], strategy[1]
