import pyautogui as spammer
import time

time.sleep(2)
string='pls meme'
t=time.time()

while time.time()-t < 45:
    spammer.write(string)
    spammer.press('enter')