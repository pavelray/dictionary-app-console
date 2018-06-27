import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w.lower() in data:
        return data[w]
    elif w.upper() in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        matched_word = get_close_matches(w,data.keys())[0]
        yn = input(f"Did you mean {matched_word} instead of {w}? Enter Y for yes and N for no ")
        if yn.lower() == 'y':
            return data[matched_word]
        elif yn.lower() =='n':
            return "Word does not exsists in the dictionary"
        else:
            return "Please enter Y for yes or N for no"
    else:
        return "No matching word found"

word = input("Enter search word: ")
result = translate(word)

if type(result) == list:
    for r in result:
        print(r)
else:
    print(result)
