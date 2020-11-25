# Description: https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == '__main__':
    n = int(input())
    assert 1 <= n <= 1000, 'Invalid integer'
    
    arr = list(map(int, input().rstrip().split()))
    assert len(arr) == n, 'Invalid number of array elements'
    assert all(map(lambda x: 1 <= x <= 10000, arr)), \
          'Invalid array element(s)'
    
    for x in reversed(arr):
        print(x, end=' ')