n,t = tuple(map(int,input().split()))
max_count = -1
arr = list(map(int,input().split()))

for i in range(n):
    if arr[i]>t:
        count += 1
    else:
        count = 0
    max_count  = max(max_count, count)
print(max_count)