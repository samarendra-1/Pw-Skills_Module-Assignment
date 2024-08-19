# employees.py

def write_employee_details(file_path: str, employees: list) -> None:
    """
    Writes the details of employees to the given file.
    
    Parameters:
    file_path (str): The path to the file to be written.
    employees (list): A list of dictionaries containing employee details.
                      Each dictionary should have keys: 'name', 'age', 'salary'.
    """
    with open(file_path, 'w') as file:
        for employee in employees:
            file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: ${employee['salary']}\n")

# Example usage
employees = [
    {'name': 'John Doe', 'age': 30, 'salary': 50000},
    {'name': 'Jane Smith', 'age': 25, 'salary': 60000},
    {'name': 'Emily Johnson', 'age': 35, 'salary': 70000},
]

file_path = 'employees.txt'
write_employee_details(file_path, employees)

print(f"Employee details have been written to {file_path}")
