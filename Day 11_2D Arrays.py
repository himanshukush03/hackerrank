#CODE:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
total= -float('inf')  # inf is infinity - a value that is greater than any other value. -inf is therefore smaller than any other value. nan stands for Not A Number, and this is not equal to 0 .  
for i in range(len(arr)-2):
    for j in range(len(arr)-2):
        total=max(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2],total)
    
print(total)
