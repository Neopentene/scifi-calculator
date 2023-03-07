# -*- coding: utf-8 -*-
"""
Created on Sun May  9 16:59:55 2021

@author: Celestyn
"""

from tkinter import Tk, Button, Entry, PhotoImage, Frame, Label, StringVar, INSERT, END, NSEW, SUNKEN, FLAT
from evaluator import Evaluator
import calLogs as log

#Expression
expression = ""

#Variables
count = 0
validInput = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/","×","x","÷","^",".","!","(",")"]
logPosition = 0
once = True
List = []

#Instances of buttons and fields
buttons = []
imageIds = []


#base path to the assets folder from drive it is located in
basePath = "D:\\College Work\\College-PP\\Mini-project\\Calculator\\assets"

# Dictionary for assets and events, format --> button number: (file_name, event_attached)
assets = {
        0: ("\\raiseTo.png", "^"),
        1: ("\\down.png", "Down"),
        2: ("\\up.png", "Up"),
        3: ("\\clearLogs.png", "clear logs"),
        4: ("\\fact.png", "!"),
        5: ("\\left.png", "Left"),
        6: ("\\right.png", "Right"),
        7: ("\\showlogs.png", "show logs"),
        8: ("\\allClear.png", "clear"),
        9: ("\\paraOpen.png", "("),
        10: ("\\paraClose.png", ")"),
        11: ("\\div.png", "÷"),
        12: ("\\7.png", "7"),
        13: ("\\8.png", "8"),
        14: ("\\9.png", "9"),
        15: ("\\mult.png", "×"),
        16: ("\\4.png", "4"),
        17: ("\\5.png", "5"),
        18: ("\\6.png", "6"),
        19: ("\\sub.png", "-"),
        20: ("\\1.png", "1"),
        21: ("\\2.png", "2"),
        22: ("\\3.png", "3"),
        23: ("\\add.png", "+"),
        24: ("\\0.png", "0"),
        25: ("\\decimal.png", "."),
        26: ("\\backspace.png", "BackSpace"),
        27: ("\\equal.png", "\r")
    }

#Root
root = Tk()
root.title("My Scifi Calculator")
root.iconbitmap(basePath + "\\icon.ico")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Event handler
def events(event, key = None):
    global expression
    global logPosition
    global once
    global List
    position = expression_field.index(INSERT)
    
    if (event == "clear" or event == "a"):
        setExpressionData()
        
    elif (event == "clear logs" or event == "c"):
        log.logManager().clearAllLogs()
        setExpressionData("", "Logs cleared")
        once = True
        
        fieldFocusEnd()
        
    elif (event == "show logs" or event == "s"):
        once = True
        events("Up")
    
    elif (event == "BackSpace" or event == "Delete"):
        if(key == None):
            if position - 1 >= 0:
                expression = expression[0:position - 1] + expression[position:]
                equation.set(expression)
                if (position - 1 < len(expression)): events("Left")
        else:
            expression = equation.get()
            
    elif (event == "Up"):
        if once:
            List = log.logManager().getAllLogs()
            logPosition = len(List) - 1
            once = False
        else:
            logPosition = logPosition - 1
        
        if(logPosition >= 0):
            setExpressionData(List[logPosition][1], List[logPosition][1])
        else:
            logPosition = 0
            once = True
            setExpressionData("", " No Logs")
            
        fieldFocusEnd()
        
    elif (event == "Down"):
        if once:
            List = log.logManager().getAllLogs()
            logPosition = 0
            once = False
        else:
            logPosition = logPosition + 1
        
        if(logPosition < len(List)):
            setExpressionData(List[logPosition][1], List[logPosition][1])
        else:
            logPosition = 0
            once = True
            setExpressionData("", " No Logs")
            
        fieldFocusEnd()
        
    elif (event == "Left"):
        position = position - 1 if(position > 0 and key == None) else 0 if(key == None) else position
        expression_field.icursor(position)
        expression_field.xview(position)
        
    elif (event == "Right"):
        position = position + 1 if(position < len(expression) and key == None) else len(expression) if(key == None) else position
        expression_field.icursor(position)
        expression_field.xview(position)
    
    #Equal, Return or Enter pressed
    elif (event == "\r"):
        try:
            equation.set(Evaluator(str(expression)).evaluate())
            expression = equation.get()
            once = True
        except:
            setExpressionData("", "Error")
            
        fieldFocusEnd()
            
    else:
        if str(event) in validInput:
            
            if (key == None):
                setexp = expression[0:position] + str(event) + expression[position:]
            else:
                setexp = expression[0:position - 1] + str(event) + expression[(position - 1):]
            setExpressionData(setexp, setexp)
            
            expression_field.focus()
            events("Right", key)
        else:
            equation.set(expression)
            events("Left")

#Key board to event handler router
def keyBoardEvents(event):
    print( event)
    if str(event.keysym) in ["BackSpace", "Delete", "Up", "Down"]:
        events(str(event.keysym), event.keysym)
    else:
        if (str(event.char) != ""): events(str(event.char), event.keysym)
        
def fieldFocusEnd():
    expression_field.focus()
    expression_field.icursor(END)
    
def setExpressionData(Expression = "", Equation = ""):
    global expression
    expression = Expression
    equation.set(Equation)
    
#---GUI Instances start from here---

#Inner frame for padding
innerFrame = Frame(root, padx = 5, pady = 5, highlightbackground="black", highlightthickness=1)
innerFrame.grid(columnspan = 4, rowspan = 9, sticky=NSEW)
innerFrame.columnconfigure(tuple(range(4)), weight=1)
innerFrame.rowconfigure(tuple(range(9)), weight=1)

#Field updater inside the Entry
equation = StringVar()

#Header
header_img = PhotoImage(file = basePath + "\\heading.png").subsample(10, 12)
header = Label(innerFrame, image = header_img)
header.grid(columnspan=4, sticky=NSEW)

#Set the Entry field
expression_field_frame = Frame(innerFrame, relief=SUNKEN, borderwidth=5)
expression_field_frame.grid(row = 1, columnspan=4, rowspan = 1, ipady = 10, sticky = NSEW)
expression_field_frame.rowconfigure((0), weight=1)
expression_field_frame.columnconfigure((0), weight=1)
expression_field = Entry(expression_field_frame, textvariable=equation, font="SegoeUI 16", bg="#99D2D0", justify="right")
expression_field.config(borderwidth=10, relief=FLAT)
expression_field.grid(rowspan = 1, columnspan=1, sticky=NSEW)

#Set the instances
for i in range(2, 9):
    for j in range(4):
        imageIds.append(PhotoImage(file = basePath + assets[count][0]).subsample(8, 8))
        buttons.append(Button(innerFrame, image = imageIds[count], borderwidth = 0, command = lambda setEvent = count: events(assets[setEvent][1])))
        buttons[count].grid(row = i, column = j, sticky=NSEW)
        count += 1

#Binded key press events to root
root.bind("<Key>", keyBoardEvents)

#Looping root
root.mainloop()
    
    