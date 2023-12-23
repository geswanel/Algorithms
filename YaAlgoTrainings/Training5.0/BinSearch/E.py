"""
Description:
Fraction numeration
Cantor

for n fraction identify numerator and denominator
INPUT:
n
OUTPUT
num/den
Solution:
1. Use binsearch to find out diagonal with needed number
    till k diagonal including => k * (k + 1) / 2 fractions
    so we need to identify min k such that k * (k + 1) / 2 >= n
    so fraction is placed in the k diagonal 
2. find out direction of numerating fractions
    even: left to right, bottom to top
    odd: right to left, top to bottom
3. identify fraction
"""
import unittest


def fractionDiagonal(n):
    l = 0
    r = n
    while l < r:
        k = (l + r) // 2
        if k * (k + 1) // 2 < n:
            l = k + 1
        else:
            r = k
    
    return l

def fraction(n):
    diag = fractionDiagonal(n)
    pos = n - (diag) * (diag - 1) // 2
    if diag % 2 == 0:
        num = diag + 1
        den = 0
        return f"{num - pos}/{den + pos}"
    else:
        num = 0
        den = diag + 1
        return f"{num + pos}/{den - pos}"



def main():
    n = int(input())
    print(fraction(n))


class TASK_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()