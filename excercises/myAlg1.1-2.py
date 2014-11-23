"""
Excercise 1.1-2
Using Figure 1.2 as a model, illustrate the operation of Insertion-Sort
on the array A = {31,41,59,26,41,58}.
Rewrite the Insertion-Sort procedure to sort into nonincreasing 
instead of nondecreasing order.
---
Well, it took 2 minutes of staring and remembering the 
whole algorithm before I got that it was only one character 
change that was needed. 
In the while -sentence, the myArray[j] has to be smaller 
or equal to myVal. 
"""

myArray = [31, 41, 59, 26, 41, 58]
print "Unsorted array: " + str(myArray)

for i in range(len(myArray)):
    myVal = myArray[i]
    j = i - 1
    while (j >= 0) and (myArray[j] <= myVal):
        myArray[j+1] = myArray[j]
        j = j -1
    myArray[j+1] = myVal

print "Sorted array: \t" + str(myArray)