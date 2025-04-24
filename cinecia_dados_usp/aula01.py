nome = "Wilson dos Reis"
print(f"Oi, meu nome é {nome} ")
print("1")
print("2")
print("3")

print("4", end=" ")
print("5", end=" ")
print("6", end=" ")

with open("wilson.txt", "w") as file:
    print("wilson pro arquivo", file=file)
print("\n")
#variavel = input("Digite algo: ")
#print(variavel)
import time
n = 10
while(n > -1):
    print(n, end=" ")
    n -= 1
    #time.sleep(1)

print()


for i in range(10, -1, -1):
    print(i, end=" ")
    #time.sleep(1)

'''
start: [ optional ] start value of the sequence
stop: next value after the end value of the sequence
step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
'''
print("\n--------")
for i in range(11):
    print(i, end=" ")