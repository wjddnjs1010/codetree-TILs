n = int(input())

# 초기 설정
matrix = [[0] * n for _ in range(n)]
dx = [0, -1, 0, 1]  # 오른쪽, 위, 왼쪽, 아래
dy = [1, 0, -1, 0]

# 시작점 설정
x, y = n // 2, n // 2
direction = 0  # 처음에는 오른쪽으로 이동
current_num = 1

# 숫자 채우기
for _ in range(n * n):
    matrix[x][y] = current_num
    current_num += 1
    
    # 다음 위치 계산
    nx, ny = x + dx[direction], y + dy[direction]
    
    # 경계를 벗어나거나 이미 방문한 경우 방향을 변경
    if not (0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0):
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]
    
    x, y = nx, ny

# 출력
for row in matrix:
    print(' '.join(map(str, row)))