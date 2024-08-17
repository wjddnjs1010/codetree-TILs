n,m = tuple(map(int,input().split()))
answer = [
    [0] * n
    for _ in range(m)
]
answer[0][0] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs,dys = [0,1,0,-1],[1,0,-1,0]
dr = 0
x,y = 0,0
for i in range(2,n*m+1):
    x_nxt,y_nxt = x+dxs[dr],y+dys[dr]
    if in_range(x_nxt,y_nxt) and answer[x_nxt][y_nxt]==0:
        answer[x_nxt][y_nxt]=i
    else:
        dr =(dr+1)%4
        x_nxt,y_nxt = x+dxs[dr],y+dys[dr]
        answer[x_nxt][y_nxt]=i


    x,y = x_nxt,y_nxt


for i in range(m):
    for j in range(n):
        print(answer[i][j], end = ' ')
    print()