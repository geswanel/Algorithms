"""
Enemy:
0 soldiers
Army producing enemy's building. y health, p soldiers per round
Player:
x soldiers
1 round each soldier can
    kill 1
    1 damage to building

Round:
1. each player's soldier move
2. each enemy's soldier kills player's soldiers
3. new p soldiers from bulding

Min number of round to destroy building and kill enemy's soldiers or -1

x, y, p < 5000
Solution ??????????????
Brute force => recursy or dp

ai - damage to barracks
Round:
y[i + 1] = y[i] - ai
e[i + 1] = e[i] - (x[i] - ai)
x[i + 1] = x[i] - (e[i] - (x[i] - ai))
e[i + 1] += p * (y[i + 1] > 0)

x[i] - (e[i] - (x[i] - ai)) > 0:
xi - ei + xi - ai > 0

ai < 2xi - ei
ai < yi # can damage more than y

bi - damage to enemies
y[i + 1] = y[i] - (x[i] - bi)
e[i + 1] = e[i] - bi
x[i + 1] = x[i] - (e[i] - bi)
e[i + 1] += p * (y[i + 1] > 0)

xi - ei + bi > 0
bi > ei - xi


y = 0
e[i + 1] = e[i] - x[i]
x[i + 1] = x[i] - e[i + 1]
2 x[i] - e[i]

y[i + 1] = y[i] - ai
e[i + 1] = e[i] - (x[i] - ai) + p(y[i + 1] > 0)
x[i + 1] = 2 * x[i] - e[i] - a[i]

"""

def nextRound(x, y, e, p, barDam, enDam):
    y = max(y - barDam, 0); e = max(e - enDam, 0)
    x = max(x - e, 0)
    e += p * (y > 0)
    return x, y, e, p

res = -1
def minRounds(x, y, e, p, round):
    print("Round ", round, x, y, e)
    global res
    if res != -1 and res <= round:
        return res
    
    if 2 * x < e:
        return -1
    #print("Round {}: x{}; y{}; e{}".format(round, x, y, e))
    if x == 0 and (y > 0 or e > 0):
        return -1
    elif x > 0 and y <= 0 and e <= 0:
        res = round
        return round
    else:
        # attack barrack
        barDam = min(x, y)
        enDam = x - barDam
        ans1 = minRounds(*nextRound(x, y, e, p, barDam, enDam), round + 1)
        if ans1 > 0 and (res == -1 or ans1 < res):
            res = ans1
        # attack enemies
        enDam = min(x, e)
        barDam = x - enDam
        nextRoundState = nextRound(x, y, e, p, barDam, enDam)
        if nextRoundState == (x, y, e, p):
            ans2 = -1
        else:
            ans2 = minRounds(*nextRound(x, y, e, p, barDam, enDam), round + 1)

        if ans1 == -1:
            return ans2
        elif ans2 == -1:
            return ans1
        else:
            return min(ans1, ans2)

def main():
    x, y, p = [int(input()) for _ in range(3)]
    print(minRounds(x, y - x, p * ((y - x) > 0), p, 1))

if __name__ == "__main__":
    main()