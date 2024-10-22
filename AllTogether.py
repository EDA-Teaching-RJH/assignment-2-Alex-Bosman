### Part Four -- your code goes here. 
import random
randomList = [random.randint(1, 100) for i in range(10)]
print(randomList)
finalList = []
for index, number in enumerate(randomList):
    if  number % 2:
        finalList.append(number)
print(finalList)