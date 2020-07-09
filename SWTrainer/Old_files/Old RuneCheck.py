from imagesearch import *
from RuneCheck import *
import pyautogui, time

pos = imagesearch_numLoop("GameImages/OK.png", 1, 3, .85)
print("image found ", pos[0], pos[1])
pyautogui.moveTo(pos[0], pos[1])
time.sleep(2)
pyautogui.click()
print("done with run")