# 입력 받기
N, H, T = map(int, input().split())  # N: 밭의 개수, H: 목표 높이, T: 연속 구간의 길이
heights = list(map(int, input().split()))  # 밭의 높이 정보

# 최소 비용을 저장할 변수, 처음엔 매우 큰 값으로 초기화
min_cost = float('inf')

# 슬라이딩 윈도우로 길이 T의 모든 구간을 확인
for i in range(N - T + 1):
    current_cost = 0
    # 구간 [i, i+T-1]의 밭 높이를 목표 높이 H로 맞추기 위한 비용 계산
    for j in range(i, i + T):
        current_cost += abs(heights[j] - H)
    
    # 최소 비용 갱신
    min_cost = min(min_cost, current_cost)

# 결과 출력
print(min_cost)