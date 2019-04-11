#!/usr/bin/python3
# Filename: test_fib.py

from fibo import fib, fib2

fib(10)
result = fib2(10)
print(result)

for num in result:
    print(num)

for num in result:
    print(num,end=' ')
