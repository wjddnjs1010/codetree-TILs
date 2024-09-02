def shoot_laser(N, grid, K):
    # dx, dy 배열은 각각 상하좌우 방향을 의미합니다.
    # dx = [-1, 1, 0, 0], dy = [0, 0, -1, 1] 순서대로
    # 상, 하, 좌, 우 방향을 나타냅니다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # K에 따라 레이저의 시작 위치와 방향을 설정합니다.
    if 1 <= K <= N:
        x, y, d = 0, K-1, 1
    elif N+1 <= K <= 2*N:
        x, y, d = K-N-1, N-1, 2
    elif 2*N+1 <= K <= 3*N:
        x, y, d = N-1, 3*N-K, 0
    else:
        x, y, d = 4*N-K, 0, 3
    
    count = 0
    
    while 0 <= x < N and 0 <= y < N:
        count += 1
        if grid[x][y] == '/':
            if d == 0: d = 3
            elif d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 0
        elif grid[x][y] == '\\':
            if d == 0: d = 2
            elif d == 1: d = 3
            elif d == 2: d = 0
            elif d == 3: d = 1
        
        x += dx[d]
        y += dy[d]
    
    return count

# 입력 예제
N = int(input())
grid = [input().strip() for _ in range(N)]
K = int(input())

# 결과 출력
print(shoot_laser(N, grid, K))