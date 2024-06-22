# the concept key
programming_dictionary = {
    "Bug": "an error in a program that preventes the program from running as expected",
    "Function" : "A piece of code that you can easily ",
}

#print(programming_dictionary["Function"])

#adding new items to dictionary
programming_dictionary["Loop"] = " The action of doing something over and over again."
#print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary["Function"])

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

for key_value in programming_dictionary:
    print(key_value)
    print(programming_dictionary[key_value])