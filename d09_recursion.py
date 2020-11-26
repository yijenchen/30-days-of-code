# Description: https://www.hackerrank.com/challenges/30-recursion/problem

def factorial(n):
    assert n >= 0, 'Invalid input'
    return 1 if n <= 1 else n * factorial(n-1)


n = int(input())
print(factorial(n))