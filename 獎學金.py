score1 = input("請輸入數學成績") #輸入數學成績
score2 = input("請輸入英文成績") #輸入英文成績
score1 = int(score1) #換成整數
score2 = int(score2) #換成整數
if (score1>90 and score2>90): #判斷有沒有獎學金
    print("有獎學金")
elif (score1== 100 or score2== 100): #判斷有沒有獎學金
    print("有獎學金")   
else:
    print("沒有獎學金")

