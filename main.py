from stats import count_words
from stats import count_chars
from stats import print_report

def get_book_text(file_path):
   with open("./books/frankenstein.txt") as file:
       print(f"Analyzing book found at {file_path}...")
       return file.read()

def main():
    print("====== BOOKBOT =====")
    book_text = get_book_text("./books/frankenstein.txt")
    word_count, words = count_words(book_text)
    print(word_count)
    print("----- Character Count ------")
    char_dict = count_chars(words)
    print_report(char_dict)

main()
