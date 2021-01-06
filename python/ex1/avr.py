#!/bin/python3

import math
import os
import random
import re
import sys



# write your code here
def avg(*arr):
    if len(arr)==0:
        return 0
    total=0
    for num in arr:
        total=total+num
    return total/len(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()