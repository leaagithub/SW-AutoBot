from imagesearch import *
from OldImages import *
import pyautogui, time


def sellableRune():
    #Code to determine if a rune worth keeping or selling
    #Check if Blue runes are there
    pos = imagesearch_numLoop("GameImages/sell-pic.png", 1, 3, .85)
    print("image found ", pos[0], pos[1])
    if pos[0] != -1:
        print("sell the rune")
        #two window click
        pos = imagesearch_numLoop("GameImages/Sell-Rune.png", 1, 3, .85)
        print("image found ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(2)
        pyautogui.click()
        pos = imagesearch_numLoop("GameImages/Yes.png", 1, 3, .85)
        print("image found ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(2)
        pyautogui.click()
    else:
        pos = imagesearch_numLoop("GameImages/save-pic.png", 1, 3, .85)
        print("image found ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        if pos[0] != -1:
            print("get the rune")
            #one Window Click
            pos = imagesearch_numLoop("GameImages/OK.png", 1, 3, .85)
            print("image found ", pos[0], pos[1])
            pyautogui.moveTo(pos[0], pos[1])
            time.sleep(2)
            pyautogui.click()
    print("dealt with the rune screen")


def refill():
    # if out of energy proceed to buy energy 3 CLICKS
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(4)
    pyautogui.click()

    pos = imagesearch_numLoop("GameImages/energy-refill-option.png", 1, 5, .85)
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(4)
    pyautogui.click()
    pos = imagesearch_numLoop("GameImages/Yes-Refill.png", 1, 5, .85)
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(4)
    pyautogui.click()

    pos = imagesearch_numLoop("GameImages/OK.png", 1, 5, .85)
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(4)
    pyautogui.click()

    pos = imagesearch_numLoop("GameImages/CloseWindowButton.png", 1, 5, .85)
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(4)
    pyautogui.click()
