def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def max_digit_sum(X, Y):
    max_sum = 0
    for num in range(X, Y + 1):
        max_sum = max(max_sum, digit_sum(num))
    return max_sum

# 입력 받기
X, Y = map(int, input().split())

# 결과 출력
print(max_digit_sum(X, Y))