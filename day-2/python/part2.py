from typing import Tuple

from part1 import (
    ActionPoints,
    ResultsScore,
    decrypt_concurrent_action,
    score_of_the_round,
)


def defined_action(letter: str) -> ResultsScore:
    match letter:
        case "X":
            return ResultsScore.LOSS
        case "Y":
            return ResultsScore.DRAW

    return ResultsScore.WIN


def solve_ending(concurrent_action: ActionPoints, defined_end: ResultsScore) -> int:
    our_action: ActionPoints = ActionPoints.SCISSORS
    match defined_end:
        case ResultsScore.WIN:
            match concurrent_action:
                case ActionPoints.SCISSORS:
                    our_action = ActionPoints.ROCK
                case ActionPoints.ROCK:
                    our_action = ActionPoints.PAPER
        case ResultsScore.LOSS:
            match concurrent_action:
                case ActionPoints.SCISSORS:
                    our_action = ActionPoints.PAPER
                case ActionPoints.PAPER:
                    our_action = ActionPoints.ROCK
        case ResultsScore.DRAW:
            our_action = concurrent_action
    return score_of_the_round(concurrent_action, our_action)


def parse(input: list[str]) -> list[Tuple[ActionPoints, ResultsScore]]:
    rounds: list[Tuple[ActionPoints, ResultsScore]] = []
    for line in input:
        concurrent_action = decrypt_concurrent_action(line[0])
        our_action = defined_action(line[2])
        rounds.append((concurrent_action, our_action))
    return rounds


def how_many_points_will_we_get(rounds: list[Tuple[ActionPoints, ResultsScore]]) -> int:
    return sum(solve_ending(round[0], round[1]) for round in rounds)


with open("./data.txt", "r", encoding="utf8") as file:
    rounds = parse([line.rstrip("\n") for line in file])

print(how_many_points_will_we_get(rounds))
