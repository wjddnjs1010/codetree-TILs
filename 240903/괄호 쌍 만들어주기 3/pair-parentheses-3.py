def count_fairs(a):
    count = 0
    n = len(a)

    for i in range(n):
        if a[i] =='(':
            for j in range(i+1,n):
                if a[j] ==')':
                    count+=1
    return count

a = input()

result = count_fairs(a)
print(result)