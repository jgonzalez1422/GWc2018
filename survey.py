import json

# TODO Part I: Add your survey questions to this empty list.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your favorite color?",
    "What color are your eyes?",
    "What is your favorite hobby?",
    "What is your favorite meme?",
    "What's your favorite show?"
    ]

# TODO Part I: store the related keys corresponding to the survey answers here.
keys = ["name", "age", "color", "eyes", "hobby", "meme", "show"]

# Create a list that will store each person's individual survey responses.
# Use for Part II.
list_of_answers = [

]

# Creates the dictionary to store responses.

# TODO Part I: write code that asks each survey question and prompts the user for a response.
# Hint: how can you go through each element of a list?
repeat = "yes"
while repeat == "yes":
    answers = {}
    for i in range(len(survey)):
        response = input(survey[i] + " ")
        answers[keys[i]] = response
    list_of_answers.append(answers)
    print(list_of_answers)
    repeat = input("Do you want to repeat the survey?")


# Print the context of the dictionary.
print(answers)

#TODO Part II: Delete the quotes. This will print each individual's survey responses
"""
#Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
names = []
for s in range(len(list_of_answers)):
    names.append(list_of_answers[s]["name"])
print(names)
"""

f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

# Reopen the file in write mode and write each entry in json format.
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if (index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
