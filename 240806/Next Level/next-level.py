id_i, lv_i = input().split()

class ch:
    def __init__(self, idy = 'codetree', lv = '10'):
        self.idy = idy
        self.lv = lv
ch_2 = ch()
ch_1 = ch(id_i,lv_i)

print('user',ch_2.idy,'lv',ch_2.lv)
print('user',ch_1.idy,'lv',ch_1.lv)