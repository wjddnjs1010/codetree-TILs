# 8방향 설정: 상하좌우, 대각선
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

n, m = map(int, input().split())

# n x m 크기의 문자열 격자 입력 받기
mat = [input().strip() for _ in range(n)]

# 'LEE'의 개수를 저장할 변수
count = 0

# 각 위치를 순회하며 'L'을 찾습니다.
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'L':  # 'L'을 찾았을 때만 탐색 시작
            for direction in directions:
                dx, dy = direction
                x, y = i + dx, j + dy
                x2, y2 = i + 2*dx, j + 2*dy
                
                # 'L' 다음 두 글자가 'EE'인지 확인
                if 0 <= x < n and 0 <= y < m and 0 <= x2 < n and 0 <= y2 < m:
                    if mat[x][y] == 'E' and mat[x2][y2] == 'E':
                        count += 1

# 결과 출력
print(count)