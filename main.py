import sys
from stats import count_words
from stats import count_char
from stats import sort_count_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    num_word = count_words(book_text)
    char_counts = count_char(book_text)
    sorted_chars = sort_count_char(char_counts)

    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}")
    print ("----------- Word Count ----------")
    print (f"Found {num_word} total words")
    print ("--------- Character Count -------")
    for item in sorted_chars:
        print (f"{item['char']}: {item['num']}")
    print ("============= END ===============")

main()
