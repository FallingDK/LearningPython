one = input("Word One: ")
two = input("Word Two: ")
three = input("Word Three: ")
four = input("Word Four: ")
five = input("Word Five: ")
# add strings to list
newList = [one, two, three, four, five]
print("Your list is: ")
# cast list to string to print
print(str(newList))
# print based upon index
print("The third element in your list is, " + str(newList[2]))
# print based upon minus index
print("The second until last element in your list is, " + str(newList[-2]))
# print based upon second letter of first word in list
print("The second letter of the first element in the list is, " +
      str(newList[0][1]))
# a slice to extract elements, includes both -2 and the rest of the list
print("The last two elements are, " + str(newList[-2:]))
# prints even elements, the two blanks = start at 0, end at end of list
print("The even elements are: " + str(newList[::2]))
# prints the odd elements
print("The odd elements are: " + str(newList[1::2]))
# prints elements backwards
print("Elements backwards: " + str(newList[::-1]))
# prints even elements backwards
print("The even elements backwards: " + str(newList[::-2]))
# prints odd elements backwards
print("The odd elements backwards: " + str(newList[3::-2]))
# check the list for element based on user input
search = input("Search for a word inside your list: ")
print(search in newList)
# print number of elements in list
print("The number of elements in your list: " + str(len(newList)))
# edit element in list
editIndex = input("Choose element to edit: ")
editString = input("Choose new string: ")
newList[int(editIndex) - 1] = editString
print(str(newList))
# delete an element
del newList[int(input("Choose element to delete: ")) - 1]
print(str(newList))
input("Press Enter to quit...")
