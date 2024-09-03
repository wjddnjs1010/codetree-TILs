n = int(input())
arr = list(map(int,input().split()))
max_sum = 0
for i in range(n-1):
    first_number = arr[i]
    for j in range(i+2,n):
        second_number = arr[j]
        sum = first_number + second_number
        max_sum = max(max_sum,sum)

print(max_sum)