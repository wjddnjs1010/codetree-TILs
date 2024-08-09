N = int(input())

class person:
    def __init__(self,height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

people = []

for i in range(N):
    height,weight = tuple(map(int,input().split()))
    people.append(person(height,weight,i+1))

people.sort(key = lambda person:(person.height,-person.weight))

for i in range(N):
    print(people[i].height,people[i].weight,people[i].num )