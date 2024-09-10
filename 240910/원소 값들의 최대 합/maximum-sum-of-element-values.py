def max_sum_after_moves(n, m, arr):
    max_sum = 0  # 최대 합을 저장할 변수

    # 각 시작 위치에서 움직임을 시도
    for start in range(n):
        current_pos = start  # 현재 위치
        total_sum = 0  # 현재 위치에서의 합
        
        # m번 움직임
        for _ in range(m):
            total_sum += arr[current_pos]  # 현재 위치의 값을 합산
            current_pos = arr[current_pos] - 1  # 다음 이동할 위치로 이동 (인덱스는 0부터 시작하므로 -1)
        
        # 현재 시작 위치에서의 합이 최대합보다 크면 갱신
        max_sum = max(max_sum, total_sum)
    
    return max_sum

# 입력 받기
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 결과 출력
print(max_sum_after_moves(n, m, arr))