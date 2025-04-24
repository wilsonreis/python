class MyClass:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def calculate(self, value):
        return value * self.a - self.b

def main():
    mc = MyClass(2, 3)
    print(mc.a, mc.b)
    result = mc.calculate(4)
    print(result)
    mc = MyClass()
    print(mc.a, mc.b)
    result = mc.calculate(4)
    print(result)

if __name__ == '__main__':
    # execute only if run as a script
    main()

'''
__main__ -  é o nome do   escopo no qual o código do script está sendo executado.
            mas não se está sendo importado como um módulo.
 
'''