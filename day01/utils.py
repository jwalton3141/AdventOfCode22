def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"

    with open(filename) as f:
        calories = [line.strip() for line in f.readlines()]

    return calories
