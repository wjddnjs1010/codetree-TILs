n = int(input())
arr = [int(input()) for _ in range(n)]
max_num = -1
for i in range(n):
    if i==0 or arr[i-1]*arr[i]<0:
        num =1
    else:
        num+=1
    max_num = max(max_num, num)

print(max_num)



#1. arr[i]<0, arr[i] > 0 구분
#2.