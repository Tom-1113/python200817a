# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:59:15 2020

@author: USER
"""
s = float(input("請輸入成績"))
if s >=0 and s<=100:
    if s>=90:
        print("level A")
    elif s>=80:
        print("level B")
    elif s>=70:
        print("level C")
    elif s>=60:
        print("level D")
    else:
        print("level E")
else:
    print("輸入錯誤")
    s = float(input("請輸入成績"))
    if s >=0 and s<=100:
        if s>=90:
            print("level A")
        elif s>=80:
            print("level B")
        elif s>=70:
            print("level C")
        elif s>=60:
            print("level D")
        else:
            print("level E")
    else:
        print("輸入錯誤")