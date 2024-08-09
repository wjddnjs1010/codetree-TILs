m1,d1,m2,d2 = tuple(map(int,input().split()))
m = [31,28,31,30,31,30,31,31,30,31,30,31]
first = 0
last = 0
for i in range(m1):
    first +=m[i]
first +=d1

for i in range(m2):
    last +=m[i]
last +=d2
print(last-first)