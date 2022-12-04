from enum import Enum

from day2.day2 import PICK_TO_SHAPE_MAPPER, SHAPE_POINTS
from utils.read_file import get_file_lines

PICK_TO_WIN = {
    "ROCK": "PAPER",
    "PAPER": "SCISSORS",
    "SCISSORS": "ROCK"
}

LETTER_TO_RESULT = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

RESULT_TO_POINTS = {
    "WIN": 6,
    "DRAW": 3,
    "LOSE": 0
}


class Results(Enum):
    WIN = "WIN"
    DRAW = "DRAW"
    LOSE = "LOSE"


def needed_pick_to_get_result(pick: str, result: str) -> str:
    if result == Results.WIN.value:
        return PICK_TO_WIN[pick]
    if result == Results.DRAW.value:
        return pick
    if result == Results.LOSE.value:
        return PICK_TO_WIN[PICK_TO_WIN[pick]]


def strategy_guide_total_points() -> int:
    total_points = 0
    lines = get_file_lines("./day2/day2_input.txt")
    for line in lines:
        elements_in_line = line.strip().split(" ")
        opponent_pick, expected_result = PICK_TO_SHAPE_MAPPER[elements_in_line[0]], \
            LETTER_TO_RESULT[elements_in_line[1]]
        total_points += _get_round_points(opponent_pick, expected_result)
    return total_points


def _get_round_points(opponent_pick: str, expected_result: str) -> int:
    player_points = RESULT_TO_POINTS[expected_result]
    player_pick = needed_pick_to_get_result(opponent_pick, expected_result)
    player_points += SHAPE_POINTS[player_pick]
    return player_points
