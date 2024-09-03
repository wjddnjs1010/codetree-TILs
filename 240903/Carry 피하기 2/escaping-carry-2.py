n = int(input())

arr = [int(input()) for _ in range(n)]

max_num = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            # 세 숫자를 문자열로 변환
            first_num = str(arr[i])
            second_num = str(arr[j])
            last_num = str(arr[k])
            
            # 가장 긴 숫자의 길이를 기준으로 자릿수를 맞춤
            max_len = max(len(first_num), len(second_num), len(last_num))
            
            # 자릿수가 짧은 숫자는 앞에 0을 채워서 자릿수를 맞춤
            first_num = first_num.zfill(max_len)
            second_num = second_num.zfill(max_len)
            last_num = last_num.zfill(max_len)
            
            # 각 자리의 합이 10 미만인지 확인
            valid = True
            for l in range(max_len):
                if int(first_num[l]) + int(second_num[l]) + int(last_num[l]) >= 10:
                    valid = False
                    break
            
            # 조건을 만족하는 경우 합을 계산하고 최대값 갱신
            if valid:
                num_sum = arr[i] + arr[j] + arr[k]
                max_num = max(num_sum, max_num)

# 결과 출력
if max_num:
    print(max_num)
else:
    print(-1)