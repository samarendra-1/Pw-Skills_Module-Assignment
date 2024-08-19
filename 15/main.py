# main.py
import file_operations

# Example file path
file_path = 'example.txt'

# Writing data to a file
file_operations.write_file(file_path, 'Hello, world!\n')

# Appending data to a file
file_operations.append_to_file(file_path, 'This is an appended line.\n')

# Reading data from a file
content = file_operations.read_file(file_path)
print("File content:")
print(content)
