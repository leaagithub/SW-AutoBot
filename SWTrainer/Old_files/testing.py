from RuneCheck import *
import pyautogui, time

pos = imagesearch("Sell Rune.png")
print("image found ", pos[0], pos[1])
print("selling rune")
time.sleep(2)
pyautogui.moveTo(pos[0], pos[1])
pyautogui.click()
time.sleep(2)
pos = imagesearch("Yes Button.png")
print("image found ", pos[0], pos[1])
print("Confirm Selling rune")
pyautogui.moveTo(pos[0], pos[1])
pyautogui.click()

pos = imagesearch("OK.png")
print("image found ", pos[0], pos[1])
print("claiming rune")
time.sleep(2)
pyautogui.moveTo(pos[0], pos[1])
pyautogui.click()