#!/usr/bin/python3

import math
import os
import random
import re
import sys

def countSwaps(a):
    length = len(a)-1
    swap_count = 0
    while length > 0:
          for i in range(0,length):
            # if this element is greater than the next element - swap
            if (a[i] > a[i+1]):
                # swap the values
                a[i], a[i+1] = a[i+1], a[i]
                swap_count += 1
          length-=1

    print("Array is sorted in",str(swap_count),"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])                             


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)