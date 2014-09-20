"""
Excercise 1.1-1
Using Figure 1.2 as a model, illustrate the operation of Insertion-Sort
on the array A = {31,41,59,26,41,58}.
---
The tricky part was that there was 2 same numbers in the array
The other thing was, of course, that I had to find a solution
from the internet in order to understand the Pseudo-code in the
book, which I suppose I learn how to read while going further.
---
"""

myArray = [31, 41, 59, 26, 41, 58]
print "Unsorted array: " + str(myArray)

for i in range(len(myArray)):
    myVal = myArray[i]
    j = i - 1
    while (j >= 0) and (myArray[j] >= myVal):
        myArray[j+1] = myArray[j]
        j = j -1
    myArray[j+1] = myVal

print "Sorted array: \t" + str(myArray)
