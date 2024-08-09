a,b,c = tuple(map(int,input().split()))

first = 0
last = 0

first = 11*24*60+11*60+11
last = a*24*60+b*60+c

if first>last:
    print(-1)
else:
    print(last-first)