#!/usr/bin/python3

import math
import os
import random
import re
import sys



# Complete the findNumber function below.
def findNumber(arr, k):
    for item in arr:
        if int(item) == k:
            return "YES"

    return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    print(res)

    # fptr.write(res + '\n')

    # fptr.close()