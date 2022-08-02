#goal: randomly (between 2-3 minutes) have the program "pause" users for 10 seconds and then tell them to "continue"

import random
import time

def pause():
    print("Stop!")
    time.sleep(10)
    #print("Continue")

def detect_pause():
    print("Start Learning!")
    timeCheck = random.randrange(120,240)
    time.sleep(timeCheck)
    pause()

def main():
    while True:
        detect_pause()

if __name__ == "__main__":
    main()

