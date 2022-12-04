from utils.read_file import get_file_lines


def _letter_to_value(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26


def sum_priorities_of_repeated_items() -> int:
    total_sum = 0
    lines = get_file_lines("./day3/day3_input.txt")
    for line in lines:
        first_compartment, second_compartment = line.strip()[:len(line) // 2], line.strip()[(len(line) // 2):]
        total_sum += _get_rucksack_value(first_compartment, second_compartment)
    return total_sum


def _get_rucksack_value(first_compartment: str, second_compartment: str) -> int:
    total_rucksack_value = 0
    for first_compartment_item in first_compartment:
        if first_compartment_item in second_compartment:
            total_rucksack_value += _letter_to_value(first_compartment_item)
            break
    return total_rucksack_value

