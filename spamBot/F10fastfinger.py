import time
import cv2
import pyautogui
import pyscreenshot as grabImage
import pytesseract
import numpy as np
from pynput import keyboard
import threading

def autofill():
    while(True):
        # this takes a snap of a certain portion of screen (1st line)
        GrabTextImage = grabImage.grab(bbox=(426,260,1385,310))
        # to convert image to string    
        text = pytesseract.image_to_string(GrabTextImage)
        # to remove last two bogus characters
        text = text[:-1]
        text = text[:-1]
        # adding a space since there's one at end
        text = text+" "
        # pyautogui to write string in textfield
        pyautogui.write(text)
        # adding a 1 second delay to to avoid afk
        time.sleep(1)

running = False

def testing():
    a=0
    while 1:
        a=a+1
        print(a)
        time.sleep(1)

def on_press(key):
    global running
    if key == keyboard.Key.f4:
        running = True
        t = threading.Thread(target=autofill)
        t.start()
    if key == keyboard.Key.f2:
        return False

def on_release(key):
    global running
    if key == keyboard.Key.f2:
        running = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



    

