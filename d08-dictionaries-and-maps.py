# Description: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())

phone_book = {}
for i in range(n):
    name, num = input().split()
    phone_book[name] = num

while True:
    try:
        q = input()
        
        if not q:  # detect EOF when input comes from sys.stdin
            break
        elif q in phone_book:
            print(f'{q}={phone_book[q]}')
        else:
            print('Not found')
        
    except EOFError:  # detect EOF when input comes from data redirected by bash
        break