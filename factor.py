#!/usr/bin/env python3

def factorc(n):
    """
    return (p, count) list
    """
    facs = []
    curr_fac = 2
    while n != 1:
        count = 0
        while n % curr_fac == 0:
            n = n // curr_fac
            count += 1
        if count > 0:
            facs.append((curr_fac, count))
        curr_fac += 1 if curr_fac == 2 else 2
    return facs

def factor(n):
    """
    return list of all factors in ascending order
    """
    facs = factorc(n)
    l = []
    for n, count in facs:
        l += count * [n]
    return l
