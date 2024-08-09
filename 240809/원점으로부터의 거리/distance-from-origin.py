N = int(input())
people = []

class person:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num
for i in range(N):
    x,y = tuple(map(float,input().split()))
    people.append(person(x,y,i+1))

people.sort(key = lambda person:(abs(person.x)+abs(person.y)))

for i in range(N):
    print(people[i].num)