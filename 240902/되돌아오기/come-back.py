N = int(input())

directions = [input().split() for _ in range(N)]
dx = {'N':0,'E':1,'S':0,'W':-1}
dy = {'N':1,'E':0,'S':-1,'W':0}

x,y = 0,0
tm =0

for i in range(N):
    direction, num = directions[i]
    num = int(num)
    for _ in range(num):
        x+=dx[direction]
        y+=dy[direction]
        tm+=1
        if (x,y)==(0,0):
            print(tm)
            exit()

print(-1)