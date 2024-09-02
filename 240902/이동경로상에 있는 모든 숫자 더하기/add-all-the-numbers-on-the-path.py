# 입력 받기
N, T = map(int, input().split())
commands = input().strip()
grid = [list(map(int, input().split())) for _ in range(N)]

# 초기 위치와 방향 설정 (북쪽)
x, y = N // 2, N // 2
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서
current_direction = 0

# 초기 위치의 숫자 더하기
total_sum = grid[x][y]

# 명령어 처리
for command in commands:
    if command == 'L':
        current_direction = (current_direction - 1) % 4
    elif command == 'R':
        current_direction = (current_direction + 1) % 4
    elif command == 'F':
        # 이동
        nx = x + directions[current_direction][0]
        ny = y + directions[current_direction][1]
        
        # 격자 범위를 벗어나지 않으면 이동
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            total_sum += grid[x][y]

# 결과 출력
print(total_sum)