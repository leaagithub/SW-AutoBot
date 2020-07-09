from imagesearch import *
from RuneCheck import *
import pyautogui, time

#WHOLE GAME SIZE : X: 560 : 240 TO X: 1360 Y : 840

RUN_TIME_SECONDS = 45
# Wait time secs for run to finish
RUN_NUMBER = 110
# HOW MANY ITERATIONS USUALLY
#105 not enough energy after refill captcha DO 115 NEXT TIME #125 WILL BE CAPTCHA
i = 0
while i < RUN_NUMBER:
    time.sleep(RUN_TIME_SECONDS)
    # Confirm Clear run and Open Chest
    pos = imagesearch_loop("GameImages/Victory.png", 1)
    #looks again after every 1 second
    #loc: 811 508
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(811, 508)
    time.sleep(2 + random.randrange(3))
    #random int
    pyautogui.click()
    print("getting chest")
    # Gets chest
    time.sleep(5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    #MAKE SURE CHEST IS OPEN
    time.sleep(random.randrange(3))
    pyautogui.click()
    print("opening chest")
    # open chest

    #Determine if it is a rune look for the sell button.
    pos = imagesearch_numLoop("GameImages/Sell-Rune.png", 1, 6, .85)
    print("image found ", pos[0], pos[1])
    if pos[0] != -1:
        #Deal with the rune
        isRune = True
        print("found rune window")
        #CALL THE RUNE CHECK METHOD
        sellableRune()
        #deals with rune screen
    else:
        #Claim the extra item
        isRune = False
        print("found extra item window")
        pos = imagesearch_numLoop("GameImages/OK.png", 1, 6, .85)
        #loc: 897 681
        print("image found ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(random.randrange(3))
        pyautogui.click()
        #deals with the extra item screen

    # RESET
    pos = imagesearch_numLoop("GameImages/Replay-Button.png", 1, 6, .85)
    #loc: 656 523
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(random.randrange(3))
    pyautogui.click()

    # REFILL (WHEN IT HAPPENS) CHECKS EVERY RUN
    pos = imagesearch_numLoop("GameImages/Shop.png", 1, 3, .85)
    print("image found ", pos[0], pos[1])
    if pos[0] != -1:
        # if out of energy proceed to buy energy 3 CLICKS
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(random.randrange(4))
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

        pos = imagesearch_numLoop("GameImages/Replay-Button.png", 1, 5, .85)
        print("image found ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(4)
        pyautogui.click()

    print("done with run")
    i += 1
    print("######################################################Run Number: ", i)
