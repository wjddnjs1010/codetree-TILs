n = int(input())

string = input()
count = 0

for i in range(len(string)-2):
    for j in range(i+1,len(string)-1):
        for k in range(j+1,len(string)):
            if string[i] == 'C' and string[j]== 'O' and string[k]=='W':
                count+=1

print(count)