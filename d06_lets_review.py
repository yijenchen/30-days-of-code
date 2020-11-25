# Description: https://www.hackerrank.com/challenges/30-review-loop/problem

t = int(input())
assert 1 <= t <= 10, 'Invalid integer'

for i in range(t):
    s = input()
    assert 2 <= len(s) <= 10000, 'Invalid string length'
    
    print(s[::2], s[1::2])