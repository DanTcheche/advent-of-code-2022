def get_file_lines(file_path: str) -> list:
    with open(file_path, encoding='utf-8') as file:
        return file.readlines()
