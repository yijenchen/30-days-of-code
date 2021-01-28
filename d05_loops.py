# Description: https://www.hackerrank.com/challenges/30-loops/problem

if __name__ == '__main__':
    n = int(input())
    assert 2 <= n <= 20, 'Invalid input'
    
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')