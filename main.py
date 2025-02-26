from stats import count_words
from stats import character_count
from stats import report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    char_counts = character_count(book_text)
    sorted_chars = report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

main()