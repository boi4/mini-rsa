#!/usr/bin/env python3
"""
small rsa implementation, using chinese remainder theorem
do not use for critical purposes
"""

from random import randrange

from factor import factor
from millerrabin import isprime
from gcd import eea, gcd
from crt import crt


def get_rand_prime(a, b):
    """
    return random prime between a and b
    """
    while True:
        s = randrange(a, b)
        if isprime(s):
            return s

def create_key():
    """
    return (pub_key, priv_key) pair
    """
    while True:
        p = get_rand_prime(2**10, 2**16)
        q = get_rand_prime(2**10, 2**16)
        if gcd(p, q) == 2:
            break

    phi = (p - 1) * (q - 1)
    f = factor(p - 1) + factor(q - 1)
    d, dp, dq = 0, 0, 0
    while True:
        e = get_rand_prime(1, phi)
        if e not in f:
            d = eea(e, phi)[1]
            dp = d % (p - 1)
            dq = d % (q - 1)
            if dp & 1 == dq & 1:
                break

    return (e, p * q), (p, q, dp, dq)

def encrypt(m, pub):
    """
    encrypts message m with publickey pub
    """
    e, n = pub
    return pow(m, e, n)

def decrypt(c, pub, priv):
    """
    decrypt encrypted message c
    """
    e, n = pub
    p, q, dp, dq = priv
    mp = pow(c, dp, p)
    mq = pow(c, dq, q)
    return crt([mp, mq], [p, q])
