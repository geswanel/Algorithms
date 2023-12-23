"""
snail on vertical line
n berries.
ai to top when fed and bi to bottom at night
What is max height.

INPUT:
n - 5*1e5
ai bi - n lines 1e9

OUTPUT:
maxHeight
n numbers - the order

Solution:
When ai - bi <= 0 this berries at the end, max a should be first
ai - bi > 0 - accumulate height + first

We have 2 arrays of indices. that result in up and down movement.
i1, i2, i3 .... j , k1, k2, k3 ....
for i => a[i] - b[i] > 0
for k => a[k] - b[k] < 0. a[k1] = max(ak)

for j ? j may be k1 or i_last:
For any index g in i and j = i_last =>
a[g] - b[g] + a[j] >= a[j] - b[j] + a[g]
          - b[g]   >= - b[j]
              b[j] >= b[g]
=> max bj for last in ai - bi > 0
"""

def maxHeight(order, a, b):
    height = 0
    ans = 0
    for i in order:
        height += a[i]
        if height > ans:
            ans = height
        height -= b[i]
    
    return ans

def feedOrder(n, a, b):
    up = []
    down = []
    for i in range(n):
        if a[i] - b[i] > 0:
            up.append(i)
        else:
            down.append(i)
    
    order = []
    # finding last in ai-bi > 0 sequence
    if up:
        maxBU = 0
        maxBUId = None
        for i in up:
            if b[i] > maxBU:
                maxBU = b[i]
                maxBUId = i
        up.remove(maxBUId)
        order.extend(up + [maxBUId])
    # finding first in ai-bi <= 0 sequence
    if down:
        maxAD = 0
        maxADId = None
        for k in down:
            if a[k] > maxAD:
                maxAD = a[k]
                maxADId = k
        down.remove(maxADId)
        order.extend([maxADId] + down)

    return order

def main():
    n = int(input())
    a = []; b = []
    for _ in range(n):
        ai, bi = (int(x) for x in input().split())
        a.append(ai); b.append(bi)

    order = feedOrder(n, a, b)
    print(maxHeight(order, a, b))
    print(" ".join([str(i + 1) for i in order]))


if __name__ == "__main__":
    main()