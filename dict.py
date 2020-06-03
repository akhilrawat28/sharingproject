import json    #forthedatabase
from difflib import get_close_matches 

data =  json.load(open("original.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes and n for no")
        if decide == "y":
                return data[get_close_matches(word , data.keys())[0]]
        elif decide ==n :
            return("word not found")
        else :
            retun("not found")
    else:
        print("word not found")

word = input("ENTER THE WORD YOU WANT TO SEARCH")
output = translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
