
import json
from pprint import pprint


# Open a json file and append entries to the file.
f = open("allanswers.json", "r")
data = json.load(f)
print(type(data))
print(data)
f.close()

# TODO: Your code below! Analyze something interesting about your data :)
count = 0
oppcount = 0
for s in data:
    if s["age"] == "17":
        count += 1
    else:
        oppcount += 1
print("Number of 17 year olds:" + str(count))
print("Number of people other ages:" + str(oppcount))
