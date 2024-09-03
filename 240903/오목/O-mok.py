# 방향을 정의: 오른쪽, 아래쪽, 대각선 아래-오른쪽, 대각선 아래-왼쪽
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

def find_winner(board):
    for i in range(19):
        for j in range(19):
            if board[i][j] != 0:
                current_stone = board[i][j]
                
                for direction in directions:
                    dx, dy = direction
                    count = 1
                    nx, ny = i + dx, j + dy
                    
                    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == current_stone:
                        count += 1
                        if count == 5:
                            # 다음 위치가 바둑알의 연속인지 확인하여 6목 방지
                            if 0 <= nx + dx < 19 and 0 <= ny + dy < 19 and board[nx + dx][ny + dy] == current_stone:
                                break
                            # 이전 위치가 바둑알의 연속인지 확인하여 6목 방지
                            if 0 <= i - dx < 19 and 0 <= j - dy < 19 and board[i - dx][j - dy] == current_stone:
                                break
                            # 승리한 경우
                            return current_stone, i + 1 + 2 * dx, j + 1 + 2 * dy
                        nx += dx
                        ny += dy
    return 0, 0, 0

# 입력 받기
board = [list(map(int, input().split())) for _ in range(19)]

# 승리자 찾기
winner, x, y = find_winner(board)

# 출력
print(winner)
if winner != 0:
    print(x, y)