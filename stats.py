def get_num_words(string):
    num_words = 0
    for word in string.split():
        num_words += 1
    return num_words

def get_char_count(string):
    char_counter = {}
    for char in string.lower():
        if char not in char_counter:
            char_counter[char] = 1
        else: 
            char_counter[char] += 1
    return char_counter

def sort_chars(count_chars):
    char_counter = count_chars
    # for char in char_counter:
    #     print(char)
