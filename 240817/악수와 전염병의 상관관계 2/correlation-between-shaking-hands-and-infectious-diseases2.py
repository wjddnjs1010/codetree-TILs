N, K, P, T = tuple(map(int,input().split()))

sh = [0]*N
gam = [0]*N
gam[P-1] = 1
shs = []

class dev:
    def __init__(self,t,x,y):
        self.t = t
        self.x = x
        self.y = y

for i in range(T):
    t,x,y = tuple(map(int,input().split()))
    shs.append(dev(t,x,y))
shs.sort(key = lambda dev:dev.t)

for j in range(T):
    if gam[shs[j].x-1] > 0:
        sh[shs[j].x-1]+=1
        if sh[shs[j].x-1]<=K:
            gam[shs[j].y-1]+=1

    if gam[shs[j].y-1]>0:
        sh[shs[j].y-1]+=1
        if sh[shs[j].y-1]<=K:
            gam[shs[j].x-1]+=1


j=0
shs[0].x-1
out = [0]*N
for i in range(N):
    if gam[i]>0:
        out[i]=1

print(''.join(map(str,out)))

'''
P = 2
gam = 0100
x = 2 y = 3
if gam[devs[j].(x-1)]>1:
    sh[devs[j].(x-1)]+=1
    if sh[devs[j].(x-1)]<K:
        gam[devs[j].(y-1)]+=1

if gam[devs[j].(y-1)]>1:
    sh[devs[j].(y-1)]+=1
    if sh[devs[j].(y-1)]<K:
        gam[devs[j].(x-1)]+=1
sh = 0100
gam = 0110
x = 2 y = 4
sh = 0200
gam = 0111
x = 1 y = 2
sh = 0300
gam = 0111

gam,sh
0100

0110
0100
0111
0200
0111
03
'''