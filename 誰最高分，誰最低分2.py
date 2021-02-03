people = input("班上有多少學生") #輸入班上有多少人
people = int(people) #換為整數
highest = 0 #建立最高分預設值0
lowest = 100 #建立最低分預設值100
highestname = "" #建立最高分同學姓名
lowestname = "" #建立最低分同學姓名
score = list() #建立score空陣列 紀錄數學成
name = list() #建立name空陣列 紀錄同學姓名
summath = 0 #建立總成績參數summath
for i in range (people): #根據input得到的people
    mathname = input("name?")
    mathscore = input("幾分?")
    mathscore = int(mathscore)
    name.append(mathname) #將該同學的姓名加入陣列
    score.append(mathscore) #將該同學的成績加入陣列
    if highest<mathscore: #判斷目前最高分是哪一個
        highest = mathscore #如果是? 取代最高分
        highestname = mathname 
    if lowest>mathscore:
       lowest = mathscore
       lowestname = mathname
    summath = summath + mathscore

print(highestname,lowestname,score)
print("班上最高",highest,"是",highestname)
print("班上最低", lowest, "是" , lowestname)
print("班上平均",summath/people)    




