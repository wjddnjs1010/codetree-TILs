# 입력 받기
n = int(input().strip())
commands = [input().strip() for _ in range(n)]

# 초기 위치와 방문 카운트
current_position = 0
visit_count = {}

# 명령 수행
for command in commands:
    x, direction = command.split()
    x = int(x)
    
    if direction == 'R':
        for i in range(current_position, current_position + x):
            if i not in visit_count:
                visit_count[i] = 0
            visit_count[i] += 1
        current_position += x
    elif direction == 'L':
        for i in range(current_position - 1, current_position - x - 1, -1):
            if i not in visit_count:
                visit_count[i] = 0
            visit_count[i] += 1
        current_position -= x

# 2번 이상 지나간 영역의 크기 계산
count = 0
for key in visit_count:
    if visit_count[key] >= 2:
        count += 1

# 결과 출력
print(count)