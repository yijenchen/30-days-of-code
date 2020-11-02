# Description: https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == '__main__':
    n = int(input())
    assert 1 <= n <= 1000, 'Invalid array size'

    arr = list(map(int, input().rstrip().split()))
    assert len(arr) == n, 'Number of array elements does not match chosen array size'
    func = lambda x: 1 <= x <= 10000
    assert all(map(func, arr)), 'One or more array elements lie in invalid range'
    
    for num in reversed(arr):
        print(num, end=' ')