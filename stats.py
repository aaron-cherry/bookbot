def count_words(text):
    words = text.split()
    return f"----- Word Count -----\nFound {len(words)} total words", words

def count_chars(words):
    char_dict = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def print_report(char_dict):
    dict_list = []
    for char in char_dict:
        dict_list.append({"char": char, "num": char_dict[char]})
    
    dict_list.sort(reverse=True, key=sort_on)
    for c in dict_list:
        if c["char"].isalpha() != True:
            continue
        print(f"{c["char"]}: {c["num"]}")
    #print(dict_list)
            