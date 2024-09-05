# 거리 계산 함수
def is_within_distance(x, y, N):
    return min(abs(x - y), N - abs(x - y)) <= 2

# 입력받기
N = int(input())  # 1부터 N까지의 숫자
a1, b1, c1 = map(int, input().split())  # 첫 번째 조합
a2, b2, c2 = map(int, input().split())  # 두 번째 조합

# 가능한 조합의 수를 저장할 변수
count = 0

# 1부터 N까지 모든 숫자 조합 탐색 (3중 for 문)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            # 첫 번째 조합과 비교하여 모든 자리가 거리 2 이내인 경우
            if (is_within_distance(i, a1, N) and
                is_within_distance(j, b1, N) and
                is_within_distance(k, c1, N)):
                count += 1
            # 두 번째 조합과 비교하여 모든 자리가 거리 2 이내인 경우
            elif (is_within_distance(i, a2, N) and
                  is_within_distance(j, b2, N) and
                  is_within_distance(k, c2, N)):
                count += 1

# 결과 출력
print(count)