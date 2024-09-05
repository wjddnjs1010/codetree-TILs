n = int(input())

numbers = list(map(int,input().split()))

count = 0

for start in range(n):
    for end in range(start,n):
        subarray = numbers[start:end+1]

        avg = sum(subarray)/ len(subarray)

        if avg in subarray:
            count+=1

print(count)