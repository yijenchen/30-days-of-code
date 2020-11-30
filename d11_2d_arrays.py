# Description: https://www.hackerrank.com/challenges/30-2d-arrays/problem

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

vals = []
for i in range(4):
    for j in range(4):
        val = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        vals.append(val)
        
print(max(vals))