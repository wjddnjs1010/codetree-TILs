N, B = map(int, input().split())
prices = [int(input()) for _ in range(N)]
prices.sort()

max_students = 0

for i in range(N):
    discounted_prices = prices[:i] + [prices[i] // 2] + prices[i+1:]
    discounted_prices.sort()
    
    total_cost = 0
    count = 0
    
    for price in discounted_prices:
        if total_cost + price <= B:
            total_cost += price
            count += 1
        else:
            break
    
    max_students = max(max_students, count)

print(max_students)