PICK_TO_SHAPE_MAPPER = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

SHAPE_POINTS = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}


def strategy_guide_total_points() -> int:
    total_points = 0
    with open("./day2/day2_input.txt", encoding='utf-8') as strategy_guide:
        lines = strategy_guide.readlines()
        for line in lines:
            round = line.strip().split(" ")
            opponent_pick, player_pick = PICK_TO_SHAPE_MAPPER[round[0]], PICK_TO_SHAPE_MAPPER[round[1]]
            total_points += _get_round_points(opponent_pick, player_pick)
    return total_points


def _get_round_points(opponent_pick: str, player_pick: str) -> int:
    player_points = SHAPE_POINTS[player_pick]
    if opponent_pick == player_pick:
        player_points += 3
    elif _defeats(player_pick, opponent_pick):
        player_points += 6
    return player_points


def _defeats(player_pick: str, opponent_pick: str) -> bool:
    if player_pick == "ROCK":
        return opponent_pick == "SCISSORS"
    if player_pick == "PAPER":
        return opponent_pick == "ROCK"
    if player_pick == "SCISSORS":
        return opponent_pick == "PAPER"
    return False
