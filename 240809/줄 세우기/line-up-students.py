class student:
    def __init__(self,height,weight,num):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())
students = []
for i in range(n):
    height,weight = tuple(map(int,input().split()))
    students.append(student(height,weight,i+1))
students.sort(key = lambda student:(-student.height, -student.weight, student.num))


for i in range(n):
    print(students[i].height,students[i].weight,students[i].num)