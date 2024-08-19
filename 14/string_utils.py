# string_utils.py

def reverse_string(s: str) -> str:
    """
    Reverses the given string.
    
    Parameters:
    s (str): The string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]

def capitalize_string(s: str) -> str:
    """
    Capitalizes the first letter of each word in the given string.
    
    Parameters:
    s (str): The string to be capitalized.
    
    Returns:
    str: The string with the first letter of each word capitalized.
    """
    return s.title()

def uppercase_string(s: str) -> str:
    """
    Converts all characters of the given string to uppercase.
    
    Parameters:
    s (str): The string to be converted to uppercase.
    
    Returns:
    str: The string with all characters in uppercase.
    """
    return s.upper()

def lowercase_string(s: str) -> str:
    """
    Converts all characters of the given string to lowercase.
    
    Parameters:
    s (str): The string to be converted to lowercase.
    
    Returns:
    str: The string with all characters in lowercase.
    """
    return s.lower()

def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.
    
    Parameters:
    s (str): The string to be checked.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

def count_vowels(s: str) -> int:
    """
    Counts the number of vowels in the given string.
    
    Parameters:
    s (str): The string in which vowels are to be counted.
    
    Returns:
    int: The number of vowels in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
