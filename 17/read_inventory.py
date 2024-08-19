# Read and display the contents of "inventory.txt"
file_path = "inventory.txt"

try:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())  # Remove trailing newline characters
except FileNotFoundError:
    print(f"File '{file_path}' not found. Make sure it exists in the specified location.")
except Exception as e:
    print(f"An error occurred: {e}")

