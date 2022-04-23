# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:32:45 2022

@author: Lucas
"""

import tkinter as tk
import math
import webbrowser
from tkinter import messagebox

'''.方法說明
.get() 取得數值
.configure() label的屬性(參數)
.delete() 刪除字串
.insert() 插入字串
'''
#計算 BMI and 體指率(BDF)
def Count():
    h = float(height_entry.get()) #取得輸入值
    w = float(weight_entry.get())
    y = int(age_entry.get())
    BMI_value = round(w/math.pow(h, 2), 2) #取小數兩位
    result1 = "Your BMI index is {}, Body Fat Percentage is {}".format(BMI_value, BodyFat(BMI_value,y))
    result2 = Status(BMI_value)
    result_label1.configure(text = result1)
    result_label2.configure(text = result2)
    
#體指率計算(BDF)
def BodyFat(BMI_value, y):
    if genderValue.get() == 1:
        BFP = 1.2*BMI_value + 0.23*y - 5.4 - 10.8
    
    elif genderValue.get() == 0:
        BFP = 1.2*BMI_value + 0.23*y - 5.4
    return round(BFP, 2)

#BMI對應體態 
def Status(BMI_value):
    x = BMI_value
    if 10 <= x < 18.5:
        return("You are too thin. Get the fucking home and eat some food.")
    elif 18.5 <= x < 24:
        return("Good status. Keep going!")
    elif 24.5 <= x < 50:
        return("Holy Fatty Guy. Shut the fuck up and go to exercise.")
    elif x<10 or x>=50:
        return("87? Please fill out the blank again.")

#清除Entry內容，可以重新輸入
def Clear():
    height_entry.delete(0, "end")
    weight_entry.delete(0, "end")
    age_entry.delete(0, "end")
    height_entry.insert(0, "Input...")
    weight_entry.insert(0, "Input...")
    age_entry.insert(0, "Input...")

#detial BMI資訊
def Detial(url):
    webbrowser.open_new(url) #打開網頁

#離開警告視窗
def Exit():
    msgbox = tk.messagebox.askquestion("Exit Warning", "Press 是(Y) to left.")
    if msgbox == 'yes':
        UI.destroy() #結束視窗
        
#視窗設定
UI = tk.Tk()
UI.title("BMI Calculator")
#UI.geometry("700x500") #使用.grid就不用設定視窗大小了
'''.grid說明
grid是一種排列元件的方法
他的做法是把元件放入一格一格的陣列(row, column)，然後視窗再按照元件數去設定大小
'''
UI.configure(background = "white")

#header
head_label = tk.Label(UI,text = "BMI Calculator",bg = "white", font = ("Times", 30, "italic"))
head_label.grid(row=0, column=1)

'''Button(按鈕) Label(標籤欄位) 參數說明
text 呈現文字
bg 背景
fg 前景
wdith 寬度
font 字體大小格式顏色
relief 字體立體感
command 點按鈕做出動作
'''
#建立height items
height_label = tk.Label(UI, text = "Height(m)", bg = "white", font = ("Times", 20, "italic")) #標籤名稱
height_label.grid(row=1, column=0)
height_entry = tk.Entry(UI, width = 30, relief = "solid") #輸入欄位
height_entry.grid(row=1, column=1)

#建立weight items
weight_label = tk.Label(UI, text = "Weight(kg)", bg = "white", font = ("Times", 20, "italic"))
weight_label.grid(row=2, column=0)
weight_entry = tk.Entry(UI, width = 30, relief = "solid")
weight_entry.grid(row=2, column=1)

#建立年齡欄位
age_label = tk.Label(UI, text = "Age", font = ("Times", 20, "italic"), bg = "white")
age_label.grid(row=3,column=0)
age_entry = tk.Entry(UI, width = 30, relief = "solid")
age_entry.grid(row=3, column=1)

#建立單選按鈕
gender_label = tk.Label(UI, text = "Gender", bg = "white", font = ("Times", 20, "italic"))
gender_label.grid(row=4, column=0)
genderValue = tk.IntVar() #建立選項型別 
#value可以回傳值到def BDF
gender1 = tk.Radiobutton(UI, text='Male', variable=genderValue, value=1, bg = "white", font = ("Times", 15, "italic")) 
gender2 = tk.Radiobutton(UI, text='Female', variable=genderValue, value=0, bg = "white", font = ("Times", 15, "italic")) 
gender1.grid(row=4, column=1)
gender2.grid(row=4, column=2)

#建立計算結果的按鈕
calc_btn = tk.Button(UI, text = "Start", width = 5, font = ("Times", 20, "italic"), command = Count)
calc_btn.grid(row=5, column=0)

#清除輸入欄的按鈕
clear_btn = tk.Button(UI, text = "Clear",width = 5, font = ("Times", 20, "italic"), command = Clear)
clear_btn.grid(row=5, column=1)

#detial 超連結，使用.bind事件處理 #lambda萬能工具
site = tk.Label(UI, text="BMI Detial", bg = "white", fg="blue", cursor="hand2", font = ("Times", 20, "italic"))
site.grid(row=7, column=2)
site.bind("<Button-1>", lambda e: Detial("https://tools.heho.com.tw/bmi/"))

#建立result(顯示計算結果)
result_label1 = tk.Label(UI, font = ("Times", 15, "italic"), bg = "white")
result_label1.grid(row=6, column=0)
result_label2 = tk.Label(UI, font = ("Times", 15, "italic"), bg = "white")
result_label2.grid(row=7, column=0)

#建立離開按鈕
exit_btn = tk.Button(UI, text = "Exit", width = 5, font = ("Times", 20, "italic"), command = Exit)
exit_btn.grid(row=5, column=2)

#進入視窗迴圈
UI.mainloop() 
