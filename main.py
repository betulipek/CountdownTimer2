import time as t

def stopwatch(sec):
    while sec:
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        print(timeformat, end='\r')
        t.sleep(100)
        sec -= 1
print('Goodbye!\n')
## calling stopwatch function
stopwatch(sec=100)