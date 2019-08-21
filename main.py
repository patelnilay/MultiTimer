import time
import tkinter

start_time = time.time()


def time_calc(sec):
    minutes = sec // 60
    seconds = str(sec % 60)
    hours = str(minutes // 60)
    minutes = str(minutes % 60)
    if len(seconds) == 1:
        seconds = "0" + seconds
    if len(minutes) == 1:
        minutes = "0" + minutes
    return "{}:{}:{}".format(hours, minutes, seconds)


top = tkinter.Tk()

time1 = tkinter.StringVar()
timer1 = tkinter.Label(top, textvariable=time1).grid(row=0, column=0)
button1 = tkinter.Button().grid(row=1, column=0)

time2 = tkinter.StringVar()
timer2 = tkinter.Label(top, textvariable=time2).grid(row=0, column=1)
button2 = tkinter.Button().grid(row=1, column=1)

time3 = tkinter.StringVar()
timer3 = tkinter.Label(top, textvariable=time3).grid(row=0, column=2)
button3 = tkinter.Button().grid(row=1, column=2)

time4 = tkinter.StringVar()
timer4 = tkinter.Label(top, textvariable=time4).grid(row=0, column=3)
button4 = tkinter.Button().grid(row=1, column=3)

while True:
    top.update_idletasks()
    top.update()
    time1.set(time_calc(int(time.time() - start_time)))
    time2.set(time_calc(int(time.time() - start_time - 1)))
    time3.set(time_calc(int(time.time() - start_time - 2)))
    time4.set(time_calc(int(time.time() - start_time - 3)))
