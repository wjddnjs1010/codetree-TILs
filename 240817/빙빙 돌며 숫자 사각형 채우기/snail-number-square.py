n, m = tuple(map(int, input().split()))
answer = [
    [0] * m
    for _ in range(n)
]
answer[0][0] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dr = 0
x, y = 0, 0
for i in range(2, n * m + 1):
    x_nxt, y_nxt = x + dxs[dr], y + dys[dr]
    if in_range(x_nxt, y_nxt) and answer[x_nxt][y_nxt] == 0:
        answer[x_nxt][y_nxt] = i
    else:
        dr = (dr + 1) % 4
        x_nxt, y_nxt = x + dxs[dr], y + dys[dr]
        answer[x_nxt][y_nxt] = i

    x, y = x_nxt, y_nxt

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()