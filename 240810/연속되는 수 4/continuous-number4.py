N = int(input())
max_count = -1
arr = [int(input()) for _ in range(N)]

for i in range(N):
    if i==0 or arr[i-1]>=arr[i]:
        count = 1
    else:
        count+=1
    max_count = max(max_count, count)
print(max_count)