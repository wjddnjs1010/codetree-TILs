N = int(input())
arr = list(map(int,input().split()))
class person:
    def __init__(self,data,num,out=0):
        self.data = data
        self.num = num
        self.out = out
people = []
for i in range(N):
    people.append(person(arr[i],i+1))

people.sort(key = lambda person:(person.data,person.num))

for i in range(N):
    people[i].out = i+1

people.sort(key = lambda person:person.num)

for i in range(N):
    print(people[i].out, end = ' ')