from day1.day1 import get_max_calories_carried_by_elf
from day2.day2 import strategy_guide_total_points
from day2.day2_part2 import strategy_guide_total_points as strategy_guide_total_points_part2


def execute_days():
    day1_answer = get_max_calories_carried_by_elf()
    print(f"Day 1: {day1_answer}")
    day2_answer = strategy_guide_total_points()
    print(f"Day 2: {day2_answer}")
    day2_part2_answer = strategy_guide_total_points_part2()
    print(f"Day 2 part 2: {day2_part2_answer}")


if __name__ == '__main__':
    execute_days()