from utils.read_file import get_file_lines


def assignments_where_one_range_is_fully_contained_by_the_other() -> int:
    total_assignments = 0
    lines = get_file_lines("./day4/day4_input.txt")
    for line in lines:
        first_assignment, second_assignment = line.strip().split(",")
        first_section, second_section = first_assignment.split("-"), second_assignment.split("-")
        if int(first_section[0]) <= int(second_section[0]) and int(first_section[1]) >= int(second_section[1]):
            total_assignments += 1
        elif int(second_section[0]) <= int(first_section[0]) and int(second_section[1]) >= int(first_section[1]):
            total_assignments += 1
    return total_assignments


def assignments_where_there_is_overlap() -> int:
    total_assignments = 0
    lines = get_file_lines("./day4/day4_input.txt")
    for line in lines:
        first_assignment, second_assignment = line.strip().split(",")
        first_section, second_section = first_assignment.split("-"), second_assignment.split("-")
        aa, ab, ba, bb = int(first_section[0]), int(first_section[1]), int(second_section[0]), int(second_section[1])
        if aa <= ba and ab >= ba:
            total_assignments += 1
            continue
        if aa >= ba and aa <= bb:
            total_assignments += 1
            continue
        if aa <= ba and ab >= bb:
            total_assignments += 1
            continue
        if ba <= aa and bb >= aa:
            total_assignments += 1
            continue
        if ba >= aa and ba <= ab:
            total_assignments += 1
            continue
        if ba <= aa and bb >= ab:
            total_assignments += 1
            continue
    return total_assignments
