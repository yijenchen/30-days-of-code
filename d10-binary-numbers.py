# Description: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Note: can also use built-in `bin()` to convert decimal int to str binary
#       representation

n = int(input())

n_bin = ''
while n > 0:
    n, b = divmod(n, 2)
    n_bin = str(b) + n_bin
    
print(max(map(len, n_bin.split('0'))))