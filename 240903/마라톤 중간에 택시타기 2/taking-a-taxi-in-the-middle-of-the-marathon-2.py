def calculate_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_min_distance(checkpoints):
    n = len(checkpoints)
    
    # 전체 경로의 거리를 먼저 계산합니다.
    total_distance = 0
    for i in range(n - 1):
        total_distance += calculate_distance(checkpoints[i], checkpoints[i + 1])
    
    # 한 개의 체크포인트를 건너뛰었을 때의 최소 거리 계산
    min_distance = float('inf')
    for i in range(1, n - 1):  # 첫 번째와 마지막은 건너뛰지 않으므로 1부터 n-2까지
        # i번째 체크포인트를 건너뛰었을 때의 거리 계산
        skipped_distance = total_distance - (calculate_distance(checkpoints[i-1], checkpoints[i]) + calculate_distance(checkpoints[i], checkpoints[i+1])) + calculate_distance(checkpoints[i-1], checkpoints[i+1])
        min_distance = min(min_distance, skipped_distance)
    
    return min_distance

# 입력 받기
n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

# 최소 거리 계산 후 출력
result = find_min_distance(checkpoints)
print(result)