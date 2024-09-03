def is_valid_jump(start_r, start_c, end_r, end_c, grid):
    # 점프가 유효한지 확인 (현재 위치보다 오른쪽 및 아래쪽으로 가야 하며 색이 달라야 함)
    return end_r > start_r and end_c > start_c and grid[start_r][start_c] != grid[end_r][end_c]

def count_paths(grid, R, C):
    count = 0
    # (1, 1)에서 출발하여 (R, C)로 가는 경로 탐색
    for r1 in range(1, R):
        for c1 in range(1, C):
            for r2 in range(r1 + 1, R + 1):
                for c2 in range(c1 + 1, C + 1):
                    if is_valid_jump(0, 0, r1 - 1, c1 - 1, grid) and is_valid_jump(r1 - 1, c1 - 1, r2 - 1, c2 - 1, grid) and is_valid_jump(r2 - 1, c2 - 1, R - 1, C - 1, grid):
                        count += 1
    return count

# 입력 받기
R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

# 경로의 수 계산
result = count_paths(grid, R, C)
print(result)