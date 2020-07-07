import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]    
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("did you mean %s instead? enter Y or N: " % get_close_matches(word, data.keys())[0]).lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "the word does not exist"
        else:
            return "sorry could not understand !"
    else:
        return "the word does not exist"

    

word = input("enter word: ").lower()

defenitions = translate(word)

if type(defenitions) == list:
    for item in defenitions:
        print(item)
else:
    print(defenitions)