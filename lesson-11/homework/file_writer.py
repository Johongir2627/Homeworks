def write_file(file_path, content):
    """Write content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)