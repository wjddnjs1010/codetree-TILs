N, K, P, T = map(int, input().split())

sh = [0] * N
gam = [0] * N
gam[P-1] = 1  # Assuming P is within [1, N]
shs = []

class dev:
    def __init__(self, t, x, y):
        self.t = t
        self.x = x
        self.y = y

for i in range(T):
    t, x, y = map(int, input().split())
    if 1 <= x <= N and 1 <= y <= N:
        shs.append(dev(t, x, y))

shs.sort(key=lambda dev: dev.t)

for j in range(T):
    if 1 <= shs[j].x <= N and 1 <= shs[j].y <= N:
        if gam[shs[j].x-1] > 0:
            sh[shs[j].x-1] += 1
            if sh[shs[j].x-1] <= K:
                gam[shs[j].y-1] += 1

        if gam[shs[j].y-1] > 0:
            sh[shs[j].y-1] += 1
            if sh[shs[j].y-1] <= K:
                gam[shs[j].x-1] += 1

out = [0] * N
for i in range(N):
    if gam[i] > 0:
        out[i] = 1

print(''.join(map(str, out)))