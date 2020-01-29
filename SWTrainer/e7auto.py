from imagesearch import *
from GameImages import *
import adbutils
import time
confirm_button = [1450, 830]
friend_send_no = [660, 650]
RUN_TIME_SECONDS = 120
screen_size = [2400, 1400]
#x1y1x2y2
game_region_size = [screen_size[0]/2, 0, screen_size[0], screen_size[1]/2]
emulator_id = "emulator-5574"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)
RUN_NUMBER = 50


def reset_run():
    time.sleep(3)
    d.click(friend_send_no[0], friend_send_no[1])
    time.sleep(3)
    d.click(friend_send_no[0], friend_send_no[1])
    time.sleep(3)
    d.click(friend_send_no[0], friend_send_no[1])
    time.sleep(3)
    d.click(confirm_button[0], confirm_button[1])
    time.sleep(3)
    d.click(confirm_button[0], confirm_button[1])
    time.sleep(3)
    d.click(confirm_button[0], confirm_button[1])
    time.sleep(3)
    d.click(confirm_button[0], confirm_button[1])
    time.sleep(3)
    d.click(confirm_button[0], confirm_button[1])
    time.sleep(3)



i = 0
while i < RUN_NUMBER:
    print("Starting Program")
    time.sleep(RUN_TIME_SECONDS)
    print("Looking Image")
    pos = imagesearch_loop("GameImages/e7-stagecomplete.png", 5)
    # pos = imagesearch_region_loop("GameImages/e7-stagecomplete.png", 1, game_region_size[0], game_region_size[1], game_region_size[2], game_region_size[3])
    print('Found Complete Image')
    time.sleep(3)
    pos = imagesearch_numLoop("GameImages/e7-urgentmission.png", 1, 3, .85)
    print("image found ", pos[0], pos[1])
    if pos[0] != -1:
        d.click(650, 650)
    print("Done")
    reset_run()
    i += 1
    print("######################################################Run Number: ", i)



