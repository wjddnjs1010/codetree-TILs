K, N = map(int, input().split())
rankings = [list(map(int, input().split())) for _ in range(K)]

count = 0

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            continue
        always_higher = True
        for ranking in rankings:
            if ranking.index(a) > ranking.index(b):
                always_higher = False
                break
        if always_higher:
            count += 1

print(count)