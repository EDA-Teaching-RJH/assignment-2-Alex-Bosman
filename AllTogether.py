### Part Four -- your code goes here. 
import random
randomList = [random.randint(1, 100) for i in range(10)]
print(randomList)
finalList = []
for index, number in enumerate(randomList):
    if  number % 2:
        finalList.append(number)
print(finalList)


'''
# one line lol
#exec("import random\nprint([x for x in [random.randint(1, 100) for i in range(10)] if x % 2 == 0])")
'''

'''
# using a for loop and a while loop:
import random
myArray = [random.randint(1, 100) for i in range(10)]
print(myArray)
oddNumbers = []
for x in myArray:
    if x % 2:
        oddNumbers.append(x)
while len(oddNumbers) != 0:
    myArray.remove(oddNumbers.pop())
print(myArray)
'''
