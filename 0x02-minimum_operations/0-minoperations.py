#!/usr/bin/python3
""" this is a module """


def minOperations(n):
    """this is a method"""
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops