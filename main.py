def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)    
    print(chars_dict)


def test(string):
    try:
        print(get_char_count(string))
    except Exception as e:
        print(e)


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
