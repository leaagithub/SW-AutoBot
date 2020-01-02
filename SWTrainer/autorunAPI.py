import sys
import flask
import pyautogui
import time
from flask import request, jsonify

run_count = 0
refill_count = 0
app = flask.Flask(__name__)
app.config["DEBUG"] = True

replay_button_cord = [792, 558]
ok_button_cord = [959, 705]
corner_spot_cord = [1322, 256]
sell_rune_cord = [880, 689]
sell_rune_confirm_cord = [880, 590]
get_rune_cord = [1036, 700]
refill_button_cord = [917, 600]
refill_shop_exit_cord = [1328, 335]
event_ok_button_cord = [959, 640]
refill_count_limit = 10


def rune_quality_check(rune):
    if rune['class'] < 6:
        print('Only Keep 6 star')
        return True
    if rune['rank'] < 4:
        print('Only Keep Purples and Up')
        return True
    if rune['pri_eff'][0] == 8:
        print('Purple Spd Slot 2')
        return False
    if rune['rank'] == 5:
        print('Legend 6 Star Keep')
        return False
    for subStats in rune['sec_eff']:
        if subStats[0] == 8:
            print('Found Spd Sub')
            return False
    print('Found No Spd Sub')
    return True


def move_mouse(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(1)


def grab_chest():
    time.sleep(10)
    pyautogui.moveTo(corner_spot_cord[0], corner_spot_cord[1])
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.doubleClick()
    time.sleep(1)
    pyautogui.doubleClick()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/', methods=['POST'])
def home():
    # print(request.json)
    global run_count
    global refill_count
    data = request.json
    grab_chest()
    try:
        if data['reward']['crate']['rune']:
            print(data['reward'])
            if rune_quality_check(data['reward']['crate']['rune']):
                move_mouse(sell_rune_cord[0], sell_rune_cord[1])
                move_mouse(sell_rune_confirm_cord[0], sell_rune_confirm_cord[1])
            else:
                move_mouse(get_rune_cord[0], get_rune_cord[1])
    except:
        move_mouse(ok_button_cord[0], ok_button_cord[1])
    try:
        if data['reward']['event_crate']:
            move_mouse(event_ok_button_cord[0], event_ok_button_cord[1])
    except:
        print('No event Crate')
    time.sleep(2)
    move_mouse(replay_button_cord[0], replay_button_cord[1])
    if data['wizard_info']['wizard_energy'] < 8:
        refill_count += 1
        print('Refill Count ')
        print(refill_count)
        if refill_count == refill_count_limit:
            sys.exit()
            shutdown()
        time.sleep(5)
        move_mouse(refill_button_cord[0], refill_button_cord[1])
        time.sleep(5)
        move_mouse(refill_button_cord[0], refill_button_cord[1])
        time.sleep(5)
        move_mouse(refill_button_cord[0], refill_button_cord[1])
        time.sleep(5)
        move_mouse(refill_button_cord[0], refill_button_cord[1])
        time.sleep(5)
        move_mouse(refill_shop_exit_cord[0], refill_shop_exit_cord[1])
        move_mouse(replay_button_cord[0], replay_button_cord[1])
    run_count += 1
    print(run_count)
    return jsonify({"message": "Good Response"})


app.run()
