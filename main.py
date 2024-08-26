def main():

    bookpath = "books/frankenstein.txt"
    book_contents = get_book_text(bookpath)
    book_words_list = book_contents.split()
    book_wordcount = get_wordcount(book_contents)
    character_dict = get_character_count(book_contents)
    sorted_character_list = sorted_list_ify(character_dict)
    
    print(f"--- Begin report of {bookpath} ---")
    print(f"{book_wordcount} words found in the document")

    for character in sorted_character_list:
        if not character["num"].isalpha():
            continue
        print(f"The '{character['num']}' character was found {character['count']} times")

    print(f"---End of Report ---")

    

def get_wordcount(contents):
    words = contents.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_character_count(contents):
    standardized = contents.lower()
    characters = {}

    if contents == '':
        return characters
    for character in standardized:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1

    return characters

def sort_on(dict):
    return dict["count"]

def sorted_list_ify(character_dict):
    
    character_list = []

    for entry in character_dict:
        new_dict = {}
        new_dict["num"] = entry
        new_dict["count"] = character_dict[entry]
        character_list.append(new_dict)

    character_list.sort(reverse=True, key=sort_on)

    return character_list

    
    




    

    # with open("books/frankenstein.txt") as f:
    #     file_contents = f.read()
    #     print(file_contents)
    #     words = file_contents.split()
    #     wordcount = 0
    #     for i in words:
    #         wordcount = wordcount + 1

    #     print(wordcount)



main()
