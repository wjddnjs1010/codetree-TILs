n,m = (map(int,input().split()))

grid = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def is_comfortable(x,y):
    count =0
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and grid[xx][yy]==1:
            count+=1
    return count==3

for _ in range(m):
    r,c = map(int,input().split())
    r-=1
    c-=1

    grid[r][c] =1
    if is_comfortable(r,c):
        print(1)
    else:
        print(0)