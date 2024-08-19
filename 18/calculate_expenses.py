# calculate_expenses.py

def calculate_total_expenses(file_path: str) -> float:
    """
    Reads the expenses from the given file and calculates the total amount spent.
    
    Parameters:
    file_path (str): The path to the file to be read.
    
    Returns:
    float: The total amount spent on expenses.
    """
    total_expenses = 0.0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    description, amount = line.strip().split(',')
                    total_expenses += float(amount)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return total_expenses

# Example usage
file_path = 'expenses.txt'
total = calculate_total_expenses(file_path)
print(f"Total amount spent: ${total:.2f}")
