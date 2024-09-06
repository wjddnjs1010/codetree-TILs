def max_students(N, B, gifts):
    # 각 학생의 선물 가격과 배송비 합을 계산
    total_costs = [P + S for P, S in gifts]

    # 선물에 쿠폰을 적용했을 때의 비용을 계산
    coupon_applied_costs = [(P // 2) + S for P, S in gifts]

    # 정답을 저장할 변수
    max_count = 0

    # 각 학생에 대해 쿠폰을 적용한 경우를 탐색
    for i in range(N):
        # i번째 학생에게 쿠폰을 적용했을 때
        costs_with_coupon = total_costs[:]
        costs_with_coupon[i] = coupon_applied_costs[i]
        
        # 총 비용을 오름차순 정렬
        costs_with_coupon.sort()
        
        # 예산 내에서 가능한 최대 학생 수를 계산
        current_budget = B
        current_count = 0
        for cost in costs_with_coupon:
            if current_budget >= cost:
                current_budget -= cost
                current_count += 1
            else:
                break
        
        # 최대 학생 수 업데이트
        max_count = max(max_count, current_count)
    
    return max_count

# 입력 처리
N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_students(N, B, gifts))