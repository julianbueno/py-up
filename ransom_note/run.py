#!/usr/bin/python3

import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for i in note:
        try:
            del magazine[magazine.index(i)]
        except ValueError:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
