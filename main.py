def count_letters(text):
    letter_counts = {}
    lowered_text = text.lower()

    for letter in lowered_text:
        if letter == " ":
            pass
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def sort_on(dict):
    return dict["num"]

def dict_to_list_of_dicts(dict):
    list_of_dicts = []
    for key in dict:
        if key.isalpha():
            d = {"letter": key, "num": dict[key]}
            list_of_dicts.append(d)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def build_report(dict_list, file, word_count):
    print(f"--- Begin report of {file} ---")
    print(f"{word_count} words found in the document\n")
    # print("\n")
    for d in dict_list:
        print(f"The '{d["letter"]}' character was found {d["num"]} times")
    print("--- End Report ---")

def count_words(text):
    words = text.split()
    return len(words)

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)
        list_of_dicts = dict_to_list_of_dicts(letter_count)
        build_report(list_of_dicts, path, word_count)
        


main()
    