# Description: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Note: can also use built-in `bin()` to convert decimal int to str binary rep

n = abs(int(input()))  # make code work for any integer

n_bin = ''
while n:
    n, b = divmod(n, 2)
    n_bin = str(b) + n_bin
    
print(max(map(len, n_bin.split('0'))))