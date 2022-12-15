## Solutions

A nice easy puzzle to kick this year's advent of code off.

The data is easy to parse. I strip the newline characters (`\n`) from each line
with the `.strip()` string method.

In both parts of the puzzle, I use the ["truthiness" of non-empty strings](
https://docs.python.org/3/library/stdtypes.html#truth-value-testing) (`if
calorie`) to separate the calorie counts of each individual elf.

### Part 1

Although tempting, it is unnecessary _and_ inefficient to compute and _store_
the calorie total of each elf. Instead, it is more efficient to simply compute
a single "running total" (`running_total`), which is updated if an elf's
calorie count (`current_total`) exceeds this value.

### Part 2

To solve part two, rather than having the running total be a single integer,
the running total is stored as a list of length three. An elf's calorie count
makes the top three if it is greater than the minimum value of this list (`if
current_total > min(running_total)`)

The smallest calorie count is then discarded from the list, with the new value
inserted (`running_total[0] = current_total`). This is possible by ensuring
that the running total list is always sorted from smallest to largest
(`running_total.sort()`).
