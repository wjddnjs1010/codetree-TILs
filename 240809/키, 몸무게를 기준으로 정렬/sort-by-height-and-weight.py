class person:
    def __init__(self,name,height,weight):
        self.name  = name
        self.height = height
        self.weight = weight
n = int(input())
people = []

for i in range(n):
    name,height,weight = input().split()
    height = int(height)
    weight = int(weight)
    people.append(person(name,height,weight))

people.sort(key = lambda person:(person.height,-person.weight))
for i in range(n):
    print(people[i].name,people[i].height,people[i].weight)