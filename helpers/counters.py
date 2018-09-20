from pathlib import Path

database_folder = Path("database_files")
potato_count_file = database_folder / "potato_count.txt"
#potato_count_file = open(potato_count_file)


def get_potato_count():
    global potato_count_file
    return potato_count_file.read_text()


def update_potato_count():
    current_count = get_potato_count()
    updated_count = int(current_count) + 1
    potato_count_file.write_text(str(updated_count))
