# 두 수를 비교하여 1번 카운트와 2번 카운트를 계산하는 함수
def count_matches(a, b):
    a = str(a)
    b = str(b)
    
    count1 = 0  # 1번 카운트
    count2 = 0  # 2번 카운트
    
    for i in range(3):
        if a[i] == b[i]:
            count1 += 1
        elif b[i] in a:
            count2 += 1
    
    return count1, count2

# 입력 받기
N = int(input())  # 질문의 개수
questions = []

for _ in range(N):
    data = input().split()
    question = int(data[0])  # 묻는 숫자
    count1 = int(data[1])    # 1번 카운트
    count2 = int(data[2])    # 2번 카운트
    questions.append((question, count1, count2))

# 가능한 숫자 세 개로 구성된 모든 세 자리 수를 완전 탐색
possible_count = 0

for i in range(123, 988):  # 123부터 987까지 가능한 세 자리 수
    num_str = str(i)
    
    # 각 숫자는 서로 다른 숫자여야 함
    if len(set(num_str)) != 3:
        continue
    
    # 각 질문에 대해 조건을 만족하는지 확인
    is_possible = True
    for question, expected_count1, expected_count2 in questions:
        actual_count1, actual_count2 = count_matches(i, question)
        
        # 주어진 카운트 정보와 실제 카운트가 일치하지 않으면 후보에서 제외
        if actual_count1 != expected_count1 or actual_count2 != expected_count2:
            is_possible = False
            break
    
    if is_possible:
        possible_count += 1

# 결과 출력
print(possible_count)