A, B, C = map(int, input().split())  # 입력 받기

max_value = 0  # 만들 수 있는 최대값을 저장할 변수

# A를 0번부터 가능한 최대 횟수인 C//A번까지 더한 값에 대해 탐색
for i in range(C // A + 1):
    # A를 i번 더한 값
    a_sum = A * i
    # B를 0번부터 가능한 최대 횟수인 C//B번까지 더한 값에 대해 탐색
    for j in range(C // B + 1):
        # A를 i번 더하고 B를 j번 더한 값
        b_sum = B * j
        total_sum = a_sum + b_sum
        # 합이 C 이하일 경우 최댓값 갱신
        if total_sum <= C:
            max_value = max(max_value, total_sum)

print(max_value)  # 최종 결과 출력