# Description: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())

phone_book = {}
for i in range(n):
    name, phone = input().split()
    phone_book[name] = phone  # overwrite old value for existing key

while True:
    try:
        name = input()
        
        if not name:  # detect EOF when input comes from sys.stdin
            break
        elif name in phone_book:
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
        
    except EOFError:  # detect EOF when input comes from file redirection
        break