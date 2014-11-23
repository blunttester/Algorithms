"""
Exercise 1.2-1
Consider sorting n numbers stored in array A by first finding 
the smallest element of A and putting it in the first entry 
of another array B. Continue with the rest of the elements of A
until n elements of A are stored in array B.
---
---
"""
from random import randrange
myArray = []
myArrayB = []
myNumbersToBeStored = randrange(1,60)
for a in range(1,60):
    myVal = randrange(999)  
    myArray.append(myVal)
    
print "Unsorted array: " + str(myArray)

for i in range(len(myArray)):
    myVal = myArray[i]
    j = i - 1
    while (j >= 0) and (myArray[j] >= myVal):
        myArray[j+1] = myArray[j]
        j = j -1
    myArray[j+1] = myVal

print "Sorted array: \t" + str(myArray)
print "The numbers to be stored in Array B: " + str(myNumbersToBeStored)

for b in range(myNumbersToBeStored):
    myArrayB.append(myArray[b]) 
    
print "Numbers in array B: " + str(myArrayB)