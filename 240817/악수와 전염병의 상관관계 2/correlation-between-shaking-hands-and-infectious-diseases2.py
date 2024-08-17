# 입력값 처리
N, K, P, T = map(int, input().split())

# 악수 기록을 저장할 리스트
handshakes = []
for _ in range(T):
    t, x, y = map(int, input().split())
    handshakes.append((t, x - 1, y - 1))

# 감염 상태 및 전염 가능 횟수 초기화
infected = [0] * N
transmissions = [0] * N

# 초기 감염 설정
infected[P - 1] = 1
transmissions[P - 1] = K

# 시간 순서대로 악수 처리
for t, x, y in sorted(handshakes):
    # x가 감염되었고 전염 가능 횟수가 남아 있을 때
    if infected[x] == 1 and transmissions[x] > 0:
        if infected[y] == 0:  # y가 감염되지 않았을 때 감염시킴
            infected[y] = 1
            transmissions[y] = K
        transmissions[x] -= 1
    
    # y가 감염되었고 전염 가능 횟수가 남아 있을 때
    if infected[y] == 1 and transmissions[y] > 0:
        if infected[x] == 0:  # x가 감염되지 않았을 때 감염시킴
            infected[x] = 1
            transmissions[x] = K
        transmissions[y] -= 1

# 결과 출력
print(''.join(map(str, infected)))