n = int(input())

class student:
    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

students = []
for i in range(n):
    name,kor,eng,mat = input().split()
    kor = int(kor)
    eng = int(eng)
    mat = int(mat)
    students.append(student(name,kor,eng,mat))

students.sort(key = lambda student:student.kor + student.eng + student.mat)

for i in range(n):
    print(students[i].name,students[i].kor,students[i].eng,students[i].mat)