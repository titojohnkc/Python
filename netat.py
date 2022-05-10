#Author: Dane Johnson
#Purpose: Convert list of numbers to their ASCII value

#import necessary libraries
import string

#declare variables
flag = []
count = 0

#open text file
f = open("numbers.txt", "r")

#load each line of text file into flag
for x in f:
    flag.append(x)

#amend each index of flag list while there are elements in flag list
while count < len(flag):
    flag[count] = chr(int(flag[count]))
    count+=1

#join characters in list into one continuous string
d = "".join(flag)

#print file
print(d)

#close file
f.close()
