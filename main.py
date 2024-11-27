def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)    
    
    test(book_path, num_words, chars_dict)


def test(book_path, num_words, chars_dict):
    try:
        print_report(num_words, chars_dict, book_path)
    except Exception as e:
        print(e)


def print_report(num_words, char_dict, filepath):
    alphabet = "abcdefghiklmnopqrstuvwxyz"

    print(f"--- Begin report of {filepath} ---")
    print(f"{num_words} words found in the document")

    for letter in alphabet:
        print(f"The '{letter}' character was found {char_dict[letter]} times")
    
    print(f"--- End report ---")


def get_char_count(text):
    if not isinstance(text, str):
        raise Exception("not a string")
    else:    
        #new_text = lower_text(text)
        chars = {}
        for c in text:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
        return chars


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
