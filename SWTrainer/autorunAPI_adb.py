import sys
import os
import flask
import adbutils
import time
from flask import request, jsonify
from SWTrainer.bluestack_settings import *

from SWTrainer.bluestack_settings import refill_count_limit, replay_button_cord, ok_button_cord, get_rune_cord, \
    sell_rune_confirm_cord, sell_rune_cord, corner_spot_cord

os.system("bluestack_settings.py")
run_count = 0
refill_count = 0
fail_count = 0
app = flask.Flask(__name__)
app.config["DEBUG"] = True
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
output = adb.connect("127.0.0.1:5555")
print(output)
d = adb.device(serial="emulator-5554")

#C:\Program Files\BlueStacks

def __init__(self):
    pass


def rune_quality_check(rune):
    if rune['set_id'] == 15:
        print('Found will rune')
        if not keep_hp_slot(rune):
            return False
    if rune['set_id'] == 19:
        print('Found fight rune')
        if not keep_hp_slot(rune):
            return False
    if rune['set_id'] == 13:
        print('Found violent rune')
        if not keep_hp_slot(rune):
            return False
    if rune['set_id'] == 3:
        print('Found swift rune')
        if not keep_hp_slot(rune):
            return False
    if rune['set_id'] == 10:
        print('Found despair rune')
        if not keep_hp_slot(rune):
            return False
    if rune['class'] < 6:
        print('Only Keep 6 star')
        return True
    if rune['rank'] < 4:
        print('Only Keep Purples and Up')
        return True
    if rune['pri_eff'][0] == 8:
        print('Purple Spd Slot 2')
        return False
    if rune['pri_eff'][0] == 10:
        print('Purple CD Slot 4')
        return False
    if rune['pri_eff'][0] == 4 and rune['slot_no'] == 6:
        print('Purple Atk Slot 6')
        return False
    if rune['rank'] == 5:
        print('Legend 6 Star Keep')
        return False
    for subStats in rune['sec_eff']:
        if subStats[0] == 8:
            print('Found Spd Sub')
            return False
    print('Found No Spd Sub')
    for subStats in rune['sec_eff']:
        if subStats[0] == 10:
            if subStats[1] == 7:
                print('Found Max CD Roll')
                return False
    print('Found No Max CD Sub')
    return True


def ancient_rune_quality_check(rune):
    if rune['set_id'] == 10:
        print('Found despair rune')
        if not ancient_keep_spd_sub(rune):
            return False
    if rune['set_id'] == 15:
        print('Found will rune')
        if not ancient_keep_spd_sub(rune):
            return False
    if rune['class'] < 16:
        print('Only Keep 6 star')
        return True
    if rune['rank'] < 14:
        print('Only Keep Purples and Up')
        return True
    if rune['pri_eff'][0] == 8:
        print('Purple Spd Slot 2')
        return False
    if rune['rank'] == 15:
        print('Legend 6 Star Keep')
        return False
    for subStats in rune['sec_eff']:
        if subStats[0] == 8:
            print('Found Spd Sub')
            return False
    print('Found No Spd Sub')
    return True


def keep_hp_slot(rune):
    #True is pass on rune False is keep the rune
    if rune['class'] == 5:
        if rune['rank'] < 5:
            print('Not 5 star legendary')
            return True
        else:
            for subStats in rune['sec_eff']:
                if subStats[0] == 8:
                    print('Found Spd Sub')
                    if subStats[1] == 5:
                        print('Found Spd Sub 5')
                        return False
            print('Checked subs and there is no spd 5')
            return True
    for subStats in rune['sec_eff']:
        if subStats[0] == 8:
            print('6 star rune spd sub keep')
            return False
    print('Found No Spd Sub return bad')
    return True


def ancient_keep_hp_slot(rune):
    if rune['slot_no'] == 4 or rune['slot_no'] == 6:
        print('Found Slot 4/6')
        if rune['rank'] < 14 & rune['class'] < 16:
            print('Only Keep Purples and Up & 6 star runes')
            if rune['pri_eff'][0] == 2:
                print('Prim Eff Hp% now checking subs')
                for subStats in rune['sec_eff']:
                    if subStats[0] == 8:
                        print('Found Spd Sub keep the rune')
                        return False
                print('Found No Spd Sub return bad')
                return True
    print('bad rune not in slot 4 or 6')
    return True


def ancient_keep_spd_sub(rune):
    if rune['class'] == 15:
        if rune['rank'] < 15:
            print('Not 5 star legendary')
            return True
        else:
            for subStats in rune['sec_eff']:
                if subStats[0] == 8:
                    print('Found Spd Sub keep the rune')
                    if subStats[1] >= 5:
                        print('Found Spd Sub 5')
                        return False
            print('Checked subs and there is no spd')
            return True
    print('6 Star rune!')
    for subStats in rune['sec_eff']:
        if subStats[0] == 8:
            print('Found Spd Sub keep the rune')
            return False
    print('Found No Spd Sub not keeping rune')
    return True


def move_mouse(x, y):
    time.sleep(1)
    d.click(x, y)
    time.sleep(1)


def grab_chest():
    time.sleep(10)
    move_mouse(corner_spot_cord[0], corner_spot_cord[1])
    time.sleep(1)
    move_mouse(corner_spot_cord[0], corner_spot_cord[1])
    d.click(corner_spot_cord[0], corner_spot_cord[1])
    time.sleep(1)
    d.click(corner_spot_cord[0], corner_spot_cord[1])
    move_mouse(corner_spot_cord[0], corner_spot_cord[1])


def refill_energy():
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


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def raid_drop_check(drop):
    if drop['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_effect_id'] == 8:
        print('Keep Spd Grind')
        return True
    if drop['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_rank'] <= 3:
        print('Throw away grind blue rune')
        return False
    if drop['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_rank'] == 5:
        print('Keep legend')
        return True
    if drop['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_effect_id'] == 5 or drop['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_effect_id'] == 1 or drop['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_effect_id'] == 3:
        print('Sell Flat stats')
        return False
    return True


def fast_refill_energy():
    time.sleep(1.5)
    move_mouse(refill_button_cord[0], refill_button_cord[1])
    time.sleep(1.5)
    move_mouse(refill_button_cord[0], refill_button_cord[1])
    time.sleep(1.5)
    move_mouse(refill_button_cord[0], refill_button_cord[1])
    time.sleep(1.5)
    move_mouse(refill_button_cord[0], refill_button_cord[1])
    time.sleep(1.5)
    move_mouse(refill_shop_exit_cord[0], refill_shop_exit_cord[1])


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('/pickGuildMazeBattleClearReward/', methods=['POST'])
def guild_maze_pick():
    print(request.json)
    data = request.json
    return jsonify({"message": "Good Response"})


@app.route('/BattleDimensionHoleDungeonResult/', methods=['POST'])
def dim_hole_result():
    global run_count
    global refill_count
    data = request.json
    # print(data['reward'])
    grab_chest()
    # craft_type 6 is grindstone and 5 is gemstone Last Number is the grade of the GEM/GRIND
    print(data['reward']['crate'])
    try:
        if data['reward']['crate']['rune']:
            if ancient_rune_quality_check(data['reward']['crate']['rune']):
                print('Selling Rune!')
                move_mouse(sell_rune_cord[0], sell_rune_cord[1])
                move_mouse(sell_rune_confirm_cord[0], sell_rune_confirm_cord[1])
            else:
                move_mouse(get_rune_cord[0], get_rune_cord[1])
                print('Keeping Rune!')
                print(data['reward']['crate']['rune'])
        elif data['reward']['crate']['changestones']:
            print('Grindstone or Gemstone!')
        else:
            move_mouse(dim_hole_ok_button_cord[0], dim_hole_ok_button_cord[1])
            print('Grabbing Extra Dungeon Drop');
    except:
        move_mouse(dim_hole_ok_button_cord[0], dim_hole_ok_button_cord[1])
        # move_mouse(dim_hole_collect_grindstone[0], dim_hole_collect_grindstone[1])
    move_mouse(replay_button_cord[0], replay_button_cord[1])
    return jsonify({"message": "Good Response"})


@app.route('/BattleTrialTowerResult_v2/', methods=['POST'])
def toa_result():
    global run_count
    global refill_count
    global fail_count
    print(request.json)
    data = request.json
    if data['win_lose'] == 1:
        grab_chest()
        move_mouse(ok_button_cord[0], ok_button_cord[1])
        move_mouse(replay_button_cord[0], replay_button_cord[1])
        move_mouse(start_battle_button_cord[0], start_battle_button_cord[1])
        # refill_energy()
        # move_mouse(start_battle_button_cord[0], start_battle_button_cord[1])
    else:
        move_mouse(ok_button_cord[0], ok_button_cord[1])
        move_mouse(ok_button_cord[0], ok_button_cord[1])
        move_mouse(replay_button_cord[0], replay_button_cord[1])
        move_mouse(start_battle_button_cord[0], start_battle_button_cord[1])
        fail_count += 1
        if fail_count == fail_count_limit:
            print("Too many fails")
            sys.exit()
            shutdown()
    return jsonify({"message": "Good Response"})


@app.route('/BattleRiftDungeonResult/', methods=['POST'])
def rift_dungeons():
    global run_count
    global refill_count
    print(request.json)
    data = request.json
    print(data['item_list'][3]['type'])
    grab_chest()
    if data['item_list'][3]['type'] == 8:
        print('Found rune!')
        if rune_quality_check(data['item_list'][3]['info']):
            move_mouse(open_rune_cord[0], open_rune_cord[1])
            move_mouse(rift_sell_rune_cord[0], rift_sell_rune_cord[1])
            move_mouse(rift_sell_rune_confirm_cord[0], rift_sell_rune_confirm_cord[1])
        else:
            print('Good Rune!')
    else:
        print('Pass')
    move_mouse(closed_reward_window_cord[0], closed_reward_window_cord[1])
    time.sleep(2)
    move_mouse(replay_button_cord[0], replay_button_cord[1])
    if data['wizard_info']['wizard_energy'] < 8:
        refill_count += 1
        print('Refill Count ')
        print(refill_count)
        if refill_count == refill_count_limit:
            sys.exit()
            shutdown()
            exit()
        refill_energy()
        move_mouse(replay_button_cord[0], replay_button_cord[1])
    run_count += 1
    print(run_count)
    return jsonify({"message": "Good Response"})


@app.route('/getGuildMazeClearRewardCrateSummary/', methods=['POST'])
def guild_maze_reward():
    print(request.json)
    data = request.json
    return jsonify({"message": "Good Response"})


@app.route('/battleGuildMazeResult/', methods=['POST'])
def guild_maze_result():
    print(request.json)
    data = request.json
    # 27 Gemstone
    return jsonify({"message": "Good Response"})


@app.route('/BattleDungeonResult_V2/', methods=['POST'])
def carios_dungeon():
    global run_count
    global refill_count
    data = request.json
    grab_chest()
    print(data['changed_item_list'])
    if data['changed_item_list'][0]['type'] == 8:
        print('Found Rune!')
        print(data['changed_item_list'][0]['info'])
        if rune_quality_check(data['changed_item_list'][0]['info']):
            print('Selling Rune')
            move_mouse(sell_rune_cord[0], sell_rune_cord[1])
            move_mouse(sell_rune_confirm_cord[0], sell_rune_confirm_cord[1])
        else:
            print('Getting Rune')
            move_mouse(get_rune_cord[0], get_rune_cord[1])
    else:
        print('No Rune Found!')
        move_mouse(ok_button_cord[0], ok_button_cord[1])
    time.sleep(2)
    move_mouse(replay_button_cord[0], replay_button_cord[1])
    if data['wizard_info']['wizard_energy'] < 8:
        refill_count += 1
        print('Refill Count ')
        print(refill_count)
        if refill_count == refill_count_limit:
            sys.exit()
            shutdown()
            exit()
        refill_energy()
        move_mouse(replay_button_cord[0], replay_button_cord[1])
    run_count += 1
    print(run_count)
    return jsonify({"message": "Good Response"})


@app.route('/BattleRiftOfWorldsRaidResult/', methods=['POST'])
def raid_dungeon():
    data = request.json
    # print(data)
    print(data['battle_reward_list'][raid_player_slot]['reward_list'])
    print(data['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_type'])
    print(data['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_rank'])
    time.sleep(13)
    d.click(open_chest[0], open_chest[1])
    time.sleep(.4)
    d.click(open_chest[0], open_chest[1])
    time.sleep(.2)
    d.click(open_chest[0], open_chest[1])
    print('Done Clicks')
    if data['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_type'] == 1 or data['battle_reward_list'][raid_player_slot]['reward_list'][0]['runecraft_type'] == 2:
        print('Found Grind/Gem')
        if raid_drop_check(data):
            print('Keep')
            time.sleep(.2)
            d.click(get_grind[0], get_grind[1])
        else:
            print('Sell')
            time.sleep(.4)
            d.click(sell_grind[0], sell_grind[1])
            time.sleep(.4)
            d.click(confirm_sell_grind[0], confirm_sell_grind[1])
            time.sleep(.4)

    else:
        print('Extra Drop')
        time.sleep(.2)
        d.click(get_mana[0], get_mana[1])
    time.sleep(.2)
    d.click(restart_run[0], restart_run[1])
    if data['wizard_info']['wizard_energy'] < 9:
        print('refill')
        fast_refill_energy()
        time.sleep(1.7)
        d.click(restart_run[0], restart_run[1])
    time.sleep(1.7)
    d.click(raid_start_battle[0], raid_start_battle[1])
    return jsonify({"message": "Good Response"})


app.run()
