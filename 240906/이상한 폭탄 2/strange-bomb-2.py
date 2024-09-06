n,k = map(int,input().split())

arr = [int(input()) for _ in range(n)]
max_num = -1
for i in range(n):
    for j in range(i+1,n):
        if arr[i] ==arr[j] and j-i<=k:
            num = arr[i]
            max_num = max(max_num,num)

print(max_num)