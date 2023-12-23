"""
Description:
(x0, y0) -> (xn, yn) - broken line with vertical boundaries at the edges.
x0 < x1 < x2 < ... < xn
If a broken line is horizontal, then rain fills the height H.

What max height now in the pits? 1e-4 - precision

INPUT:
N H
xi yi - N + 1 points
OUTPUT
max H
Solution:
Divide our structure into isolated pits with calculated volume

0. Info:
H * dl => volume of water in the segment dl
0 < Hmax < (max(yi) - min(yi) + H)
For fixed Hcand:
    divide points into min size segments where (max(y) - min(y) > Hmax)
        this segments will have common edge points
    For each segment count volume if Hmax is the height of water.
    If all this volumes > H * (xRight - xLeft)
        decrease Hcand
    if any of them < H * (xRight - xLeft)
        increase Hmax
    if all this volumes > H * (xRight - xLeft) and at least 1 is equal => answer
1. Bin search Hcand
2. divide into pits O(n) (100)
3. Count volume of pits with Hcand water level O(n)
    4. Compare all volumes O(n) with precision

Didn't consider overflow
"""
import unittest

eps = (1e-4 / 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return str((self.x, self.y))
    
    def __repr__(self) -> str:
        return str((self.x, self.y))


def volume(points, topBound):
    pitVolume = 0
    for i in range(1, len(points)):
        lPoint = points[i - 1]
        rPoint = points[i]
        if lPoint.y <= topBound and rPoint.y <= topBound:
            a = topBound - lPoint.y
            b = topBound - rPoint.y
            h = rPoint.x - lPoint.x
            pitVolume += (a + b) * h / 2
        else:
            dx = rPoint.x - lPoint.x
            dy = rPoint.y - lPoint.y
            if lPoint.y <= topBound:
                hl = topBound - lPoint.y 
                a = hl * dx / dy
                pitVolume += a * hl / 2
            elif rPoint.y <= topBound:
                hr = topBound - rPoint.y
                a = - hr * dx / dy
                pitVolume += a * hr / 2
    return pitVolume


class Pit:
    LEFT_EDGE = -1
    RIGHT_EDGE = 1
    FLOW_RIGHT = 1
    FLOW_LEFT = -1
    NO_FLOW = 0
    def __init__(self):
        self.points = []
        self.edge = None
        self.pitVolume = 0
        self.waterVolume = 0
        self.yMin = 0
    
    def identifyEdge(self, edge):
        self.edge = edge
    
    def append(self, val):
        self.points.append(val)
    
    def extend(self, newPoints):
        self.points.extend(newPoints)
    
    def flowDirection(self):
        lBound = float('inf') if (self.edge is not None and self.edge == Pit.LEFT_EDGE)\
            else self.points[0].y 
        rBound = float('inf') if (self.edge is not None and self.edge == Pit.RIGHT_EDGE)\
            else self.points[-1].y 

        if lBound < rBound:
            return Pit.FLOW_LEFT
        elif lBound > rBound:
            return Pit.FLOW_RIGHT

        return Pit.NO_FLOW
    
    def __topBound(self):
        points = self.points
        if self.edge is not None:
            if self.edge == self.LEFT_EDGE and points[-1].y >= points[0].y:
                return points[-1].y
            if self.edge == self.RIGHT_EDGE and points[-1].y <= points[0].y:
                return points[0].y

        return min(points[0].y, points[-1].y)

    def __pitVolume(self):
        points = self.points
        topBound = self.__topBound()
        #print("topBound ", points, topBound)
        self.pitVolume = volume(points, topBound)

    def calculateVolumes(self, hWater=None):
        points = self.points
        
        if hWater is not None:
            self.waterVolume = (points[-1].x - points[0].x) * hWater

        # TODO: Consider edge pits with infinity walls
        self.__pitVolume()

    def unify(self, left, right):
        self.points = left.points[:-1] + right.points
        self.waterVolume = left.waterVolume + right.waterVolume
        if left.edge == Pit.LEFT_EDGE:
            self.edge = Pit.LEFT_EDGE
        elif right.edge ==Pit.RIGHT_EDGE:
            self.edge = Pit.RIGHT_EDGE
        
        self.__pitVolume()


    def __str__(self):
        return f"{self.points}: vol{self.pitVolume}, water{self.waterVolume}, edge{self.edge}, flow{self.flowDirection()}"


def divideIntoPits(N: int, points: list[Point]):
    pits = [Pit()]
    curPit = pits[0]
    curPit.identifyEdge(Pit.LEFT_EDGE)

    curPit.append(points[0])
    for i in range(1, N):
        curPit.append(points[i])
        if points[i - 1].y < points[i].y > points[i + 1].y:
            pits.append(Pit())
            curPit = pits[-1]
            curPit.append(points[i])
    curPit.append(points[-1])
    curPit.identifyEdge(Pit.RIGHT_EDGE)

    return pits


def flow(pits: list[Pit], id=None):
    flowed = False
    #print("Flowing process", id)
    i = 0
    while i + 1 < len(pits):
        leftPit = pits[i]
        rightPit = pits[i + 1]
        #print(f"{i}: left:{leftPit}\nright:{rightPit}")

        if leftPit.waterVolume >= leftPit.pitVolume and\
            rightPit.waterVolume >= rightPit.pitVolume and\
            leftPit.flowDirection() == Pit.FLOW_RIGHT and\
                rightPit.flowDirection() == Pit.FLOW_LEFT:
            # unify pits into 1 pit because they are full and will compound together
            #print("unification")
            newPit = Pit()
            newPit.unify(leftPit, rightPit)

            pits.pop(i + 1); pits.pop(i)
            pits.insert(i, newPit)
            
            flowed = True
            i -= 1
        elif leftPit.waterVolume > leftPit.pitVolume and\
            leftPit.flowDirection() == Pit.FLOW_RIGHT:
            #print("flow right")
            # flow from left to right
            delta = leftPit.waterVolume - leftPit.pitVolume
            leftPit.waterVolume -= delta
            rightPit.waterVolume += delta
            flowed = True
        elif rightPit.waterVolume > rightPit.pitVolume and\
            rightPit.flowDirection() == Pit.FLOW_LEFT:
            # from right to left
            #print("flow left")
            delta = rightPit.waterVolume - rightPit.pitVolume
            rightPit.waterVolume -= delta
            leftPit.waterVolume += delta
            flowed = True
        i += 1
    
    return flowed

        


def overflowing(pits: list[Pit]):
    overflowed = False
    i = 0
    while not overflowed:
        overflowed = True
        overflowed = not flow(pits, i)
        i += 1
        #print("OVERFLOWED")
        #print("\n".join(str(p) for p in pits))
        #print("OVERFLOWED END")
    
    if len(pits) == 1:
        pit = pits[0]
        pit.pitVolume = volume(pit.points, max(point.y for point in pit.points))
    
    for pit in pits:
        pit.yMin = min(point.y for point in pit.points)
    

    

        

def isolatedPits(N: int, points: list[Point], H):
    # N + 1 points.
    pits = divideIntoPits(N, points)
    for pit in pits:
        pit.calculateVolumes(H)

    #print("\n".join(str(p) for p in pits))

    overflowing(pits)

    return pits
    

def checkPits(pits: list[Pit], hMid: float):
    isLower = True
    for pit in pits:
        v = volume(pit.points, pit.yMin + hMid)
        if v < pit.waterVolume:
            isLower = False

    return isLower


def findHMax(N: int, H: float, points: list[Point]):
    pits = isolatedPits(N, points, H)

    hMin = 0
    hMax = max(p.y for p in points) - min(p.y for p in points) + H
    while hMax - hMin > eps:
        hMid = (hMax + hMin) / 2
        if checkPits(pits, hMid):
            hMax = hMid
        else:
            hMin = hMid

    return hMin


def main():
    N, H = input().split()
    N = int(N); H = float(H)
    points = []
    for _ in range(N + 1):
        x, y = (int(coord) for coord in input().split())
        points.append(Point(x, y))

    isolatedPits(N, points, H) 
    print(findHMax(N, H, points))

if __name__ == "__main__":
    main()