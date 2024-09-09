n = int(input())

arr = list(map(int,input().split()))

max_count = 0

for k in range(min(arr)+1, max(arr)):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == 2*k:
                count+=1
    max_count = max(max_count,count)
print(max_count)