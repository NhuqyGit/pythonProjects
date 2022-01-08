import time
from playsound import playsound

tic = int(input("Input your time your want to countdown: "))

while tic:
    mins = tic // 60
    secs = tic % 60
    clock = '{:02d}:{:02d}'.format(mins,secs)

    print(" " + clock, end='\r')
    time.sleep(1)
    tic -= 1
print("Its time!!!")
playsound("C:/Users/DELL/OneDrive/Máy tính/openCV/iphone_4s.mp3")