#!/usr/bin/python3

import sys

# Complete the minimumBribes function below.
def minimumBribes(a, t):
    swaps = [0] * t

    swapped = True

    while swapped:
        swapped = False

        for i in range(t):
            while i < t - 1 and a[i] > a[i + 1]:
                swaps[a[i] - 1] += 1
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                i += 1

    bribes = 0
    for swap in swaps:
        bribes += swap

        if swap > 2:
            print('Too chaotic')
            break
    else:
        print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q,n))
