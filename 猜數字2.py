import random #輸入模組
num = random.randint(1, 10) #比較


a = True
while a:
    number =  input("請猜1 ~ 10的數字") #輸入1~10的數字
    number = int(number) #換成整數
    if (number == num):
        print("你猜對了")
        a = False
    else:
        print("你猜錯了")    
    

