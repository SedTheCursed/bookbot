def main(book):
    with open(book) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        char_map = count_char(file_contents)
        print_report(book, words, char_map)


def count_words(file):
    return len(file.split())


def count_char(file):
    chars = {}
    for char in file.lower():
        if not char.isalpha(): continue

        if char not in chars:
            chars[char] = 0

        chars[char] += 1

    chars_list = chars.items()

    return sorted(chars_list)


def print_report(book, words, char_map):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()

    for (k, v) in char_map:
        print(f"The '{k}' character was found {v} times")

    print("--- End report ---")


main(book = "books/frankenstein.txt")