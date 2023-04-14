def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        program = [line.strip() for line in f.readlines()]
    return program
