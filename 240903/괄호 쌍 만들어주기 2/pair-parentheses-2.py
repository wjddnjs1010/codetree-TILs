def count_valid_pairs(A):
    count = 0
    n = len(A)
    
    for i in range(n - 3):
        if A[i] == '(' and A[i + 1] == '(':
            for j in range(i + 2, n - 1):
                if A[j] == ')' and A[j + 1] == ')':
                    count += 1
    
    return count

# 예제 입력
A = input()
print(count_valid_pairs(A))  # 출력: 4