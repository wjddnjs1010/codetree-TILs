def find_min_unique_substring_length(s):
    n = len(s)
    
    # 1부터 n까지의 길이로 부분 문자열을 검사
    for length in range(1, n + 1):
        seen_substrings = set()  # 이미 본 부분 문자열을 저장할 집합
        
        for i in range(n - length + 1):
            substring = s[i:i + length]  # 길이 length의 부분 문자열 추출
            
            if substring in seen_substrings:
                break  # 중복이 발생하면 다음 길이로 이동
            seen_substrings.add(substring)
        else:
            # break가 발생하지 않고 정상적으로 탐색이 끝났다면, 이 길이가 답이다
            return length

# 입력 받기
n = int(input())  # 문자열의 길이
s = input()  # 주어진 문자열

# 결과 출력
print(find_min_unique_substring_length(s))