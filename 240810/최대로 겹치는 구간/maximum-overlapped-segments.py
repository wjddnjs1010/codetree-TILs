n = int(input())

blocks = [0]*201

for i in range(n):
    x1,x2 = tuple(map(int,input().split()))
    offset = 100
    x1 +=offset
    x2 +=offset

    for j in range(x1,x2):
        blocks[j]+=1
print(max(blocks))