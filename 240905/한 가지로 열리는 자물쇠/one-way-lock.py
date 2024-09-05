# 입력 받기
N = int(input())  # 자물쇠 숫자의 범위
a, b, c = map(int, input().split())  # 주어진 자물쇠 조합

# 자물쇠가 열리는 조건을 만족하는 조합의 개수를 셀 변수
count = 0

# 1부터 N까지의 숫자로 3자리 조합을 모두 탐색 (완전 탐색)
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for z in range(1, N + 1):
            # 각 자리의 차이가 2 이내이면 자물쇠가 열릴 수 있음
            if abs(x - a) <= 2 or abs(y - b) <= 2 or abs(z - c) <= 2:
                count += 1

# 결과 출력
print(count)