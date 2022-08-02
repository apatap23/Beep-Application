#goal: randomly (between 2-3 minutes) have the program "pause" users for 10 seconds and then tell them to "continue"

import random
import time
from playsound import playsound

def pause():
    playsound('/audio/pause.mp3') #verbal print("Stop!")
    time.sleep(10)

def detect_pause():
    playsound('/audio/start.mp3') #vertbal print("Start Learning!")
    timeCheck = random.randrange(120,240)
    time.sleep(timeCheck)
    pause()

def main():
    while True:
        detect_pause()

if __name__ == "__main__":
    main()

