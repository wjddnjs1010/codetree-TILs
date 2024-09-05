n = int(input())

arr = sorted(list(map(int,input().split())))
count = 0
for i in range(n):
    for j in range(i,n):
        mean = (arr[j]+arr[i])/(j-i+1)
        for k in range(i, j+1):
            if arr[k]==mean:
                count+=1

print(count)