math = float(input("math score"))
eng = float(input("eng score"))
if eng >=0 and eng<=100 and math >=0 and math<=100:
    if eng>=90 and math>=90:
        print("你有獎品")
    elif eng<60 and math<60:
        print("你要被處罰")
    elif eng<60 or math<60:
        print("要加油")
    else:
        print("很好")
else:
    print("輸入錯誤")