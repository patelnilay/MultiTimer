import time
import tkinter

start_time = time.time()

beginning1 = None
beginning2 = None
beginning3 = None
beginning4 = None

end1 = None
end2 = None
end3 = None
end4 = None

started1 = False
started2 = False
started3 = False
started4 = False


def start1():
    global beginning1
    global started1
    if not started1:
        beginning1 = time.time()
    started1 = True


def start2():
    global beginning2
    global started2
    if not started2:
        beginning2 = time.time()
    started2 = True


def start3():
    global beginning3
    global started3
    if not started3:
        beginning3 = time.time()
    started3 = True


def start4():
    global beginning4
    global started4
    if not started4:
        beginning4 = time.time()
    started4 = True


def stop1():
    global end1
    global started1
    if started1:
        end1 = time.time()
        started1 = False


def stop2():
    global end2
    global started2
    if started2:
        end2 = time.time()
        started2 = False


def stop3():
    global end3
    global started3
    if started3:
        end3 = time.time()
        started3 = False


def stop4():
    global end4
    global started4
    if started4:
        end4 = time.time()
        started4 = False


def reset1():
    global beginning1
    global end1
    if not started1:
        beginning1 = None
        end1 = None


def reset2():
    global beginning2
    global end2
    if not started2:
        beginning2 = None
        end2 = None


def reset3():
    global beginning3
    global end3
    if not started3:
        beginning3 = None
        end3 = None


def reset4():
    global beginning4
    global end4
    if not started4:
        beginning4 = None
        end4 = None


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
top.title("MultiTimer")

time1 = tkinter.StringVar()
name1 = tkinter.Entry().grid(row=0, column=0)
timer1 = tkinter.Label(top, textvariable=time1).grid(row=1, column=0)
button1start = tkinter.Button(text="START", command=start1).grid(row=2, column=0, sticky="W")
button1stop = tkinter.Button(text="STOP", command=stop1).grid(row=2, column=0)
button1reset = tkinter.Button(text="RESET", command=reset1).grid(row=2, column=0, sticky="E")

time2 = tkinter.StringVar()
name2 = tkinter.Entry().grid(row=0, column=1)
timer2 = tkinter.Label(top, textvariable=time2).grid(row=1, column=1)
button2start = tkinter.Button(text="START", command=start2).grid(row=2, column=1, sticky="W")
button2stop = tkinter.Button(text="STOP", command=stop2).grid(row=2, column=1)
button2reset = tkinter.Button(text="RESET", command=reset2).grid(row=2, column=1, sticky="E")

time3 = tkinter.StringVar()
name3 = tkinter.Entry().grid(row=0, column=2)
timer3 = tkinter.Label(top, textvariable=time3).grid(row=1, column=2)
button3start = tkinter.Button(text="START", command=start3).grid(row=2, column=2, sticky="W")
button3stop = tkinter.Button(text="STOP", command=stop3).grid(row=2, column=2)
button3reset = tkinter.Button(text="RESET", command=reset3).grid(row=2, column=2, sticky="E")

time4 = tkinter.StringVar()
name4 = tkinter.Entry().grid(row=0, column=3)
timer4 = tkinter.Label(top, textvariable=time4).grid(row=1, column=3)
button4start = tkinter.Button(text="START", command=start4).grid(row=2, column=3, sticky="W")
button4stop = tkinter.Button(text="STOP", command=stop4).grid(row=2, column=3)
button4reset = tkinter.Button(text="RESET", command=reset4).grid(row=2, column=3, sticky="E")

while True:
    try:
        top.update_idletasks()
    except tkinter.TclError:
        break
    top.update()
    if started1:
        time1.set(time_calc(int(time.time() - beginning1)))
    elif beginning1 is not None:
        time1.set(time_calc(int(end1 - beginning1)))
    else:
        time1.set("0:00:00")
    if started2:
        time2.set(time_calc(int(time.time() - beginning2)))
    elif beginning2 is not None:
        time2.set(time_calc(int(end2 - beginning2)))
    else:
        time2.set("0:00:00")
    if started3:
        time3.set(time_calc(int(time.time() - beginning3)))
    elif beginning3 is not None:
        time3.set(time_calc(int(end3 - beginning3)))
    else:
        time3.set("0:00:00")
    if started4:
        time4.set(time_calc(int(time.time() - beginning4)))
    elif beginning4 is not None:
        time4.set(time_calc(int(end4 - beginning4)))
    else:
        time4.set("0:00:00")
    time.sleep(.1)
