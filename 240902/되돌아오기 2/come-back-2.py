string = input().strip()
N = len(string)

directions = [(0,1),(1,0),(0,-1),(-1,0)]

x,y = 0,0
current_direction = 0
tm = 0

for st in string:
    if st == 'L':
        current_direction = (current_direction-1)%4
    elif st =='R':
        current_direction = (current_direction+1)%4
    elif st =='F':
        x+=directions[current_direction][0]
        y+=directions[current_direction][1]
    tm+=1
    if (x,y)==(0,0):
        print(tm)
        exit()

print(-1)