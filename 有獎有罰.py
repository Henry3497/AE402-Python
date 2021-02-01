score1 = input("請輸入數學成績")
score2 = input("請輸入英文成績")
score1 = int(score1)
score2 = int(score2)
if (score1>90 and score2>90):
    print("有獎品")
if (score1<60 and score2>60 or score1>60 and score2<60):
    print("再加油")
if (score1<60 and score2<60):
    print("要處罰")
