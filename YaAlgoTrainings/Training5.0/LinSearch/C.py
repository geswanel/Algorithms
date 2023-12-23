"""
2 lines same length
1 was cut into N parts
N 1

1 of them was taken

the smallest length of taken part

L = l1 + l2 + ... lN

Taken i:
    max > sum()
    max - sum
Taken L:
    max <= sum
    sum + max


"""
def minLine(l):
    maxL = 0
    sumL = 0
    for line in l:
        if line > maxL:
            maxL = line
        sumL += line
    sumL -= maxL
    if maxL <= sumL:
        return maxL + sumL
    else:
        return maxL - sumL

    


def main():
    N = int(input())
    l = [int(x) for x in input().split()]
    
    print(minLine(l))


if __name__ == "__main__":
    main()