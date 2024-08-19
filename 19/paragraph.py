def read_paragraph(file_path):
    try:
        with open(file_path, "r") as file:
            paragraph = file.read()
            return paragraph
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Make sure it exists in the specified location.")
        return ""

def count_word_occurrences(paragraph):
    word_counts = {}
    words = paragraph.lower().split()  # Convert to lowercase and split by spaces

    for word in words:
        # Remove punctuation (if any)
        word = word.strip(".,!?\"'()[]{}:;-")

        if word:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def display_sorted_counts(word_counts):
    sorted_counts = sorted(word_counts.items(), key=lambda item: item[0])
    for word, count in sorted_counts:
        print(f"{word}: {count}")

if __name__ == "__main__":
    paragraph_file = "paragraph.txt"
    paragraph_text = read_paragraph(paragraph_file)

    if paragraph_text:
        word_occurrences = count_word_occurrences(paragraph_text)
        display_sorted_counts(word_occurrences)
    else:
        print("No valid paragraph found in the file.")
