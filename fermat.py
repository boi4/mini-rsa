#!/usr/bin/env python3
from random import randrange

def fermat_test(n):
    return ((randrange(1, n) ** (n - 1)) % n) == 1

def isprime(p, tries):
    for i in range(tries):
        if not fermat_test(p):
            return False
    return True
