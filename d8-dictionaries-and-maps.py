# Description: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())

phone_book = {}
for i in range(n):
    name, phone = input().split()
    phone_book[name] = phone

while True: 
    try:
        q = input()
        if q in phone_book:
            print(f'{q}={phone_book[q]}')
        else:
            print('Not found')

    except EOFError:
        break