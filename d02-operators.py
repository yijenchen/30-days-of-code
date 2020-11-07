# Description: https://www.hackerrank.com/challenges/30-operators/problem

def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost * (1 + tip_percent * 1e-2 + tax_percent * 1e-2)
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)