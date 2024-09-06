def min_rectangle_area(points):
    # x 좌표, y 좌표를 분리하여 리스트로 저장
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    
    # 현재 상태에서의 최소 넓이를 매우 큰 값으로 초기화
    min_area = float('inf')
    
    # 모든 점을 한 번씩 제거하고 나머지 점들로 만들 수 있는 직사각형의 넓이를 계산
    for i in range(len(points)):
        # i번째 점을 제거한 리스트를 만든다.
        x_remain = x_values[:i] + x_values[i+1:]
        y_remain = y_values[:i] + y_values[i+1:]
        
        # 나머지 점들 중 x와 y 좌표의 최대/최소값을 찾는다.
        x_min, x_max = min(x_remain), max(x_remain)
        y_min, y_max = min(y_remain), max(y_remain)
        
        # 가로와 세로 길이를 계산
        width = x_max - x_min
        height = y_max - y_min
        
        # 넓이를 계산하고 최소 넓이를 갱신
        area = width * height
        min_area = min(min_area, area)
    
    return min_area

# 입력 처리
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 최소 넓이 계산
result = min_rectangle_area(points)
print(result)