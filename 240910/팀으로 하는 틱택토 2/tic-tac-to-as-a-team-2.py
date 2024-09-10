# 보드 입력 받기
board = [input() for _ in range(3)]

# 8가지의 이길 수 있는 줄(3개의 가로줄, 3개의 세로줄, 2개의 대각선)
lines = [
    board[0],  # 가로 1번째 줄
    board[1],  # 가로 2번째 줄
    board[2],  # 가로 3번째 줄
    board[0][0] + board[1][0] + board[2][0],  # 세로 1번째 줄
    board[0][1] + board[1][1] + board[2][1],  # 세로 2번째 줄
    board[0][2] + board[1][2] + board[2][2],  # 세로 3번째 줄
    board[0][0] + board[1][1] + board[2][2],  # 대각선 1
    board[0][2] + board[1][1] + board[2][0]   # 대각선 2
]

team_wins = 0  # 팀이 이긴 경우의 수

# 각 줄에 대해 팀으로 이길 수 있는지 확인
for line in lines:
    unique_digits = set(line)  # 한 줄의 숫자를 집합으로 변환하여 중복을 제거
    if len(unique_digits) == 2:  # 서로 다른 숫자가 2개일 때 팀 승리 가능
        team_wins += 1

# 결과 출력
print(team_wins)