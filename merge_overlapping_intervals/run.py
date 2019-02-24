#!/usr/bin/python3

import math
import os
import random
import re
import sys

                      
def merge_intervals(intervals):
    """
    A simple algorithm can be used:
    1. Sort the intervals in increasing order
    2. Push the first interval on the stack
    3. Iterate through intervals and for each one compare current interval
       with the top of the stack and:
       A. If current interval does not overlap, push on to stack
       B. If current interval does overlap, merge both intervals in to one
          and push on to stack
    4. At the end return stack
    """
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
    return merged

def merge_overlapping(initialranges):
    i = sorted(set([tuple(sorted(x)) for x in initialranges]))

    # initialize final ranges to [(a,b)]
    f = [i[0]]
    for c, d in i[1:]:
        a, b = f[-1]
        if c<=b<d:
            f[-1] = a, d
        elif b<c<d:
            f.append((c,d))
        else:
            # else case included for clarity. Since 
            # we already sorted the tuples and the list
            # only remaining possibility is c<d<b
            # in which case we can silently pass
            pass
    return f    

if __name__ == '__main__':
    # l = [(1, 5), (11, 116), (3, 4), (10, 12), (6, 12)]
    l = [(1, 4), (2, 5), (6, 7)]
    print("Original list of ranges: {}".format(l))
    merged_list = merge_overlapping(l)
    print("List of ranges after merge_ranges: {}".format(merged_list))