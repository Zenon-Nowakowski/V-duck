import difflib
import json
import string

def FilterAlgorithm(message, user):
    print("hit the alg :D")
    with open("config/config.json") as jsonFile:
        d = json.load(jsonFile)
        data = d["FilteredStrings"]
    print("the data is: " + ''.join(data))
    for word in message.split():
        difference = difflib.get_close_matches(word, data, n=1, cutoff=0.8)
        if difference == []:
            continue
        elif difference is not None:
            print(f"{word}, used by {user} is closest to {difference} in the json file.")
            return True
    return False