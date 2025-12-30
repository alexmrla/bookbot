from stats import get_num_words, get_char_count, sort_chars
import sys


def get_book_text(input_path):
    with open(input_path) as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    string = get_book_text(input_path)
    total_words = get_num_words(string)
    count_chars = get_char_count(string)
    char_sort = sort_chars(count_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for item in char_sort:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()
