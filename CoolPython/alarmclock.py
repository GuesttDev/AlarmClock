import time
import datetime
import pygame

def setAlarm(alarmTime):
    print(f"Alarm set for {alarmTime}")
    soundFile = "CoolPython/Spark.mp3"
    
    while True:
        timenow = datetime.datetime.now().strftime("%H:%M:%S")
        print(timenow)

        if timenow == alarmTime:
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(soundFile)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)

if __name__ == "__main__":
    alarmTime = input("Enter the alarm time (HH:MM:SS): ")
    setAlarm(alarmTime)