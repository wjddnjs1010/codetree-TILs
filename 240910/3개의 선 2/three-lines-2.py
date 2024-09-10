from itertools import combinations

# 좌표를 커버하는지 확인하는 함수
def is_covered(points, lines, axis):
    for x, y in points:
        if axis == 'x':
            if x not in lines:
                return False
        else:
            if y not in lines:
                return False
    return True

# 입력 받기
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 가능한 x 값과 y 값을 추출
x_values = set([x for x, y in points])
y_values = set([y for x, y in points])

# x축 평행선 3개로 커버 가능한지 확인
for x_lines in combinations(x_values, 3):
    if is_covered(points, x_lines, 'x'):
        print(1)
        exit()

# y축 평행선 3개로 커버 가능한지 확인
for y_lines in combinations(y_values, 3):
    if is_covered(points, y_lines, 'y'):
        print(1)
        exit()

# 둘 다 불가능하면 0 출력
print(0)