from itertools import combinations

# 두 선분이 겹치는지 확인하는 함수
def is_overlapping(s1, s2):
    return not (s1[1] <= s2[0] or s2[1] <= s1[0])

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 3개의 선분을 제거할 수 있는 모든 경우를 탐색
valid_count = 0
for remove in combinations(range(n), 3):
    remaining_segments = [segments[i] for i in range(n) if i not in remove]
    overlapping = False
    
    # 남은 선분들끼리 겹치는지 확인
    for i in range(len(remaining_segments)):
        for j in range(i + 1, len(remaining_segments)):
            if is_overlapping(remaining_segments[i], remaining_segments[j]):
                overlapping = True
                break
        if overlapping:
            break
    
    # 겹치지 않으면 유효한 경우
    if not overlapping:
        valid_count += 1

print(valid_count)