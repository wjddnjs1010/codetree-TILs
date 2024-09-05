# 주어진 배열에서 두 명씩 3팀을 구성하여 최대 팀과 최소 팀의 합의 차이를 구하는 함수
def find_min_difference(abilities):
    min_diff = float('inf')  # 최소 차이를 저장할 변수

    # 6명의 개발자를 모두 완전 탐색으로 두 명씩 3팀을 구성
    for i in range(6):
        for j in range(i + 1, 6):
            team1_sum = abilities[i] + abilities[j]
            remaining = [k for k in range(6) if k != i and k != j]

            for m in range(4):
                for n in range(m + 1, 4):
                    team2_sum = abilities[remaining[m]] + abilities[remaining[n]]
                    team3_sum = sum(abilities) - team1_sum - team2_sum

                    max_team = max(team1_sum, team2_sum, team3_sum)
                    min_team = min(team1_sum, team2_sum, team3_sum)

                    min_diff = min(min_diff, max_team - min_team)

    return min_diff

# 입력 받기
abilities = list(map(int, input().split()))

# 결과 출력
print(find_min_difference(abilities))