# 입력 받기
N = int(input())  # 사람 수
people = []

for _ in range(N):
    position, sign = input().split()
    position = int(position)
    people.append((position, sign))

# 위치를 기준으로 정렬 (위치 순으로 확인할 수 있게)
people.sort()

max_distance = 0

# 모든 구간 탐색
for start in range(N):
    g_count = 0
    h_count = 0
    for end in range(start, N):
        if people[end][1] == 'G':
            g_count += 1
        else:
            h_count += 1

        # 조건 1: G만 있는 구간
        if h_count == 0 or g_count == 0:
            # 구간 내에 G만 있거나 H만 있는 경우
            if start != end:
                distance = people[end][0] - people[start][0]
                max_distance = max(max_distance, distance)
        
        # 조건 2: G와 H의 개수가 같은 구간
        if g_count == h_count:
            # G와 H의 개수가 같을 때
            distance = people[end][0] - people[start][0]
            max_distance = max(max_distance, distance)

# 결과 출력
print(max_distance)