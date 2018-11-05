#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
For loop and function python katas.
"""
__author__ = "tgentry300"


def add(a, b):
        return (a + b)

def multiply(a, b):
    total = 0
    for x in range(a):
        total = add(total, b)
    return total

def power(x, n):
    total = x
    for i in range(n - 1):
        total = (multiply(total, x))
    return total

def fibonacci(n):
    result = 0
    y = 0
    x = 1
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    for i in range(n - 2):
        result = add(x, y)
        y = x
        x = result
    
    return result

        


def main():
    print(add(1, 2))
    print(multiply(3, 4))
    print(power(2, 3))
    print(fibonacci(8))



if __name__ == '__main__':
    """Runs main function containing all kata functions"""
    main()
