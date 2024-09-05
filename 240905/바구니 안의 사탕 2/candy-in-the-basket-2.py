# 입력 받기
N, K = map(int, input().split())  # N: 바구니 개수, K: 구간의 반경
candies = []

# N개의 바구니 정보 입력받기
for _ in range(N):
    count, position = map(int, input().split())  # 사탕 개수와 바구니 위치
    candies.append((count, position))

# 최대 사탕 수를 저장할 변수
max_candies = 0

# 중심점 c를 0부터 100까지 시도
for c in range(101):
    # 구간 [c-K, c+K] 내에 있는 사탕 수 계산
    current_candies = 0
    for count, position in candies:
        if c - K <= position <= c + K:
            current_candies += count
    # 최대값 갱신
    max_candies = max(max_candies, current_candies)

# 결과 출력
print(max_candies)