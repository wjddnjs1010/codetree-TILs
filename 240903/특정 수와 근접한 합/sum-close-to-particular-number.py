n, s = map(int, input().split())

min_diff = 10000  # 초기값을 큰 값으로 설정

arr = list(map(int, input().split()))
total = sum(arr)

for i in range(n):
    for j in range(i + 1, n):
        fir = arr[i]
        sec = arr[j]
        mid = total - fir - sec
        diff = abs(s - mid)
        min_diff = min(min_diff, diff)  # min_diff를 업데이트

print(min_diff)