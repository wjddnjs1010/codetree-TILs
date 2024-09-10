n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_m = float('inf')  # M의 최소값을 저장할 변수

# x축과 y축에 평행한 직선을 짝수 좌표에 하나씩 그어서 완전탐색
for x_line in range(2, 101, 2):  # 가능한 짝수 x좌표
    for y_line in range(2, 101, 2):  # 가능한 짝수 y좌표
        # 4개의 구역에 속하는 점들의 개수를 셉니다.
        quad1 = quad2 = quad3 = quad4 = 0
        
        for x, y in points:
            if x > x_line and y > y_line:
                quad1 += 1  # 1사분면 (오른쪽 위)
            elif x < x_line and y > y_line:
                quad2 += 1  # 2사분면 (왼쪽 위)
            elif x < x_line and y < y_line:
                quad3 += 1  # 3사분면 (왼쪽 아래)
            elif x > x_line and y < y_line:
                quad4 += 1  # 4사분면 (오른쪽 아래)
        
        # 각 구역의 점의 개수 중에서 최대값을 구함
        max_in_quadrant = max(quad1, quad2, quad3, quad4)
        
        # M의 최소값을 갱신
        min_m = min(min_m, max_in_quadrant)

# 결과 출력
print(min_m)