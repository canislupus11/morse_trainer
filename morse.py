from morsecodelib import sound as morseSound
from morsecodelib.config import config as morseConfig

import sys
import time
import random
import os

if len (sys.argv) != 3 :
    print("Usage: python morse.py wpm tone_freq")
    sys.exit (1)

morseConfig.WORDS_PER_MINUTE = int(sys.argv[1])
morseConfig.FREQUENCY = int(sys.argv[2])

player = morseSound.MorseSoundPlayer()
znaki = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "O", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while True:
        os.system('clear')
        znak = random.choice(znaki)
        print(znak)
        time.sleep(0.3)
        player.text_to_sound(znak)
        time.sleep(1)
