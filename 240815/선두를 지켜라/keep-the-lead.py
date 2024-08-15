n,m = tuple(map(int,input().split()))

a=[0]
b=[0]
f=[]
c=[0]*(len(a))
count = 0


for i in range(n):
    v,t = tuple(map(int,input().split()))
    for i in range(t):
        a.append(a[-1]+v)
a = a[1:]
for i in range(m):
    v,t = tuple(map(int,input().split()))
    for i in range(t):
        b.append(b[-1]+v)
b = b[1:]

for i in range(len(a)):
    if a[i]==b[i]:
        continue
    if a[i]>b[i]:
        f.append(0)
    else:
        f.append(1)

for i in range(1,len(f)):
    if f[i-1]!=f[i]:
        count+=1
print(count)