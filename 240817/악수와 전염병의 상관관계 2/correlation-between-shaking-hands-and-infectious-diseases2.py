N, K, P, T = map(int, input().split())

sh = [0] * N  # 각 개발자의 악수 횟수를 추적
gam = [0] * N  # 각 개발자의 감염 상태를 추적
gam[P-1] = 1  # 최초 감염자 설정

handshakes = []

# 악수 정보 입력
for _ in range(T):
    t, x, y = map(int, input().split())
    if 1 <= x <= N and 1 <= y <= N:
        handshakes.append((t, x-1, y-1))  # 0-based 인덱스로 저장

# 시간 순서대로 악수 처리
handshakes.sort()

for _, x, y in handshakes:
    if gam[x] > 0 and sh[x] < K:  # x가 전염 가능하다면
        sh[x] += 1
        gam[y] += 1

    if gam[y] > 0 and sh[y] < K:  # y가 전염 가능하다면
        sh[y] += 1
        gam[x] += 1

# 결과 출력
print(''.join(map(str, [1 if g > 0 else 0 for g in gam])))