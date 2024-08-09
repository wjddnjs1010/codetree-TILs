N,k = tuple(map(int,input().split()))
blocks = [0]*N

for i in range(k):
    a,b =tuple(map(int,input().split()))
    for j in range(a-1,b):
        blocks[j] +=1

print(max(blocks))