from tkinter import *

root = Tk()

root['bg'] = '#fafafa'
root.title('Супер приложение')
root.geometry('700x700')

# root.wm_attributes('-alpha', 0.7)
# root.resizable(width=False, height=False)

canvas = Canvas(root, height=700, width=700)
canvas.pack()

frame = Frame(root, bg='black')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow')
btn.pack()
root.mainloop()
