class product:
    def __init__(self, name= 'codetree', code= '50'):
        self.name = name
        self.code = code


name, code = input().split()
product_1 = product()
product_2 = product(name,code)

print('product',product_1.code,'is',product_1.name)
print('product',product_2.code,'is',product_2.name)