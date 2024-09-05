# 입력받기
numbers = list(map(int, input().split()))  # 6명의 능력치

# 최소 차이를 저장할 변수
min_diff = float('inf')

# 6명 중 3명을 선택하여 완전 탐색
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            # 첫 번째 팀의 합
            team1_sum = numbers[i] + numbers[j] + numbers[k]
            
            # 두 번째 팀의 합은 전체 합에서 첫 번째 팀의 합을 뺀 값
            team2_sum = sum(numbers) - team1_sum
            
            # 두 팀 간의 차이 계산
            diff = abs(team1_sum - team2_sum)
            
            # 최소 차이 갱신
            min_diff = min(min_diff, diff)

# 결과 출력
print(min_diff)