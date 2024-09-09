x,y = input().split()
num_int = 0
for h in range(int(x),int(y)+1):
    count = 0
    
    h = str(h)
    for i in range(len(h)):
        for j in range(i+1,len(h)):
            if h[i]==h[j]:
                count+=1
    if count ==1:
        num_int+=1

print(num_int)