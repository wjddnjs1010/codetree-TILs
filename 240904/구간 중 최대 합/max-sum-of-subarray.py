n,k = map(int,input().split())

arr = list(map(int,input().split()))
arr_max = 0
for i in range(n):
    arr_cur = 0
    for j in range(i,i+k):
        if i+k<n:
            arr_cur += arr[j]
            arr_max = max(arr_max, arr_cur)

print(arr_max)