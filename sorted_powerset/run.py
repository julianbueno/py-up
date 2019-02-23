#!/usr/bin/python3

from itertools import chain, combinations

def powerset(iterable):
    "Given a string of lowercase unique characters (e.g. 'ab', 'lmne') sort the string alphabetically and then find all possible combinations, ignoring ordering. e.g. 'ab' -> 'a', 'b', 'ab'" 
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

if __name__ == '__main__':
    str = str(input())
    #a = list(map(int, input().rstrip().split()))
    print(sorted(map(''.join, powerset(str))))           