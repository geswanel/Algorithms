"""
k friends
n profit
in each of next d days add a digit at the end of n
each day n % k == 0

if k <= 10 - always can choose a digit
if k > 10 - can choose <= 1 digit. if can't => -1

so if k > 10 => only 1 example exists
if k < 10 => can choose any

(n * 10 + digit) % k == 0
digit ?

1 step
(n * 10 + digit) % k = 0
n = n * 10 + digit
"""
import sys

sys.set_int_max_str_digits(100010)

def countProfit(n, k, d):
    digit = (k - (n * 10) % k) % k
    if digit < 10:
        n = n * 10 + digit
    else:
        return -1
    
    return n * int(10 ** (d - 1))


def main():
    n, k, d = [int(x) for x in input().split()[:3]]
    print(countProfit(n, k, d))


if __name__ == "__main__":
    main()