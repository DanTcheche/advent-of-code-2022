def get_max_calories_carried_by_elf() -> int:
    current_elf_calories = 0
    all_elf_calories = []
    with open("./day1/day1_input.txt", encoding = 'utf-8') as calories_per_elf_file:
        lines = calories_per_elf_file.readlines()
        for line in lines:
            if line.strip():
                current_elf_calories += int(line)
            else:
                all_elf_calories.append(current_elf_calories)
                current_elf_calories = 0
    return sum(sorted(all_elf_calories, reverse=True)[:3])
