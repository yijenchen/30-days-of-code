# Description: https://www.hackerrank.com/challenges/30-conditional-statements/problem?h_r=email&unlock_token=583a3af111bcb85b7b7bb17fccddef43a0eb11bd&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

if __name__ == '__main__':
    N = int(input())
    assert 1 <= N <= 100, "Invalid input"
            
    if N % 2 or 6 <= N <= 20:  # short-circuit evaluation
        print('Weird')
    else:
        print('Not Weird')