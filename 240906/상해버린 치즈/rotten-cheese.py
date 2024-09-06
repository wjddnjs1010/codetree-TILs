N, M, D, S = map(int, input().split())
eat_log = []
sick_log = []

for _ in range(D):
    p, m, t = map(int, input().split())
    eat_log.append((p, m, t))

for _ in range(S):
    p, t = map(int, input().split())
    sick_log.append((p, t))

max_sick_people = 0

for cheese in range(1, M + 1):
    sick_people = set()
    possible = True
    for p, t in sick_log:
        ate_cheese = False
        for log in eat_log:
            if log[0] == p and log[1] == cheese and log[2] < t:
                ate_cheese = True
        if not ate_cheese:
            possible = False
            break

    if possible:
        for log in eat_log:
            if log[1] == cheese:
                sick_people.add(log[0])
        max_sick_people = max(max_sick_people, len(sick_people))

print(max_sick_people)