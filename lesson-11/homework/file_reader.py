def read_file(file_path):
    """Read the content of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."