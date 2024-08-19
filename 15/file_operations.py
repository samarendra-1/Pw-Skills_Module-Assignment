# file_operations.py

def read_file(file_path: str) -> str:
    """
    Reads the content of the given file.
    
    Parameters:
    file_path (str): The path to the file to be read.
    
    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path: str, data: str) -> None:
    """
    Writes data to the given file. Overwrites the file if it already exists.
    
    Parameters:
    file_path (str): The path to the file to be written.
    data (str): The data to be written to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)

def append_to_file(file_path: str, data: str) -> None:
    """
    Appends data to the given file. Creates the file if it does not exist.
    
    Parameters:
    file_path (str): The path to the file to be appended to.
    data (str): The data to be appended to the file.
    """
    with open(file_path, 'a') as file:
        file.write(data)
