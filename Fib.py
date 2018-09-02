# -*- coding:utf-8 -*-
'''斐波那契数列'''
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_fix(n):
    a, b = 0, 1
    result = []
    while a < n:
        result.append(b)
        a, b = b, a + b
    return result

print fib(5)
print fib_fix(6)