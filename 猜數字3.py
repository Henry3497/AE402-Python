import random
num = random.randint(1, 10)
b = 0

while b <5:
    number = input("請猜1~10的數字")
    number = int(number)
    b = b + 1
    if (num == number):
        print("答對了!")
        print("猜了",b,"次")
    elif (num < number):
        print("太大了")
        print("猜了",b,"次")      
    else :
        print("太小了")
        print("猜了",b,"次")