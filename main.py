from stats import get_num_words, get_char_count, sort_chars

def get_book_text():
    with open('./books/frankenstein.txt') as f:
        convert_to_string = f.read()
    return convert_to_string

def main():
    string = get_book_text()
    total_words = get_num_words(string)
    count_chars = get_char_count(string)
    char_sort = sort_chars(count_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for item in char_sort:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()
