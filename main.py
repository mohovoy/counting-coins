from tkinter import *
from tkinter import messagebox


MONEY__1 = 0.01
MONEY__2 = 0.02
MONEY__5 = 0.05
MONEY__10 = 0.10
MONEY__20 = 0.20
MONEY__50 = 0.50
MONEY__100 = 1.00
MONEY__200 = 2.00

root = Tk()
root.title('Подсчет белорусских монет')
root.geometry('384x320')
root.resizable(False, False)

def CountingMoney():
    g_money_1 = float(money_1.get()) * MONEY__1
    g_money_2 = float(money_2.get()) * MONEY__2
    g_money_3 = float(money_3.get()) * MONEY__5
    g_money_4 = float(money_4.get()) * MONEY__10
    g_money_5 = float(money_5.get()) * MONEY__20
    g_money_6 = float(money_6.get()) * MONEY__50
    g_money_7 = float(money_7.get()) * MONEY__100
    g_money_8 = float(money_8.get()) * MONEY__200
    cash = g_money_1 + g_money_2 + g_money_3 + g_money_4 + g_money_5 + g_money_6 + g_money_7 + g_money_8
    messagebox.showinfo('Общая сумма', f'Общая сумма равна {cash:.2f} рублей')

t_money_1 = IntVar()
t_money_2 = IntVar()
t_money_3 = IntVar()
t_money_4 = IntVar()
t_money_5 = IntVar()
t_money_6 = IntVar()
t_money_7 = IntVar()
t_money_8 = IntVar()


LabelDescrText = 'В нижние поля введите кол-во монет каждой номинальности'
LabelDescr = Label(root, text=LabelDescrText)
label_1 = Label(root, text='1 копейка')
money_1 = Entry(root, textvariable=t_money_1)
label_2 = Label(root, text='2 копейки')
money_2 = Entry(root, textvariable=t_money_2)
label_3 = Label(root, text='5 копеек')
money_3 = Entry(root, textvariable=t_money_3)
label_4 = Label(root, text='10 копеек')
money_4 = Entry(root, textvariable=t_money_4)
label_5 = Label(root, text='20 копеек')
money_5 = Entry(root, textvariable=t_money_5)
label_6 = Label(root, text='50 копеек')
money_6 = Entry(root, textvariable=t_money_6)
label_7 = Label(root, text='1 рубль')
money_7 = Entry(root, textvariable=t_money_7)
label_8 = Label(root, text='2 рубля')
money_8 = Entry(root, textvariable=t_money_8)
button = Button(root, text='Подсчитать общую сумму', command=CountingMoney, font=12)

LabelDescr.place(x=8, y=10)
label_1.place(x=8, y=40)
money_1.place(x=72, y=40)
label_2.place(x=8, y=70)
money_2.place(x=72, y=70)
label_3.place(x=8, y=100)
money_3.place(x=72, y=100)
label_4.place(x=8, y=130)
money_4.place(x=72, y=130)
label_5.place(x=8, y=160)
money_5.place(x=72, y=160)
label_6.place(x=8, y=190)
money_6.place(x=72, y=190)
label_7.place(x=8, y=220)
money_7.place(x=72, y=220)
label_8.place(x=8, y=250)
money_8.place(x=72, y=250)
button.place(x=8, y=280, w=368)

root.mainloop()
