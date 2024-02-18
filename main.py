from collections import defaultdict
import os

def count_letters(text):
    lowered_text = text.lower()
    d = defaultdict(int)
    for letter in lowered_text:
        d[letter] += 1
    
    return d

def count_words(text):
    return len(text.split())
    

def create_report(text, filename):
    word_count = count_words(text)
    chars_count = count_letters(file_contents)
    print(f"--- Begin report of {filename} ---\n{word_count} words found in the document\n\n")
    for char in sorted(chars_count, key=chars_count.get, reverse=True):
        if char.isalpha():
            print(f"The `{char}` character was found {chars_count[char]} times")
    print("--- End report ---")

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        create_report(file_contents, f.name)



