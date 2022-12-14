from day1.day1 import get_max_calories_carried_by_elf
from day2.day2 import strategy_guide_total_points
from day2.day2_part2 import strategy_guide_total_points as strategy_guide_total_points_part2
from day3.day3 import sum_priorities_of_repeated_items
from day4.day4 import assignments_where_one_range_is_fully_contained_by_the_other, assignments_where_there_is_overlap


def execute_days():
    day1_answer = get_max_calories_carried_by_elf()
    print(f"Day 1: {day1_answer}")
    day2_answer = strategy_guide_total_points()
    print(f"Day 2: {day2_answer}")
    day2_part2_answer = strategy_guide_total_points_part2()
    print(f"Day 2 part 2: {day2_part2_answer}")
    day3_answer = sum_priorities_of_repeated_items()
    print(f"Day 3: {day3_answer}")
    day4_answer = assignments_where_one_range_is_fully_contained_by_the_other()
    print(f"Day 4: {day4_answer}")
    day4_part2_answer = assignments_where_there_is_overlap()
    print(f"Day 4 part 2: {day4_part2_answer}")


if __name__ == '__main__':
    execute_days()
