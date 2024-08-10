# 변수 선언 및 입력:
n = int(input())
commands = [input().strip() for _ in range(n)]

MAX_K = 100000
tiles = [0] * (2 * MAX_K + 1)  # 0: 회색, 1: 흰색, 2: 검은색
current_position = MAX_K

# 명령 처리:
for command in commands:
    x, direction = command.split()
    x = int(x)
    
    if direction == 'L':
        for i in range(x):
            position = current_position - i
            tiles[position] = 1  # 왼쪽으로 뒤집으면 흰색
        current_position -= (x - 1)
    elif direction == 'R':
        for i in range(x):
            position = current_position + i
            tiles[position] = 2  # 오른쪽으로 뒤집으면 검은색
        current_position += (x - 1)

# 결과 계산:
white_count = tiles.count(1)
black_count = tiles.count(2)

# 결과 출력:
print(white_count, black_count)