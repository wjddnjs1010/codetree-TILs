code, color, second = input().split()

class sol:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

sol_1 = sol(code, color, second)
print('code :', sol_1.code)
print('color :', sol_1.color)
print('second :', sol_1.second)