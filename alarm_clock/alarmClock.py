import time
from playsound import playsound
from datetime import datetime

t = input("Input time you want the alarm to ring (hour:min)?").split(":")
AP = input("Am or Pm?")

if AP == "Pm":
    t[0] = str(int(t[0]) + 12)

while True:
    if int(t[0]) == datetime.now().hour and int(t[1]) == datetime.now().minute:
        print("Its time!!!!")
        playsound("C:/Users/DELL/OneDrive/Máy tính/pythonProjects/alarm_tones.mp3")
        time.sleep(1)
        playsound("C:/Users/DELL/OneDrive/Máy tính/pythonProjects/alarm_tones.mp3")
        time.sleep(1)
        playsound("C:/Users/DELL/OneDrive/Máy tính/pythonProjects/alarm_tones.mp3")
        break 
