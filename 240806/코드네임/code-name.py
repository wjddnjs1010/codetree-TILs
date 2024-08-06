class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = []

for i in range(5):
    name, score = input().split()
    score = int(score)
    students.append(student(name,score))


min_score_student = min(students, key = lambda agent: agent.score)

print(min_score_student.name, min_score_student.score)