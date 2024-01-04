def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_words_num(text)
    chars_dict = get_chars_dict(text)
    letters_count = chars_dict_to_letters_count(chars_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for i in range(0, len(letters_count)):
        print (f"The '{letters_count[i][1]}' character was found {letters_count[i][0]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as text:
        return text.read()
    
    
def get_words_num(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    dict = {}
    for c in text:
        char = c.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def chars_dict_to_letters_count(dict):
    count_list = []
    for char in dict:
        if char.isalpha():
            count_list.append((dict[char], char))
    count_list.sort(reverse = True)
    return count_list


main()