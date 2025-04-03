import sys
import os
from stats import num_words, count_characters, sort_characters_by_count

if len(sys.argv) == 2:
    print(f"Argument provided: {sys.argv[1]}")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(filepath):
    """Reads a text file and returns its contents as a string."""
    with open(filepath) as file:
        return file.read()

def main():
    """Reads frankenstein.txt, prints word count and character frequency."""
    book_text = get_book_text(path_to_book)  # Read the file
    word_count = num_words(book_text)  # Count words
    char_count = count_characters(book_text)  # Count characters
    sorted_chars = sort_characters_by_count(char_count)  # Sort character count
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
#    print("Character Frequency:")
#    for char, count in sorted(char_count.items()):  # Sort characters alphabetically
#       print(f"'{char}': {count}")
#    print(sorting_list)
#    print("Character Frequency (sorted, alphabetical only):")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
