# 입력 받기
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 가장 가까운 두 점 사이의 거리의 제곱을 구하는 함수
def min_distance_squared(points):
    min_dist_sq = float('inf')  # 초기값을 무한대로 설정
    # 모든 점 쌍에 대해 거리의 제곱을 계산
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2  # 두 점 사이의 거리의 제곱
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
    return min_dist_sq

# 결과 출력
print(min_distance_squared(points))