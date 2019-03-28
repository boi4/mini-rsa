#!/usr/bin/env python3
from random import randrange

def miller(n):
    exp = 0
    a = randrange(1, n)
    d = n - 1
    while d % 2 == 0:
        d = d // 2
        exp +=1

    x = pow(a,d,n)
    if x == n - 1 or x == 1:
        return True

    for i in range(exp):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def isprime_t(n, t):
    for i in range(t):
        if not miller(n):
            return False
    return True

def isprime(n):
    return isprime_t(n, 12)
