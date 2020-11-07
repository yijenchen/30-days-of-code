# Description: https://www.hackerrank.com/challenges/30-conditional-statements/problem

if __name__ == '__main__':
    N = int(input())
    assert 1 <= N <= 100, "Invalid input"
            
    if N % 2 or 6 <= N <= 20:  # short-circuit evaluation
        print('Weird')
    else:
        print('Not Weird')