x,y = 0,0

n = int(input())
direc = ['E','W','S','N']
dx,dy = [1,-1,0,0], [0,0,-1,1]

for i in range(n):
    d,s = input().split()
    s = int(s)
    for i in range(4):
        if d == direc[i]:
            x = x+s*dx[i]
            y = y+s*dy[i]
print(x,y)