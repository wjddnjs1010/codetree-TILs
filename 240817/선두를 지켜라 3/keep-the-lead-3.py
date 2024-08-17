first = []
count = 1
a = []
b = []
n,m = tuple(map(int,input().split()))

for i in range(n):
    v,t = tuple(map(int,input().split()))
    for j in range(t):
        if len(a)==0:
            a.append(v)
        else:
            a.append(a[-1]+v)

for i in range(m):
    v,t = tuple(map(int,input().split()))
    for j in range(t):
        if len(b)==0:
            b.append(v)
        else:
            b.append(b[-1]+v)

for i in range(len(a)):
    if a[i]>b[i]:
        first.append(0)
    elif a[i]<b[i]:
        first.append(1)
    else:
        first.append(2)

for i in range(1,len(first)):
        if first[i-1]!=first[i]:
            count+=1

print(count)