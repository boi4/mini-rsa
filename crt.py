#!/usr/bin/env python3
import operator
from functools import reduce

def crt(rest_list, modulus_list):
    """
    einfache Implementierung des Chinesischen Restsatzes 
    TODO: test if modulus gcd = 1
    """
    def product(l):
        return reduce(operator.mul, l, 1)

    not_changers = []

    for rest, modulus in zip(rest_list, modulus_list):
        tmp = list(modulus_list)
        tmp.remove(modulus)
        x = mul_list(tmp)
        c = 1
        while True:
            if (c * x) % modulus == rest:
                break
            c += 1
        not_changers.append(c * x)
    return sum(not_changers) % product(modulus_list)
