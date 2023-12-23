def main():
    K = int(input())
    cells = []
    xmin = ymin = int(1e9 + 1)
    xmax = ymax = -int(1e9 + 1)

    for _ in range(K):
        x, y = map(int, input().split())
        
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
        
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
    
    print(xmin, ymin, xmax, ymax)
        


if __name__ == "__main__":
    main()