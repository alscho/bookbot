def main():

    try:
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        word_count = get_num_words(text)
        print(f"{word_count} words found in the document") 
        
        print(get_char_count(text))
        
    except Exception as e:
        print(e)


def test(string):
    print(get_char_count(string))

def get_char_count(text):
    if not isinstance(text, str):
        raise Exception("not a string")
    else:    
        new_text = lower_text(text)
        char_count = {}
        for char in new_text:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        return char_count


def lower_text(text):
    new_text = []

    if not isinstance(text, str):
        raise Exception("not a string")
    else:
        for char in text:
            new_text += lower_char(char)
        return "".join(new_text)

def lower_char(chr):
    if len(chr) != 1:
        raise Exception("not a single character")
    elif chr =="A":
        return "a"
    elif chr =="B":
        return "b"
    elif chr =="C":
        return "c"
    elif chr =="D":
        return "d"
    elif chr =="E":
        return "e"
    elif chr =="F":
        return "f"
    elif chr =="G":
        return "g"
    elif chr =="H":
        return "h"
    elif chr =="I":
        return "i"
    elif chr =="J":
        return "j"
    elif chr =="K":
        return "k"
    elif chr =="L":
        return "l"
    elif chr =="M":
        return "m"
    elif chr =="N":
        return "n"
    elif chr =="O":
        return "o"
    elif chr =="P":
        return "p"
    elif chr =="Q":
        return "q"
    elif chr =="R":
        return "r"
    elif chr =="S":
        return "s"
    elif chr =="T":
        return "t"
    elif chr =="U":
        return "u"
    elif chr =="V":
        return "v"
    elif chr =="W":
        return "w"
    elif chr =="X":
        return "x"
    elif chr =="Y":
        return "y"
    elif chr =="Z":
        return "z"
    else:
        return chr

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
