import json
import os

from tkinter import *
from tkinter import messagebox

##
def newTask():
    task = my_entry.get()
    if task != '':
        lb.insert(END, task)
        my_entry.delete(0, 'end')
    else:
        messagebox.showwarning('WARNING', 'Please enter some task.')

##
def deleteTask():
    lb.delete(ANCHOR)

# TACHA EL TEXTO
def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

##
def markDoneTask():
    text = lb.get(ANCHOR)
    text = strike(text)

    lb.delete(ANCHOR)
    lb.insert(ANCHOR, text)

##
def closeWindow():
    saveData()
    ws.destroy()

##
def saveData():
    data = {}
    data['chores'] = lb.get(0, END)
    with open(directory + '/data.json', 'w') as js:
        json.dump(data, js)

##
def getData():
    try:
        with open(directory + '/data.json') as js:
            data = json.load(js)
            task_list = data['chores']
    except:
        task_list = []
    for item in task_list:
        lb.insert(END, item)

##
def setScrollbarList():
    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    getData()
    sb.config(command=lb.yview)    

def generateButtons():
    addTask_btn = Button(
        button_frame,
        font=('Helvetica 14'),
        bg='#37C871',
        text='Add Task',
        padx=20,
        pady=10,
        command=newTask
    )
    
    delTask_btn = Button(
        button_frame,
        font=('Helvetica', 14),
        bg='#FF0000',
        text='Delete Task',
        padx=10,
        pady=10,
        command=deleteTask
    )

    markDone_btn = Button(
        button_frame,
        font=('Helvetica', 14),
        bg='#133AF0',
        text='Finish Task',
        padx=12,
        pady=10,
        command=markDoneTask
    )

    closeWindow_btn = Button(
        button_frame,
        font=('Helvetica', 14),
        bg='#808080',
        text='Close',
        padx=35,
        pady=10,
        command=closeWindow
    )

    addTask_btn.grid(column=0, row = 1)
    delTask_btn.grid(column=1, row = 1)
    markDone_btn.grid(column=0, row = 2)
    closeWindow_btn.grid(column=1, row = 2)

full_path = os.path.realpath(__file__)
directory = os.path.dirname(full_path)

ws = Tk()
ws.geometry('600x700')
ws.title('Today\'s chores')
ws.config(bg='#000000')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=30)

lb = Listbox(
        frame,
        width=40,
        height=15,
        font=('Helvetica', 18),
        bd=0,
        fg='#464646',
        bg='#101613',
        highlightthickness=0,
        selectbackground='#A6A6A6',
        activestyle="none"
    )
lb.pack(side=LEFT, fill=BOTH)
setScrollbarList()

newTaskLabel = Label(
    ws, 
    text='Insert new chore', 
    bg='#000000'
)
newTaskLabel.pack()
my_entry = Entry(
    ws, 
    font=('times', 24), 
    bg='#101613',
    width=30,
)
my_entry.pack(pady=10)

button_frame = Frame(ws, bg='#000000', pady=10)
button_frame.pack()
generateButtons()

ws.mainloop()