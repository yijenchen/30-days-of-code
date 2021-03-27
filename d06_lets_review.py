# Description: https://www.hackerrank.com/challenges/30-review-loop/problem

t = int(input())

for i in range(t):
    s = input()
    print(s[::2], s[1::2])