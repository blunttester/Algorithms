"""
Excercise 1.1-3
Using Figure 1.2 as a model, illustrate the operation of Insertion-Sort
on the array A = {31,41,59,26,41,58}.
Write code for linear search which scans through the sequence looking for value 
and returns it or a message that value was not found.
---
The trouble in here was that the binary myStatement got 
written over on every non -matching value. I had the myStatement
assignment to True and False inside the for -loop. The trick was to
move the False -assignment outside the for -loop and check the 
value after the loop.
"""
from random import randrange

myArray = [31, 41, 59, 26, 41, 58]
print "Scanned array: " + str(myArray)
myVal = randrange(20, 60) 
print "Value to be found: " + str(myVal)
myStatement = False
for i in range(len(myArray)):
    if myVal == myArray[i]:
        myStatement = True

if myStatement:
    print "Value " + str(myVal) + " found on the array" +  str(myArray) + "\n"
else:
    print "Value " + str(myVal) + " NOT found on the array" +  str(myArray) + "\n"