N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

def is_overlapping(s1, s2):
    # s1, s2가 겹치는지 확인하는 함수
    return not (s1[1] < s2[0] or s2[1] < s1[0])

non_overlapping_count = 0

for i in range(N):
    overlap = False
    for j in range(N):
        if i != j and is_overlapping(segments[i], segments[j]):
            overlap = True
            break
    if not overlap:
        non_overlapping_count += 1

print(non_overlapping_count)