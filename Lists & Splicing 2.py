cakeList = ["cake", "is"]
print(str(cakeList))
cakeAdd = input("Choose a word to add to this sentence: ")
# adding to a list
cakeList.insert(len(cakeList), cakeAdd)
print(str(cakeList))
sentence = ["There", "are", "some", "words", "missing"]
print(str(sentence))
# NOTE: you could change these four lines to match the splicing off a list style
wordOne = input("Word one: ")
wordTwo = input("Word two: ")
wordThree = input("Word three: ")
missingWords = [wordOne, wordTwo, wordThree]
# splicing onto a list
sentence[5:] = missingWords
print(str(sentence))
badSentence = ["I", "remove", "these", "words", "love", "Python"]
print(str(badSentence))
# splicing off a list
badSentence[int(input("Index one: ")):int(input("Index two: "))] = []
print(str(badSentence))
input("Press Enter to quit...")
