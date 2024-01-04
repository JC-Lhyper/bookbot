def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_words_num(text)
    print(f"There is {num_words} words in this book")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    
def get_words_num(text):
    words = text.split()
    return len(words)




main()