N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]

def calculate_operating_time(exclude_idx):
    intervals = []
    for i in range(N):
        if i != exclude_idx:
            intervals.append(times[i])
    intervals.sort()
    
    total_time = 0
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            total_time += current_end - current_start
            current_start, current_end = start, end
    
    total_time += current_end - current_start
    return total_time

max_time = 0
for i in range(N):
    max_time = max(max_time, calculate_operating_time(i))

print(max_time)