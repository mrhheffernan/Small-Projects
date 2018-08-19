import json
from difflib import get_close_matches as gcm
data = json.load(open("data.json","r"))

def define(obj):
    obj = obj.lower() # Takes care of case sensitivity
    if obj in data:
        return data[obj]
    else:
        guesses = gcm(obj,data.keys())
        if not len(guesses) == 0:
            check = "N"
            index = 0
            while check == "N" and index < len(guesses): # Allows for multiple suggestions
                check = input("Did you mean %s? Y/N: " % guesses[index],)
                if check == "Y":
                    break
                elif check == "N":
                    index = index + 1
                elif check != "Y" and check != "N": # Handling unexpected input without exiting the script
                    print("We did not understand your input. Plesae try again.")
                    check = "N"

        if check == "Y":
            return data[guesses[index]]

        return "The word you entered, %s, is not in this dictionary. Try again." % obj

word = input("Enter a word:",)
definition = define(word)

if type(definition)==list:
    for item in definition:
        print(item)
else:
    print(definition)
