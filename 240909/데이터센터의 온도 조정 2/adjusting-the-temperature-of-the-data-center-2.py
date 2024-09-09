n,c,g,h = map(int,input().split())

arr = [tuple(map(int,input().split())) for _ in range(n)]
max_work = 0
for cur_tem in range(0,1001):
    work = 0
    for ta,tb in arr:
        if cur_tem < ta:
            work += c
        elif cur_tem > tb:
            work +=h
        else:
            work +=g
    max_work = max(max_work, work)

print(max_work)