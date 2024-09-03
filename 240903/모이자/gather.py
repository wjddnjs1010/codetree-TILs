n = int(input())
a = list(map(int,input().split()))

def calculate_distance(target_house):
    total_distance = 0
    for i in range(n):
        total_distance +=abs(i-target_house)*a[i]
    return total_distance

min_distance = float('inf')
for target_house in range(n):
    min_distance = min(min_distance,calculate_distance(target_house))

print(min_distance)