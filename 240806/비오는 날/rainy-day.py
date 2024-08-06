n = int(input())
arr = []
weathers = []
class weather:
    def __init__(self,date,day,fore):
        self.date = date
        self.day = day
        self.fore = fore

for i in range(n):
    date, day, fore =  input().split()
    weathers.append(weather(date,day,fore))

arr = [word for word in weathers if word.fore == 'Rain']

min_arr = min(arr, key = lambda weather:weather.date)

print(min_arr.date,min_arr.day,min_arr.fore)