from io import TextIOWrapper
from typing import Iterable


def parse(splited_input: list[str]) -> list[int | None]:
    parsed_list: list[int | None] = []
    for line in splited_input:
        parsed_list.append(None if line == "" else int(line))
    return parsed_list


def find_most_calories(calories_list: list[int | None]) -> int:
    elfs_calories: list[int] = [0]
    tracker_index: int = 0
    for cals in calories_list:
        if cals is not None:
            elfs_calories[tracker_index] += cals
        else:
            tracker_index += 1
            elfs_calories.append(0)
    return max(elfs_calories)


def find_top_three_calories(calories_list: list[int | None]) -> list[int]:
    elfs_calories: list[int] = [0]
    tracker_index: int = 0
    for cals in calories_list:
        if cals is not None:
            elfs_calories[tracker_index] += cals
        else:
            tracker_index += 1
            elfs_calories.append(0)
    return sorted(elfs_calories, reverse=True)[:3]


with open("./data.txt", "r", encoding="utf8") as file:
    calories = parse([line.rstrip("\n") for line in file])

# print(find_most_calories(calories))
print(sum(find_top_three_calories(calories)))
