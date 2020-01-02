from imagesearch import *
from RuneCheck import *
import pyautogui, time



RUN_TIME = 30
# Wait time secs for run to finish
n = 100
# HOW MANY ITERATIONS USUALLY 100
i = 0
while i < n:
    #start run
    pos = imagesearch_loop("GameImages/toa-start-battle.png", 1)
    # looks again after every 1 second
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2)
    pyautogui.click()
    print("starting run")

    # REFILL (WHEN IT HAPPENS) CHECKS EVERY RUN
    pos = imagesearch_numLoop("GameImages/Shop.png", 1, 3, .85)
    print("image found ", pos[0], pos[1])
    if pos[0] != -1:
        # refill if u find the shop button
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

        pos = imagesearch_loop("GameImages/toa-start-battle.png", 1)
        # looks again after every 1 second
        print("image found ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(2)
        pyautogui.click()
        print("starting run")


    time.sleep(RUN_TIME)
    # Confirm Clear run and Open Chest
    pos = imagesearch_loop("GameImages/toa-victory.png", 1)
    #looks again after every 1 second
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2)
    pyautogui.click()
    print("getting chest")
    # Gets chest
    time.sleep(5)
    pyautogui.click()
    time.sleep(5)
    pyautogui.click()
    #MAKE SURE CHEST IS OPEN
    time.sleep(5)
    pyautogui.click()
    print("opening chest")
    # open chest
    #claim toa reward
    pos = imagesearch_numLoop("GameImages/OK.png", 1, 4, .85)
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2)
    pyautogui.click()

    # RESET
    pos = imagesearch_numLoop("GameImages/toa-next-stage.png", 1, 6, .85)
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2)
    pyautogui.click()

    print("done with run")
    i += 1
    print("######################################################Run Number: ", i)
