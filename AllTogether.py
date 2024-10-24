### Part Four -- your code goes here. 
# using a for loop and a while loop:
import random
numberList = [random.randint(1, 100) for i in range(10)]
evenNumbers = []
for x in numberList:
    if not (x % 2):
        evenNumbers.append(x)
while len(evenNumbers) != 0:
    numberList.remove(evenNumbers.pop())
print(numberList)


# more elegant solution (but doesn't use while loop so not used.)
'''
import random
print([x for x in [random.randint(1, 100) for i in range(10)] if x % 2 == 1])
'''
