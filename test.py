import json 
import random 
with open("copypasta.json") as jsonFile:
    mega = json.load(jsonFile)
    data = mega["copyastas"]
    pasta = random.choice(data)
    message = f"# {(pasta)['name']}\n{(pasta)['text']}"
print(message)