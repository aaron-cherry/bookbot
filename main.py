import sys
from stats import count_words
from stats import count_chars
from stats import print_report

def get_book_text(file_path):
   with open(file_path) as file:
       print(f"Analyzing book found at {file_path}...")
       return file.read()

def check_args(arg_list):
    if len(arg_list) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    print("====== BOOKBOT =====")
    check_args(sys.argv)
    book_text = get_book_text(sys.argv[1])
    word_count, words = count_words(book_text)
    print(word_count)
    print("----- Character Count ------")
    char_dict = count_chars(words)
    print_report(char_dict)

main()
