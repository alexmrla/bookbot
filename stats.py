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

def sort_on(items):
    return items["num"]


def sort_chars(count_chars):
    split_counts = []
    for char in count_chars:
        if char.isalpha():
            split_counts.append({"char": char, "num": count_chars[char]})
    #print(f"Split Counts: {split_counts}")
    split_counts.sort(reverse=True, key=sort_on)
    return split_counts
