N, M = map(int, input().split())

# A와 B의 이동 기록을 저장할 리스트
A_moves = []
B_moves = []

# A의 이동 정보 입력
for _ in range(N):
    d, t = input().split()
    A_moves.append((d, int(t)))

# B의 이동 정보 입력
for _ in range(M):
    d, t = input().split()
    B_moves.append((d, int(t)))

# 위치 기록을 저장할 딕셔너리
A_positions = {}
B_positions = {}

# A의 이동 기록
cur_position = 0
cur_time = 0
for d, t in A_moves:
    for _ in range(t):
        if d == 'R':
            cur_position += 1
        else:
            cur_position -= 1
        cur_time += 1
        A_positions[cur_time] = cur_position

# B의 이동 기록
cur_position = 0
cur_time = 0
for d, t in B_moves:
    for _ in range(t):
        if d == 'R':
            cur_position += 1
        else:
            cur_position -= 1
        cur_time += 1
        B_positions[cur_time] = cur_position

# 최초로 만나는 시간 찾기
meeting_time = -1
for time in range(1, max(len(A_positions), len(B_positions)) + 1):
    if time in A_positions and time in B_positions and A_positions[time] == B_positions[time]:
        meeting_time = time
        break

print(meeting_time)