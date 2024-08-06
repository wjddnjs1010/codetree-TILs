n = int(input())
people = []

class person:
    def __init__(self,name,num,reg):
        self.name = name
        self.num = num
        self.reg = reg

for i in range(n):
    name, num, reg  = input().split()
    people.append(person(name,num,reg))

min_person = max(people, key = lambda person:person.name)

print('name',min_person.name)
print('addr',min_person.num)
print('city',min_person.reg)