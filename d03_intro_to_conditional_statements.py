# Description: https://www.hackerrank.com/challenges/30-conditional-statements/problem

if __name__ == '__main__':
    n = int(input())
    assert 1 <= n <= 100, "Invalid input"
    
    if n % 2 or 6 <= n <= 20:  # short-circuit evaluation
        print('Weird')
    else:
        print('Not Weird')