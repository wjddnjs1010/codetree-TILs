N =int(input())
max_num=-1
num=0
arr = []
for i in range(N):
    curr = int(input())
    arr.append(curr)

for i in range(N):
    if i==0 or arr[i-1]!=arr[i]:
        num=1
    elif arr[i]==arr[i-1]:
        num+=1
    max_num = max(max_num,num)
print(max_num)