#!/usr/bin/env python3
"""
kleine Implementierung des EEA
"""

def eea(a, b, write=False):
    def printd(a, b):
        if write:
            print(a, b)
    vals = []

    while b != 0:
        vals.append((a, b))
        printd(a, b)
        r = a % b
        a, b = b, r

    res = a
    al = 0
    be = 1

    vals.pop()
    vals.reverse()
    for (a, b) in vals:
        printd(al, be)
        al, be = be, al - (a // b) * be

    printd(al, be)
    return res, al, be

def gcd(a, b):
    return eea(a, b)[0]
