from tkinter import *
from tkinter import messagebox
from time import sleep

root = Tk()
root.geometry('250x250')
root.title('Clicker')
root.resizable(False, False)

upgrade_price = 30
value = 0
points_per_click = 1

lbl = Label(root, text=str(value))
lbl.pack(expand=1)

lbl_2 = Label(root, text='points per click = ' + str(points_per_click))
lbl_2.pack()


def upgrade1():
    global points_per_click
    global lbl
    global lbl_2
    global value
    global upgrade_price
    global btn_2
    if value >= upgrade_price:
        points_per_click += 1
        lbl_2.configure(text='points per click = ' + str(points_per_click))
        value -= upgrade_price
        lbl.configure(text=str(value))
        messagebox.showinfo(title='congrats!', message='you just bought an upgrade')
        upgrade_price += 10
        btn_2.configure(text='upgrade: +1 (costs ' + str(upgrade_price) + ' clicks)')
        if points_per_click == 100:
            messagebox.showinfo(title='Umm...', message='congrats. did you really have nothing to do with your day?')
            sleep(2)
            root.quit()
    else:
        messagebox.showwarning(title='not enough points', message="you don't have enough points\nto buy this upgrade")


def btn_click():
    global lbl
    global value
    global points_per_click
    value += points_per_click
    if value >= 100000:
        messagebox.showinfo(title='Umm...', message='congrats. did you really have nothing to do with your day?')
        sleep(2)
        root.quit()
    lbl.configure(text=str(value))


btn_1 = Button(root, text='Click me!', command=btn_click)
btn_1.pack()

btn_2 = Button(root, text='upgrade: +1 (costs ' + str(upgrade_price) + ' clicks)', command=upgrade1)
btn_2.pack()

root.mainloop()
