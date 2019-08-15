import time


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

input("START?")
start_time = time.time()

while True:
    end_time = time.time()
    time_lapsed = int(end_time - start_time)
    print(time_calc(time_lapsed))
    time.sleep(1)
