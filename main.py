from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return (f.read())

def main():
    # TODO: add filepath
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
    wc = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_chars = sort_char_count(char_count)
    # TODO: add filepath
    print("============ BOOKBOT ============\n"
          f"Analyzing book found at {sys.argv[1]}\n"
          "----------- Word Count ----------\n"
          f"Found {wc} total words\n"
          "--------- Character Count -------")
    # print(f"{wc} words found in the document")
    for item in sorted_chars:
        print(f"{item["char"]}: {item["num"]}")

main()