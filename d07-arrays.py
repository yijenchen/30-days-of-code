# Description: https://www.hackerrank.com/challenges/30-arrays/problem

if __name__ == '__main__':
    n = int(input())

    arr = input().rstrip().split()
    assert len(arr) == n, 'Number of array elements does not match chosen array size'
    func = lambda x: 1 <= int(x) <= 10000
    assert all(map(func, arr)), 'One or more array elements lie in invalid range'
    
    print(' '.join(reversed(arr)))