import os

def num_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the occurrences of each character in the text."""
    char_count = {}  # Dictionary to store character frequencies
    for char in text.lower():  # Convert text to lowercase to avoid duplicates
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count  # Return dictionary of character counts

def sort_characters_by_count(char_dict):
    """Takes a character count dictionary and returns a sorted list of dictionaries."""
    sorted_list = sorted(
        [{"char": char, "count": count} for char, count in char_dict.items() if char.isalpha()], 
        key=lambda x: x["count"], 
        reverse=True
    )
    return sorted_list
