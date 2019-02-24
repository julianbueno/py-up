
#!/usr/bin/python3

import math
import os
import random
import re
import sys
from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        "{} {}".format(self.name, self.score)
    
    def comparator(self, a, b):
        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        return val


def main():
    ''' Main function '''

    player_count = int(input())
    data = []
    for i in range(player_count):
        name, score = input().split()
        score = int(score)
        player = Player(name, score)
        data.append(player)

    data = sorted(data, key=cmp_to_key(Player.comparator))
    for i in data:
        print(i.name, i.score)

if __name__ == '__main__':
    main()
