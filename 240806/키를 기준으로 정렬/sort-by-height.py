class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
students = []
for i in range(n):
    name, height,weight = input().split()
    students.append(student(name,height,weight))
students.sort(key = lambda student:student.height)

for i in range(n):
    print(students[i].name,students[i].height,students[i].weight)