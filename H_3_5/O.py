import json

with open("scoring.json") as test:
    data = json.load(test)

points = 0

for dictionary in data:
    for dct in dictionary["tests"]:
        if dct["pattern"] == input():
            points += int(dictionary["points"]) / len(dictionary["tests"])
print(int(points))
