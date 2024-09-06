n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

max_area = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k:
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                
                if (x1 == x2 and y2 == y3) or (y1 == y2 and x2 == x3):
                    area = abs((x3 - x1) * (y3 - y1))
                    max_area = max(max_area, area)

print(max_area)