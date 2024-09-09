x,y = map(int,input().split())
count = 0
for i in range(x,y+1):
    i_str = str(i)
    for j in range(len(i_str)//2):
        if i_str[j]!=i_str[-j-1]:
            break
    else:
        count+=1

print(count)