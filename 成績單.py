score = input("請輸入成績 ")
score = int(score)
if (score>0 and score<100):
    print("請輸入0 ~ 100的數字")
if (score>=90 and score<=100):
    print("優")
if (score>=80 and score<=89):
    print("甲")
if (score>=70 and score<=79):
    print("乙")
if (score>=60 and score<=69):
    print("丙")
if (score<60):
    print("丁")    
    