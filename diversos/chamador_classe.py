from classe import MyClass  # Importe a classe MyClass

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
    main()