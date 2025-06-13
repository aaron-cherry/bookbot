def count_words(text):
    words = text.split()
    count_chars(words)
    return f"{len(words)} words found in the document"

def count_chars(words):
    char_list = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in char_list:
                char_list[letter] += 1
            else:
                char_list[letter] = 1
    print(char_list)

