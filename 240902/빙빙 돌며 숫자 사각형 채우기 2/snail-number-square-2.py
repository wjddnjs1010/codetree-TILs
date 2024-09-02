def fill_snail_matrix(n, m):
    # n * m 크기의 2차원 리스트(행렬)를 초기화합니다.
    matrix = [[0] * m for _ in range(n)]
    
    # 초기 위치와 방향 설정
    x, y = 0, 0  # 시작 위치는 (0, 0)
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]  # 아래, 오른쪽, 위쪽, 왼쪽 순서의 이동
    direction = 0  # 현재 방향 인덱스
    current_value = 1  # 채울 숫자
    
    while current_value <= n * m:
        matrix[x][y] = current_value  # 현재 위치에 숫자를 채웁니다.
        current_value += 1
        
        # 다음 위치를 미리 계산
        nx, ny = x + dx[direction], y + dy[direction]
        
        # 경계를 벗어나거나 이미 숫자가 채워진 경우 방향 전환
        if not (0 <= nx < n and 0 <= ny < m) or matrix[nx][ny] != 0:
            direction = (direction + 1) % 4  # 방향을 전환
            nx, ny = x + dx[direction], y + dy[direction]
        
        # 위치를 업데이트
        x, y = nx, ny
    
    # 결과 출력
    for row in matrix:
        print(" ".join(map(str, row)))

# 입력 예제를 처리하는 코드
n, m = map(int, input().split())
fill_snail_matrix(n, m)