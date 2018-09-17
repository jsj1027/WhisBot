from pathlib import Path

counter_file_folder = Path("database_files")
potato_count_file = None


def load_potato_count():
    global potato_count_file
    potato_count_path = counter_file_folder / "potato_count.txt"
    potato_count_file = open(potato_count_path)


def get_potato_count():
    return potato_count_file.read()


def update_potato_count():
    global potato_count_file
    current_count = potato_count_file.read()
    updated_count = current_count + 1
    potato_count_file.write(updated_count)
