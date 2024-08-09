m1,d1,m2,d2 = tuple(map(int,input().split()))
week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

first = 0
last = 0

month = [31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(m1-1):
    first +=month[i]
first +=d1

for i in range(m2-1):
    last +=month[i]
last +=d2

target = (last-first)%7

print(week_days[target])