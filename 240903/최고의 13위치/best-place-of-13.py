n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]

def count_max_coins(n,mat):
    max_count = 0
    for i in range(n):
        for j in range(n-2):
            current_coins = mat[i][j] + mat[i][j + 1] + mat[i][j + 2]
            max_count = max(max_count, current_coins)
    return max_count

result = count_max_coins(n,mat)
print(result)