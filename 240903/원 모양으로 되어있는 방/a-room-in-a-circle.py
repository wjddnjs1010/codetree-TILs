def calculate_min_distance(n, people):
    min_distance = float('inf')
    
    for start in range(n):
        current_distance = 0
        
        for i in range(n):
            # i번 방까지의 거리 계산 (시작점으로부터)
            dist = (i - start + n) % n
            current_distance += dist * people[i]
        
        # 최소 거리를 갱신
        if current_distance < min_distance:
            min_distance = current_distance
    
    return min_distance

# 입력 받기
n = int(input())
people = [int(input()) for _ in range(n)]

# 최소 거리 계산
result = calculate_min_distance(n, people)
print(result)