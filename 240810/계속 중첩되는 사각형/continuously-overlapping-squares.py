n = int(input())

# 좌표평면을 초기화합니다.
plane = [[0] * 201 for _ in range(201)]

# 색칠을 시작합니다. 빨간색은 1, 파란색은 2로 표시합니다.
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    color = 2 if i % 2 == 1 else 1
    
    for x in range(x1 + 100, x2 + 100):
        for y in range(y1 + 100, y2 + 100):
            plane[x][y] = color

# 파란색 영역의 넓이를 계산합니다.
blue_area = 0
for x in range(201):
    for y in range(201):
        if plane[x][y] == 2:
            blue_area += 1

print(blue_area)