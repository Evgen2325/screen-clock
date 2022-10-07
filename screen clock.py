import tkinter
import datetime
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=800, height=100)
canvas.pack()
x = 400
our_time = canvas.create_text(100, 150, text='', font=('Arial', 50), fill='DarkMagenta')
delta = 2
while True:
    x = x + delta
    canvas.coords(our_time, x, 50)
    nowtime = datetime.datetime.now()
    text = nowtime.strftime("%c")
    canvas.itemconfig(our_time, text=text)
    canvas.update()
    if x < 360 or x > 440:
        delta = -delta
    time.sleep(0.01)
# noinspection PyUnreachableCode
window.mainloop()
