#!/usr/bin/env python
import pyxhook
import datetime
import simpleaudio
from playsound import playsound
import threading
import argparse



sound_file = ""

def kbevent(event):
    threading.Thread(target=playsound, args=[sound_file]).start()

def main():
    global sound_file
    parser = argparse.ArgumentParser(description="This is a program to play sound when you are typing.")
    parser.add_argument("sound", help="a sound file (mp3/wav)")
    args = parser.parse_args()
    sound_file = args.sound
    hookman = pyxhook.HookManager()
    hookman.KeyDown = kbevent
    hookman.HookKeyboard()
    hookman.start()

if __name__ == "__main__":
    main()
