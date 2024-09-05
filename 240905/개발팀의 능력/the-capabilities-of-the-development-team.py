# 5명 중 2명을 선택하는 모든 조합을 직접 구현하는 함수
def get_combinations(arr, r):
    result = []
    def comb_recursive(start, chosen):
        if len(chosen) == r:
            result.append(chosen[:])
            return
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            comb_recursive(i + 1, chosen)
            chosen.pop()
    comb_recursive(0, [])
    return result

# 입력 받기
abilities = list(map(int, input().split()))

# 가능한 최소 차이를 저장할 변수 (초기값을 매우 큰 값으로 설정)
min_diff = float('inf')

# 가능한 모든 조합을 직접 구현한 get_combinations 함수를 사용해 찾기
# 5명 중 2명을 선택하여 첫 번째 팀 구성
first_team_combinations = get_combinations([0, 1, 2, 3, 4], 2)

# 첫 번째 팀을 결정한 후, 나머지 개발자로 두 번째 팀과 세 번째 팀 구성
for first_team in first_team_combinations:
    remaining_indices = [i for i in range(5) if i not in first_team]
    second_team_combinations = get_combinations(remaining_indices, 2)
    
    for second_team in second_team_combinations:
        third_team = [i for i in remaining_indices if i not in second_team]
        
        # 각 팀의 능력치 계산
        team1_sum = abilities[first_team[0]] + abilities[first_team[1]]
        team2_sum = abilities[second_team[0]] + abilities[second_team[1]]
        team3_sum = abilities[third_team[0]]  # 세 번째 팀은 한 명
        
        # 각 팀의 능력치가 서로 달라야 함
        if len(set([team1_sum, team2_sum, team3_sum])) == 3:
            # 최대 팀과 최소 팀의 차이 계산
            diff = max(team1_sum, team2_sum, team3_sum) - min(team1_sum, team2_sum, team3_sum)
            # 최소 차이를 갱신
            min_diff = min(min_diff, diff)

# 가능한 팀 구성이 없는 경우 -1 출력
if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)