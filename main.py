from stats import word_counter
from stats import sorted_char_report
import sys

def get_book_text(filepath):
    content = None
    with open(filepath) as file:
        content = file.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    book_content = get_book_text(path)
    print("----------- Word Count ----------")
    word_count = word_counter(book_content)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count_list = sorted_char_report(book_content)
    for char_count_dict in char_count_list:
        char = char_count_dict['char']
        num = char_count_dict['num']
        if char.isalpha():
            print(f"{char_count_dict['char']}: {char_count_dict['num']}")
    print("============= END ===============")

main()
