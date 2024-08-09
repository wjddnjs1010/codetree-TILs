def count_specific_weekday(m1, d1, m2, d2, target_weekday):
    # 각 월의 일수를 저장하는 리스트 (2024년은 윤년)
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 요일을 저장하는 리스트
    week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # 특정 요일의 인덱스 찾기
    target_index = week_days.index(target_weekday)
    
    # 첫 번째 날짜와 두 번째 날짜를 일수로 변환
    def date_to_days(month, day):
        return sum(month_days[:month-1]) + day
    
    start_day_count = date_to_days(m1, d1)
    end_day_count = date_to_days(m2, d2)
    
    # 시작 요일 계산 (2024년 1월 1일은 월요일)
    start_weekday_index = (start_day_count - 1) % 7
    
    # 특정 요일 등장 횟수 계산
    count = 0
    for day in range(start_day_count, end_day_count + 1):
        if (start_weekday_index % 7) == target_index:
            count += 1
        start_weekday_index += 1
    if start_day_count-end_day_count ==0 and target_index ==0:
        count = 1
    return count

# 사용자로부터 입력 받기
m1, d1, m2, d2 = map(int, input().split())
target_weekday = input().strip()

# 함수 호출 및 결과 출력
result = count_specific_weekday(m1, d1, m2, d2, target_weekday)
print(result)