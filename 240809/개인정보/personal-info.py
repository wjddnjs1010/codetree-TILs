class person:
    def __init__(self,name,height,weight):
        self.name  = name
        self.height = height
        self.weight = weight

people = []

for i in range(5):
    name,height,weight = input().split()
    height = int(height)
    weight = float(weight)
    people.append(person(name,height,weight))
people.sort(key = lambda person:person.name)
print('name')
for i in range(5):
    print(people[i].name,people[i].height,people[i].weight)

print()
print('height')
people.sort(key = lambda person:-person.height)
for i in range(5):
    print(people[i].name,people[i].height,people[i].weight)