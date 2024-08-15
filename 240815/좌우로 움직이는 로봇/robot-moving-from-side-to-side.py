n,m = tuple(map(int,input().split()))

maxi = 2000000

a = [0]
b = [0]


for i in range(n):
    t,d = input().split()
    t = int(t)
    for i in range(t):
        if d=='L':
            a.append(a[-1]-1)
        else:
            a.append(a[-1]+1)
a = a[1:]
for i in range(m):
    t,d = input().split()
    t = int(t)
    for i in range(t):
        if d=='L':
            b.append(b[-1]-1)
        else:
            b.append(b[-1]+1)
b=b[1:]

count = 0

if len(a)<len(b):
    for i in range(abs(len(b)-len(a))):
        a.append(a[-1])
else:
    for i in range(abs(len(b)-len(a))):
        b.append(b[-1])
for i in range(1,len(a)):
    if a[i-1]!=b[i-1] and a[i]==b[i]:
        count+=1
print(count)