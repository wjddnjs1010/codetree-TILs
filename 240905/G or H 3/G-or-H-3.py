# 입력 받기
n, k = map(int, input().split())

# 각 사람의 위치와 팻말을 리스트로 저장
people = []
for _ in range(n):
    pos, alpha = input().split()
    pos = int(pos)
    people.append((pos, alpha))

# 위치를 기준으로 정렬
people.sort()

max_score = 0

# 모든 시작 지점을 기준으로 K 범위 안에서 구간 탐색
for i in range(n):
    current_score = 0
    # i번째 사람을 시작점으로 해서 K 범위 내에 있는 사람을 찾음
    for j in range(i, n):
        # 시작점에서 j번째 사람까지의 거리가 K 이내인 경우
        if people[j][0] - people[i][0] <= k:
            if people[j][1] == 'G':
                current_score += 1  # 'G'는 1점
            elif people[j][1] == 'H':
                current_score += 2  # 'H'는 2점
        else:
            break
    # 최대 점수 갱신
    max_score = max(max_score, current_score)

# 결과 출력
print(max_score)