# importando tkinter
from tkinter import *
from tkinter import Tk, ttk

# colors
cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#faf5f5"
cor4 = "#8f8d8d"
cor5 = "#992828"


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")  # largura e comprimento
janela.config(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

# frames
frame_display = Frame(janela, width=235, height=50, bg=cor3)
frame_display.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)

# logica
text_value = StringVar()
all_value = ''


def inputValue(event):
    global all_value

    all_value = all_value + str(event)
    text_value.set(all_value)  # passando o valor para a tela


def calcular():
    global all_value

    result = eval(all_value)

    text_value.set(str(result))


def clean():
    global all_value

    all_value = ''
    text_value.set('')


# label
app_label = Label(frame_display, textvariable=text_value, width=16,
                  height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor1)
app_label.place(x=0, y=0)


# buttons
b_1 = Button(frame_body, command=clean, text="C", width=11, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)  # x horizontal, y vertical
b_2 = Button(frame_body, command=lambda: inputValue('%'), text="%", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_body, command=lambda: inputValue('/'), text="/", width=5, height=2, bg=cor5,
             fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_body, command=lambda: inputValue('7'), text="7", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_body, command=lambda: inputValue('8'), text="8", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body, command=lambda: inputValue('9'), text="9", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_body, command=lambda: inputValue('*'), text="*", width=5, height=2, bg=cor5,
             fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_body, command=lambda: inputValue('4'), text="4", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_body, command=lambda: inputValue('5'), text="5", width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body, command=lambda: inputValue('6'), text="6", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_body, command=lambda: inputValue('-'), text="-", width=5, height=2, bg=cor5,
              fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_body, command=lambda: inputValue('1'), text="1", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_body, command=lambda: inputValue('2'), text="2", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body, command=lambda: inputValue('3'), text="3", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_body, command=lambda: inputValue('+'), text="+", width=5, height=2, bg=cor5,
              fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_body, command=lambda: inputValue('0'), text="0", width=11, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_body, command=lambda: inputValue('.'), text=".", width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_body, command=calcular, text="=", width=5, height=2, bg=cor5,
              fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()
