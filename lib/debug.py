#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    p1 = Player('andy')
    p2 = Player('bob')
    p3 = Player('ted')

    g1 = Game('ball')
    g2 = Game('stick')
    g3 = Game('disc')

    r1 = Result(p1, g1, 2)
    r2 = Result(p1, g2, 12)
    r3 = Result(p2, g1, 24)
    r4 = Result(p3, g3, 45)
    r5 = Result(p1, g1, 4)

    ipdb.set_trace()
