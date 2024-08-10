# 입력을 받아 처리합니다.
N = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(N)]

# 평면의 크기를 201x201로 정의하고, 모두 0으로 초기화합니다.
# 각 좌표는 -100부터 100까지의 범위를 가지므로, 이를 0부터 200까지의 범위로 변환하여 사용합니다.
plane = [[0] * 201 for _ in range(201)]

# 각 직사각형의 범위를 plane 배열에 표시합니다.
for x1, y1, x2, y2 in rectangles:
    for i in range(x1 + 100, x2 + 100):
        for j in range(y1 + 100, y2 + 100):
            plane[i][j] = 1

# plane 배열에서 1로 표시된 영역의 수를 셉니다.
total_area = sum(sum(row) for row in plane)

# 결과 출력
print(total_area)