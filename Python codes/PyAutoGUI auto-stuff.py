# PyAutoGUI auto-stuff
# So maybe I was a bad loser sometimes and when I lost but my mate didn't forfeit, I code this anti-AFK. It doesn't work all the time but it's pretty effective against the big dickheads...

import pyautogui as gui
import time as time_ 
import keyboard as kb
from random import *

def CheckProb(echelle: int, poids = 1) :
    return randint(1, echelle) <= poids

time_.sleep(5)

while True :
    gui.keyUp('z')
    gui.keyUp('d')
    gui.keyUp('q')
    gui.click()
        

 