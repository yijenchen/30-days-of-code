# Description: https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().rstrip().split()))
    
    for x in reversed(arr):
        print(x, end=' ')