
def get_book_text(file_path):
   with open("./books/frankenstein.txt") as file:
       return file.read()
   
def count_words(text):
    words = text.split()
    return f"{len(words)} words found in the document"
   
def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    print(word_count)

main()

