x,y = input().split()
num_int = 0
for h in range(int(x),int(y)+1):
    min_count = float('inf')
    h = str(h)

    for i in range(len(h)):
        count = 0
        for j in range(len(h)):
            if i !=j and h[i]!=h[j]:
                count+=1
        min_count = min(min_count, count)
                #print(min_count)
    if min_count ==1:
        num_int+=1

print(num_int)