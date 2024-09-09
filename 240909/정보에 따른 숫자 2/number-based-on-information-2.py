t,a,b = map(int,input().split())
arr = []
for _ in range(t):
    alp, pos = input().split()
    pos = int(pos)
    arr.append((alp,pos))

count = 0

for i in range(a,b+1):
    min_d1 = float('inf')
    min_d2 = float('inf')
    for alp,pos in arr:
        if alp == 'S':
            d1 = abs(i-pos)
            min_d1 = min(min_d1,d1)
        elif alp == 'N':
            d2 = abs(i-pos)
            min_d2 = min(min_d2,d2)
    if min_d1<=min_d2:
        count+=1

print(count)