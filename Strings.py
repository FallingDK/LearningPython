"""
Application based upon Strings.
Also this is a multiline comment in Python.
"""
# single line comment
fname = input("What's your first name: ")
sname = input("What's your surname: ")
# concatenate and display the name input
name = fname + " " + sname
print(name)
# input the age as a string
ageString = input("What's your age: ")
# cast the age to an integer, to do simple calculation
age = int(ageString)
nextAge = age + 1
# cast back to string to allow print
nextAgeString = str(nextAge)
print("So on your next birthday you'll be " + nextAgeString)
input("Press Enter to quit...")



