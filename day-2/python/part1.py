from enum import Enum
from typing import Tuple


class ActionPoints(Enum):
    SCISSORS = (3,)
    PAPER = (2,)
    ROCK = (1,)


class ResultsScore(Enum):
    WIN = (6,)
    DRAW = (3,)
    LOSS = (0,)


def decrypt_concurrent_action(letter: str) -> ActionPoints:
    match letter:
        case "A":
            return ActionPoints.ROCK
        case "B":
            return ActionPoints.PAPER

    return ActionPoints.SCISSORS


def decrypt_our_action(letter: str) -> ActionPoints:
    match letter:
        case "X":
            return ActionPoints.ROCK
        case "Y":
            return ActionPoints.PAPER

    return ActionPoints.SCISSORS


def score_of_the_round(concurrent: ActionPoints, our_action: ActionPoints) -> int:
    did_we_win: bool = bool(
        (concurrent == ActionPoints.SCISSORS and our_action == ActionPoints.ROCK)
        | (concurrent == ActionPoints.ROCK and our_action == ActionPoints.PAPER)
        | (concurrent == ActionPoints.PAPER and our_action == ActionPoints.SCISSORS)
    )
    return (
        int(ResultsScore.WIN.value[0]) + int(our_action.value[0])
        if did_we_win
        else int(ResultsScore.DRAW.value[0]) + int(our_action.value[0])
        if our_action == concurrent
        else int(ResultsScore.LOSS.value[0]) + int(our_action.value[0])
    )


def parse(input: list[str]) -> list[Tuple[ActionPoints, ActionPoints]]:
    rounds: list[Tuple[ActionPoints, ActionPoints]] = []
    for line in input:
        concurrent_action = decrypt_concurrent_action(line[0])
        our_action = decrypt_our_action(line[2])
        rounds.append((concurrent_action, our_action))
    return rounds


def how_many_points_will_we_get(rounds: list[Tuple[ActionPoints, ActionPoints]]) -> int:
    return sum(score_of_the_round(round[0], round[1]) for round in rounds)


with open("./data.txt", "r", encoding="utf8") as file:
    rounds = parse([line.rstrip("\n") for line in file])

print(how_many_points_will_we_get(rounds))
