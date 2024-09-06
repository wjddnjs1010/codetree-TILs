N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]

def is_overlapping(seg1, seg2):
    return not (seg1[1] <= seg2[0] or seg2[1] <= seg1[0])

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