import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def find(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        new_word = get_close_matches(word, data.keys())[0]
        user_response = input("Did you mean %s instead? Y for 'YES' or N for 'No': " % new_word)
        if user_response == 'y' or user_response == 'Y':
            return data[new_word]
        else:
            return "The word doesnot exist!"
    else:
        return "The word doesnot exist!"


word = input("Enter a word to search: ")
words = find(word)

if type(words) == list:
    for w in words:
        print(w)
else:
    print(words)

