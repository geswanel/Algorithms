"""
n numbers
+ x signs
result odd

input:
n
ai - n numbers

odd * odd = odd
odd + even = odd
any other combinations => even

find odd island
...* even + (odd *... odd) + even *...

"""

def findOddWindow(a: list[int]):
    start = -1
    
    for i, num in enumerate(a):
        if num % 2 == 1 and start == -1:
            start = i
        elif num % 2 == 0 and start != -1:
            return start, i - 1
    
    return start, len(a) - 1

def operations(a: list[int]):
    firstOdd = -1
    ans = ["x"] * (len(a) - 1)

    st, end = findOddWindow(a)
    if st > 0:
        ans[st - 1] = "+"
    
    if end < len(ans):
        ans[end] = "+"
        
    return "".join(ans)



def main():
    n = int(input())
    a = [int(x) for x in input().split()[:n]]
    print(operations(a))


if __name__ == "__main__":
    main()