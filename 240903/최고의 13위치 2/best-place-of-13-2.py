def count_coins(arr, x, y):
    return arr[x][y] + arr[x][y+1] + arr[x][y+2]

def is_valid_position(x, y, n):
    return y + 2 < n

def max_coins(n, arr):
    max_coins = 0
    
    for i in range(n):
        for j in range(n-2):
            if is_valid_position(i, j, n):
                first_coins = count_coins(arr, i, j)
                
                for k in range(n):
                    for l in range(n-2):
                        if is_valid_position(k, l, n):
                            # 두 격자가 겹치는지 확인
                            if i == k and (j <= l+2 and l <= j+2):
                                continue
                            second_coins = count_coins(arr, k, l)
                            max_coins = max(max_coins, first_coins + second_coins)
    
    return max_coins

# 입력
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최대 동전 개수 출력
print(max_coins(n, arr))