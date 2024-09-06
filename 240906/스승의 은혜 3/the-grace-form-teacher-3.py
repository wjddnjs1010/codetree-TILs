n,b = map(int,input().split())
cost = [tuple(map(int,input().split())) for _ in range(n)]

total_cost = [cost[i][0]+cost[i][1] for i in range(n)]

total_cost.sort()
max_st = -1
for i in range(n):
    pay = sum(total_cost[:i]+total_cost[i+1:]) + cost[i][0]//2 + cost[i][1]
    if pay >b:
        max_st = max(max_st,i)
        continue
print(max_st)