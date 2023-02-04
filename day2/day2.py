import pathlib
import os

parent_dir = pathlib.Path(__file__).parent.resolve()
f = open(os.path.join(parent_dir, "day2_input.txt"), "r")

SHAPE_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

OUTCOME_SCORE = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0
}

DESIRED_OUTCOME = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN"
}


def play(opp_move, my_move):
    round_score = 0
    # This is gross
    if opp_move == "A":  # ROCK
        if my_move == "X":
            round_score = SHAPE_SCORE["X"] + OUTCOME_SCORE["DRAW"]
        elif my_move == "Y":
            round_score = SHAPE_SCORE["Y"] + OUTCOME_SCORE["WIN"]
        elif my_move == "Z":
            round_score = SHAPE_SCORE["Z"] + OUTCOME_SCORE["LOSE"]
    elif opp_move == "B":  # PAPER
        if my_move == "X":
            round_score = SHAPE_SCORE["X"] + OUTCOME_SCORE["LOSE"]
        elif my_move == "Y":
            round_score = SHAPE_SCORE["Y"] + OUTCOME_SCORE["DRAW"]
        elif my_move == "Z":
            round_score = SHAPE_SCORE["Z"] + OUTCOME_SCORE["WIN"]
    elif opp_move == "C":  # SCISSORS
        if my_move == "X":
            round_score = SHAPE_SCORE["X"] + OUTCOME_SCORE["WIN"]
        elif my_move == "Y":
            round_score = SHAPE_SCORE["Y"] + OUTCOME_SCORE["LOSE"]
        elif my_move == "Z":
            round_score = SHAPE_SCORE["Z"] + OUTCOME_SCORE["DRAW"]

    return int(round_score)


def find_my_move(opp_move, outcome_code):
    outcome = DESIRED_OUTCOME[outcome_code]

    if opp_move == "A":  # ROCK
        if outcome == "WIN":
            return "Y"
        elif outcome == "DRAW":
            return "X"
        elif outcome == "LOSE":
            return "Z"
    elif opp_move == "B":  # PAPER
        if outcome == "WIN":
            return "Z"
        elif outcome == "DRAW":
            return "Y"
        elif outcome == "LOSE":
            return "X"
    elif opp_move == "C":  # SCISSORS
        if outcome == "WIN":
            return "X"
        elif outcome == "DRAW":
            return "Z"
        elif outcome == "LOSE":
            return "Y"
    else:
        raise ValueError(f"unknown move: {opp_move}")


score = 0
for line in f.read().splitlines():
    moves = line.split(" ")
    if len(moves) != 2:
        raise ValueError("Error parsing moves")
    opp_move = moves[0]
    # my_move = moves[1]
    # part 2
    my_move = find_my_move(opp_move, moves[1])
    score += play(opp_move, my_move)

print(f"Total score: {score}")

