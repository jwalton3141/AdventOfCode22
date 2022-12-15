## Solutions

I particularly enjoyed this problem, and felt pleased with my solution.

Although the puzzle can be solved _without_ "decoding" the plays, the resulting
solution is more difficult to understand and leads to more obfuscated code.

### Part 1

Scoring the shapes played in part one is easy, whereas scoring outcomes takes a
little more work. I used a dictionary `shape_to_beat` to code which plays beat
which. This made it easy to compute the outcome of each game:

```py
shape_to_beat = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

score = 0
for their_play, our_play in zip(their_plays, our_plays):
    if our_play == their_play:
        score += 3
    elif our_play == shape_to_beat[their_play]:
        score += 6
```

### Part 2

The twist of the interpretation of the input between part one and part two was
fun and unexpected. In this part the outcomes are easy to score, but the shapes
played more difficult. Again I made use of the `shape_to_beat` dictionary,
noting that the shape to play to _lose_ can be computed by applying the
`shape_to_beat` dictionary twice. Neat!

```py
shape_to_beat = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
shape_scorecard = {"rock": 1, "paper": 2, "scissors": 3}

score = 0
for their_play, outcome in zip(their_plays, outcomes):
    if outcome == "draw":
        shape_to_play = their_play
    elif outcome == "win":
        shape_to_play = shape_to_beat[their_play]
    else:
        shape_to_play = shape_to_beat[shape_to_beat[their_play]]

    score += shape_scorecard[shape_to_play]
```
