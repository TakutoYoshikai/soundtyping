#!/usr/bin/env python
import pyxhook
import datetime
import simpleaudio
from playsound import playsound
import threading



def kbevent(event):
    threading.Thread(target=playsound, args=["sound.mp3"]).start()

hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
