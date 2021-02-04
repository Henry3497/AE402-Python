import os.path


if os.path.isfile("myfile.txt"):
    print("檔案存在")
else:
    print("檔案不存在")
    
english = {}

print("################")
print("#歡迎進入本系統")
print("################")
print("***使用本系統，你將會成為英文高手***")

while True:
    print("=>")
    print("1.建立詞彙")
    print("2.列出所有單字")
    print("3.英翻中")
    print("4.中翻英")
    print("5.測驗學習成果")
    print("6.離開系統")

    sel = input("請輸入欲直行選項")

    if sel=="1":
        while True:
            voc = input("輸入新單字(按0跳出)")
            if voc == "0":
                break
            if voc not in english:
                m = input("輸入中文解釋")
                english[voc] = m
            else:
                print("單字已經存在")
    elif sel == "2":
         lk = sorted(english)
         for  item in lk:
             print(item,"是",english[item])
    elif sel == "3":
         voc = input("輸入輸入要查詢的英文單字(按0跳出")
         if voc == "0":
             break
         if voc in engish:
             print(english[voc])
         else:
             print("字典裡沒有這個單字")
    elif sel == "4":
        got = False
        ch = input("輸入要查詢的中文單字(按0跳出")
        if ch == "0":
            break
        for k,v in english.item():
            if ch == v:
                print(ch,"的英文是",k)
                got = True
        if not got:
            print("抱歉，查不到")
    elif sel == "5":
        score = 0
        print("The total score is", len(english),"points")
        for k, v in english.items():
            print(v,":")
            ans = input()
            if ans == k:
                score = score + 1
                print("correct!you got",score,"points now")
            else :
                print("wrong!you got",score,"points now")
    elif sel == "6":
        break
    else:
        print("輸入錯誤，請重新輸入!")
          

        
             
