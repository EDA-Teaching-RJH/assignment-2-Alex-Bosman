### Part Three -- your code goes here. 
givenList = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
givenList.sort()
finalList = [x for x in givenList if x != 1] + [7, 8]
print(finalList)