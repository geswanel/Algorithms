"""
Description:
Lapta game. One team catches the ball and tries to touch runner using the ball.
Another team player before running should throw the ball in the field.
Max distance is known
Velocities and coordinates of players of the first team is known.

Angle and force to throw the ball so the min time for the first team to catch it is max.

Input:
D N - max distance and number of rivals 1000, 200
xi yi vi - N players parameters - integer numbers

Runner is located in (0, 0) the ball is throwed to y >= 0

Output:
min time
coordinates of ball 1e-3 precision

Solution:
Find the farthest point by time from every player in half-.circle
0. Time [0, 3000] => logT
1. For each t
- Iterate over circles  O(n)
    - For each circle find intersections with others O(n) - points
        these points are candidates
            check if point is outside any circle O(n)

"""
from math import sqrt


eps = 1e-3

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({round(self.x, 3)}, {round(self.y, 3)})"
    
    def __repr__(self):
        return str(self)

class Circle:
    def __init__(self, x, y, r):
        self.p = Point(x, y)
        self.r = r
    
    def __str__(self) -> str:
        return f"Circle({round(self.r)}, {self.p})"
    
    def __repr__(self) -> str:
        return str(self)

def displace(points, displacement):
    for p in points:
        p.x += displacement[0]
        p.y += displacement[1]

def validPoint(D: int, p: Point):
    return p.y  >= 0 and (p.x * p.x + p.y * p.y <= D * D + eps)

def validatePoints(D: int, points: list[Point]):
    ans = []
    for p in points:
        if validPoint(D, p):
            ans.append(p)
    
    return ans

def circlesIntersection(D:int, c1: Circle, c2: Circle):
    displacement = (c1.p.x, c1.p.y)
    dx = c2.p.x - c1.p.x
    dy = c2.p.y - c1.p.y

    a = 2 * dx; b = 2 * dy
    c = c2.r * c2.r - c1.r * c1.r - dx * dx - dy * dy
    points = circleLineIntersection(c1.r, a, b, c)
    displace(points, displacement)
    
    return validatePoints(D, points)

def circleLineIntersection(r, a, b, c) -> list[Point]:
    a2b2 = a * a + b * b
    x0 = -a * c / a2b2; y0 = -b * c / a2b2
    d2 = r * r - c * c / a2b2
    ans = []
    if d2 > 0: # 2 points
        mult = sqrt(d2 / a2b2)
        p1 = Point(x0 + b * mult, y0 - a * mult)
        p2 = Point(x0 - b * mult, y0 + a * mult)
        ans += [p1, p2]
    elif d2 == 0: # 1 point
        ans += [Point(x0, y0)]
    return ans

class Player:
    def __init__(self, x, y, v):
        self.p = Point(x, y)
        self.v = v
    
    def createCircle(self, time):
        return Circle(self.p.x, self.p.y, self.v * time)

    def __str__(self) -> str:
        return f"Player({self.v}, {self.p})"
    
    def __repr__(self) -> str:
        return str(self)


def edgeIntersection(D: int, cir: Circle):
    candPoints = horizCircleIntersection(D, cir)

    candPoints += circlesIntersection(D, Circle(0, 0, D), cir)

    return candPoints

def horizCircleIntersection(D: int, cir: Circle):
    displacement = (cir.p.x, cir.p.y)
    a = 0; b = 1; c = cir.p.y
    points = circleLineIntersection(cir.r, a, b, c)
    
    displace(points, displacement)
    return validatePoints(D, points)


def isInside(N: int, players: list[Player], point: Point, t: float):
    for player in players:
        c = player.createCircle(t)
        dx = (point.x - player.p.x)
        dy = (point.y - player.p.y)
        dist2 = dx * dx + dy * dy

        if dist2 + eps < c.r * c.r:
            return True
    
    return False

def candPoint(D: int, N: int, players: list[Player], t: float):
    #print(f"Time {t:=^20}")
    edgeIntFlag = False
    for i in range(N):
        p = players[i]
        c = p.createCircle(t)
        edgePoints = edgeIntersection(D, c)
        for point in edgePoints:
            edgeIntFlag = True
            if not isInside(N, players, point, t):
                return point
    
    if not edgeIntFlag:
        point = Point(0, 0)
        if not isInside(N, players, point, t):
            return point

    for i in range(N):
        p1 = players[i]
        c1 = p1.createCircle(t)
        for j in range(i + 1, N):
            p2 = players[j]
            c2 = p2.createCircle(t)
            candPoints = circlesIntersection(D, c1, c2)

            #print(f"Candidate points for {c1} and {c2}")
            #print(candPoints)
            for point in candPoints:
                if not isInside(N, players, point, t):
                    return point

    return None


def ballEndpoint(D, N, players):
    tMin = 0
    tMax = 3000

    while tMax - tMin > eps:
        tMid = (tMax + tMin) / 2
        point = candPoint(D, N, players, tMid)
        if point:
            tMin = tMid
        else:
            tMax = tMid
    
    return tMin, candPoint(D, N, players, tMin)



def main():
    D, N = (int(x) for x in input().split())
    players = []
    for _ in range(N):
        x, y, v = (int(x) for x in input().split())
        players.append(Player(x, y, v))
    
    maxTime, point = ballEndpoint(D, N, players)
    print(round(maxTime, 3))
    print(round(point.x, 3), round(point.y, 3))

def circleIntersectionTest():
    while True:
        x1, y1, r1 = (int(x) for x in input().split())
        x2, y2, r2 = (int(x) for x in input().split())

        #print(circlesIntersection(1e10, Circle(x1, y1, r1), Circle(x2, y2, r2)))

if __name__ == "__main__":
    #circleIntersectionTest()
    main()