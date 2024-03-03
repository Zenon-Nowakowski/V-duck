import difflib
import json
import string

def filtering_algorithm(message, user):
    with open("internal.json") as jsonFile:
        d = json.load(jsonFile)
        data = d["filtered_strings"]
    for word in message.split():
        difference = difflib.get_close_matches(word, data, n=1, cutoff=0.5)
        if difference == []:
            continue
        elif difference is not None:
            print(f"{word}, used by {user} is closest to {difference} in the json file.")
            return True
    return False