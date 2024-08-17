dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
out = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = row[j]

for i in range(n):
    for j in range(n):
        count = 0
        for dx, dy in zip(dxs, dys):
            ni, nj = i + dx, j + dy
            if in_range(ni, nj, n) and arr[ni][nj] == 1:
                count += 1
        if count > 2:
            out += 1

print(out)