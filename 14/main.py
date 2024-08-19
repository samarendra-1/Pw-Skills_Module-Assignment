# main.py
import string_utils

# Example usage of the string_utils module
sample_string = "hello world"

print("Original string:", sample_string)
print("Reversed string:", string_utils.reverse_string(sample_string))
print("Capitalized string:", string_utils.capitalize_string(sample_string))
print("Uppercase string:", string_utils.uppercase_string(sample_string))
print("Lowercase string:", string_utils.lowercase_string(sample_string))
print("Is palindrome:", string_utils.is_palindrome(sample_string))
print("Number of vowels:", string_utils.count_vowels(sample_string))
