from imagesearch import *
from RuneCheck import *
import pyautogui, time



RUN_TIME = 110
# Wait time secs for run to finish
n = 95
# HOW MANY ITERATIONS USUALLY 100
i = 0
while i < n:
    time.sleep(RUN_TIME)
    # Confirm Clear run and Open Chest
    pos = imagesearch_loop("GameImages/riftdungeon-result.png", 1)
    #looks again after every 1 second
    #loc: 811 508
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2 + random.randrange(9))
    #random int
    pyautogui.click()
    print("getting chest")
    # Gets chest
    time.sleep(5)
    pyautogui.click()
    #MAKE SURE CHEST IS OPEN
    time.sleep(5)
    pyautogui.click()
    print("opening chest")
    # open chest

    #Claim the extra item
    print("found extra item window")
    pos = imagesearch_numLoop("GameImages/OK.png", 1, 3, .85)
    #loc: 897 681
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2)
    pyautogui.click()
    #deals with the extra item screen

    # RESET
    pos = imagesearch_numLoop("GameImages/Replay-Button.png", 1, 6, .85)
    #loc: 656 523
    print("image found ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(2)
    pyautogui.click()

    print("done with run")
    i += 1
    print("######################################################Run Number: ", i)
