code, place, time = input().split()


class test:
    def __init__(self,cd,pl,tm):
        self.cd = cd
        self.pl = pl
        self.tm = tm

test_1 = test(code,place,time)

print('secret code :', test_1.cd) 
print('meeting point :',test_1.pl)
print('time :', test_1.tm)