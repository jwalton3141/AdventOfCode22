def load_input(practice=False):
    filename = f"input{'_practice' * practice}.txt"
    with open(filename) as f:
        msg = f.readline().strip()
    return msg


def first_chunk_without_repeats(msg, chunk_length):
    for i in range(len(msg) - chunk_length):
        if len(set(msg[i : chunk_length + i])) == chunk_length:
            return chunk_length + i
