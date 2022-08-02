#goal: randomly (between 2-3 minutes) have the program "pause" users for 10 seconds and then tell them to "continue"

import random
import time
from pydub import AudioSegment
from pydub.playback import play

def pause():
    sound = AudioSegment.from_mp3('./audio/pause.mp3') #verbal print("Stop!")
    play(sound)
    time.sleep(15)

def detect_pause():
    sound = AudioSegment.from_mp3('./audio/start.mp3') #vertbal print("Start Learning!")
    play(sound)
    timeCheck = random.randrange(120,240)
    time.sleep(timeCheck + 5)
    pause()

def main():
    while True:
        detect_pause()

if __name__ == "__main__":
    main()

