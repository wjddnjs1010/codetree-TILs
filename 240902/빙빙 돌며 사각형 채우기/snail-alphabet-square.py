n, m = map(int, input().split())

# 초기 설정
matrix = [[''] * m for _ in range(n)]
dx = [0, 1, 0, -1]  # 오른쪽, 아래, 왼쪽, 위
dy = [1, 0, -1, 0]

x, y = 0, 0
direction = 0  # 처음에는 오른쪽으로 이동
current_char = ord('A')  # 첫 문자 A의 ASCII 코드

# 달팽이 모양으로 알파벳 채우기
for _ in range(n * m):
    matrix[x][y] = chr(current_char)
    current_char += 1
    
    # Z를 넘어가면 다시 A로 돌아감
    if current_char > ord('Z'):
        current_char = ord('A')
    
    # 다음 위치 계산
    nx, ny = x + dx[direction], y + dy[direction]
    
    # 경계를 벗어나거나 이미 방문한 경우 방향을 변경
    if not (0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == ''):
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]
    
    x, y = nx, ny

# 출력
for row in matrix:
    print(' '.join(row))