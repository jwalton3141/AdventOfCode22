## Solutions

I struggled for quite a while in deciding what an appropriate data structure to
store the directory tree in should look like. Once I settled on an appropriate
structure, the puzzle was easy to solve.

To begin with, I spent some time pursuing the idea of constructing a dictionary
of nested dictionaries, with each nesting representing another level in the
directory tree. However, this turned out to be more involved than I initially
anticipated.

I also spent some time thinking that the only thing I really needed to keep
track of was my current directory name, and my depth in the tree. Although I
think this may be a valid approach to the problem, I realised a simpler
approach was simply to create a dictionary where each key is a full directory
path!

The real workhorse of my approach is in the following snippet:
```py
dir_sizes = {}
current_dir = []

for line in tty:
    if re_match := re.match(r"\$ cd (\w+|/)", line):
        # Change current directory
        current_dir.append(re_match.groups()[0])
        # Create an entry in the dir_size dict
        dir_sizes["".join(current_dir)] = 0
    elif line.startswith("$ cd .."):
        # Move up a directory
        current_dir.pop()
    elif re_match := re.match(r"\d+", line):
        # Extract filesize
        filesize = int(re_match.group())
        # Add size to current directory and all parents
        for i in range(1, len(current_dir) + 1):
            dir_sizes["".join(current_dir[:i])] += filesize
```

`current_dir` is a list which records the current directory. We move down the
tree by `append`ing  new values to this list
(`current_dir.append(re_match.groups()[0]) `), and move up the tree by
`pop`ping the last value in the list (`current_dir.pop()`).

If we find any files in a directory, we add the size of the file to the
corresponding key's value in `dir_sizes`, and to any parent directories, with:
```py
for i in range(1, len(current_dir) + 1):
    dir_sizes["".join(current_dir[:i])] += filesize
```

### Part 1

Once an appropriate data structure has been constructed (`get_dir_sizes()`), it
was trivial to use a numpy array and boolean mask to find the sum of the
directories smaller than or equal to `100000` (`sizes[sizes <= 100000].sum()`).

### Part 2

Again, this part is easy to solve once an appropriate data structure has been
created. Again, I make use of a numpy array and boolean mask to compute the
smallest directory which could be removed to fix the file system.
