n = int(input())  # 숫자의 개수
arr = list(map(int, input().split()))  # 숫자 배열

min_diff = float('inf')  # 차이의 합의 최솟값을 저장할 변수

# 첫 번째 숫자를 2배로 만드는 루프
for i in range(n):
    # 배열 복사 후 i번째 숫자를 2배로 만든다
    arr_doubled = arr[:]
    arr_doubled[i] *= 2
    
    # 두 번째로 숫자를 제거하는 루프
    for j in range(n):
        if i == j:
            continue  # 같은 숫자를 2배로 만들고 제거할 수는 없다
        
        # j번째 숫자를 제거한 새로운 배열을 만든다
        temp_arr = arr_doubled[:j] + arr_doubled[j+1:]
        
        # 인접한 숫자들 간의 차이의 합을 계산한다
        dif_sum = 0
        for k in range(len(temp_arr) - 1):
            dif_sum += abs(temp_arr[k] - temp_arr[k+1])
        
        # 차이의 합이 더 작으면 최솟값 갱신
        min_diff = min(min_diff, dif_sum)

# 최솟값 출력
print(min_diff)