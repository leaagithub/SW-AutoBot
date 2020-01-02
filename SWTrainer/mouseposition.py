import time

import pyautogui, sys

print('Press Ctrl-C to quit.')

# REPLAY_BUTTON  X: 792 Y: 558
# OK_BUTTONN X:959 Y:705
# Corner Spot: X1322 Y:256
# RUNE OPTIONS
# Sell Button X: 880 Y: 689
# GET RUNE ( OK BUTTON ) X : 1036 Y: 700

refill_button_cord = [917, 600]
refill_shop_exit_cord = [1328, 335]
event_ok_button_cord = [959, 640]


def move_mouse(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y)
    pyautogui.doubleClick()
    time.sleep(1)


# move_mouse(event_ok_button_cord[0], event_ok_button_cord[1])


try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
