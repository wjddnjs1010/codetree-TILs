def count_valid_triplets(n,heights):
    count = 0

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if heights[i]<=heights[j] and heights[j]<=heights[k]:
                    count+=1
    return count

n = int(input())
heights = list(map(int,input().split()))

result = count_valid_triplets(n,heights)
print(result)