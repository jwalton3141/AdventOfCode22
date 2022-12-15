## About

These are my solutions to the 2022 [Advent of
Code](https://adventofcode.com/2022) challenge

Calendar:
```
@@##@##@@@@@@#@@@@#@@@#@#@###@@@@#@@#@@@#@@#@#@#@  25
@@@@@@@##@@@@#@#@@@@#@@@##@@@@@###@#@##@##@@@@@@#  24
@@@###@@@@####@@#@@@@@@@@#@@@#@@@@@@###@@@#@#@##@  23
@@@@@@@##@@#@#@@#@@@@####@@@@@@#@#@@@#@#@@@#@#@@@  22
@@@@#@##@@#@@@@#@#@@@#@@@#@@@@##@@@@@@#@##@@@@@##  21
@#@#@@@#@@#@@@@###@#@@@@@@@#@@#@@@@#@#@@@@@@@@@#@  20
@#@@#@#@@@@@@@@@@@@#|@#@##@@#@@@#@###@@#@@@@##@@#  19
@#@@#@#@@@@@##@@@@@#@@@@##@@#@@#@@##@@@##@@##@##@  18
#@@@##@@##@##@#@@@@@@@@#@@@@@@@#@@@@#@#@@@#@#@@##  17
@@#@@@@@@@@#@#@#@@@@@@@@@#@#@@#@@@@@#@#@@@@@#@@@#  16
@@@#@@@@@@@#@@@@@@@@@#@@@@@@@@@@@#@#@@#@#@#@@#@@#  15
@@#@#@#@###@@@#@@@@@#@##@@@@@@@#@@#@##@@###@@##@@  14
##@@#@####@@@#@#@#@@@@@@#@@@@#@@###@@#@#@@#@@@#@@  13
@@#@@@@@@@@@@@@@@@#@#@@##@#@@####@@@@@@#####@@#@@  12
#@@@#@#@@@@@@##@@##@@#@##@@@#@@#@#@@@@##@#@#@@#@@  11
@@@@#@##@##@#@@@@@@@@@##@##@@@@#@#@@@@@@@#@@@@@@@  10
@#@@##@@@@##@@@###@@@#@#@@#@@#@#@@#@@@####@##@##@   9 **
@@#####@@@@@@@@@@@@@@@@#@#@#@@@@@##@@##@@@#@@#@@#   8 **
@@#@#@@@@@#@#@@@@@@@@@@@@@@@@@@@@@@@@####@#####@#   7 **
#@@@@@@@@@@@.~~.@#@#@@@..#@@@@@#@#@#@@@#@@@@@@#@#   6 **
@@@@#@##@@@@@.~~.@@./\.'@@#@@@@@@@#@@@@@@@@#@@@@@   5 **
@@###@@#@@@.' ~  './\'./\' .#@@#@@@@@#@@@@@#@#@#@   4 **
@@@#@@@#@_/ ~   ~  \ ' '. '.'.@@@#@@@@#@@@@@##@@@   3 **
-~------'    ~    ~ '--~-----~-~----___________--   2 **
  ~    ~  ~      ~     ~ ~   ~     ~  ~  ~   ~      1 **
```

## Solutions

My solutions for each day's puzzles reside in their own directory. Each
directory follows the same pattern. Consider:

```sh
$ tree day01
day01
├── input_practice.txt
├── input.txt
├── part1.py
├── part2.py
├── README.md
├── solutions.md
├── test_solutions.py
└── utils.py
```

### `input_practice.txt` & `input.txt`

These files contain the practice and full puzzle input, respectively. The
practice puzzle input is invaluable in solving each day's puzzle, as it
provides an input which is easier to reason about than the full puzzle input,
and is accompanied by a known solution.

### `part1.py` & `part2.py`

These files contain the solutions to each part of the puzzle. The
[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) `#! /usr/bin/env
python3` specified at the top of each file instructs the program loader to use
the Python environment _active in the current session_ to run the scripts. Each
program can then be run from the command line simply as, say, `$ ./part1.py`.

### `README.md`

This file contains the statement of the puzzle, as taken from the Advent of
Code website.

### `solutions.md`

This file contains some details about my general approach to each puzzle. It
also describes some of the other approaches I considered, and either discarded
initially, or abandoned after later discovering shortcomings to the approach.

### `utils.py`

The `utils` module is used to capture any functionality which is common to both
the `part1` and `part2` solutions. This logic can then be loaded from within
the solution scripts as eg. `from utils import load_input`.

Sometimes the only common functionality between solution scripts is that of
the data loading, but in other cases there may be more common logic.

### `test_solutions.py`

This file can be used by [`pytest`](https://docs.pytest.org/en/7.2.x/) to check
the solutions to the puzzles. This is useful when one has solved a puzzle, but
wishes to then refactor, reformulate, or
[optimise](https://wiki.c2.com/?PrematureOptimization) the puzzle's solution.

Solutions can either be tested on a day-by-day basis as, eg.
```sh
/home/aoc/day01/ $ pytest .
```
or for _all_ puzzle solutions as:
```sh
/home/aoc $ make test
```

## Requirements

As I use [Python's walrus
operator](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions)
in a few of the puzzle's solutions, these solutions require Python version >=
3.8.

The packages required for all the solutions are captured within a
[`requirements.txt`](./requirements.txt). Running `make` will create a virtual
environment, activate it, and install the packages listed in `requirements.txt`.
