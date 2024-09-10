def max_score(N, operations):
    # 최대 점수를 구하기 위해 각 초기 위치에 따른 점수를 저장할 배열
    scores = [0, 0, 0]  # 1번, 2번, 3번 컵에 각각 초기 조약돌을 넣었을 때의 점수
    
    # 각 초기 위치에 대해 시뮬레이션
    for initial_pos in range(3):
        position = initial_pos  # 현재 조약돌 위치 (0, 1, 2 -> 1, 2, 3번 컵)
        score = 0
        
        # 각 교환을 처리
        for a, b, c in operations:
            # 인덱스는 0부터 시작하므로 a-1, b-1, c-1
            a -= 1
            b -= 1
            c -= 1
            
            # 종이컵 a와 b를 교환
            if position == a:
                position = b
            elif position == b:
                position = a
            
            # c번 컵을 열었을 때 조약돌이 그 안에 있으면 점수를 얻음
            if position == c:
                score += 1
        
        # 해당 초기 위치에서 얻은 점수를 기록
        scores[initial_pos] = score
    
    # 최대 점수를 반환
    return max(scores)

# 입력 처리
N = int(input())
operations = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_score(N, operations))