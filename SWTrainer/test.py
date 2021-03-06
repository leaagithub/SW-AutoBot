import os
import sys
import time
import adbutils
from SWTrainer.bluestack_settings import *
from ppadb.client import Client as AdbClient

emulator_id = "emulator-5554"
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())
d = adb.device(serial=emulator_id)
output = adb.connect("127.0.0.1:5555")
print(output)
url = "https://discord.com/api/webhooks/658413169420664832/7mVV_FmhuQD4tBM6-4vSsP9ZR8onBRA0wH-jhzrPWIX3I_c1MI5w9eoZ8_QCWPtXIzP-"


def move_mouse(x, y):
    time.sleep(.5)
    d.click(x, y)
    time.sleep(.5)


def refill_energy_auto_func():
    time.sleep(5)
    move_mouse(refill_energy_auto[0], refill_energy_auto[1])
    time.sleep(5)
    move_mouse(shop_auto[0], shop_auto[1])
    time.sleep(5)
    move_mouse(store_energy_auto[0], store_energy_auto[1])
    time.sleep(5)
    move_mouse(yes_auto[0], yes_auto[1])
    time.sleep(5)
    move_mouse(ok_auto[0], ok_auto[1])
    time.sleep(5)
    move_mouse(exit_energy_store_auto[0], exit_energy_store_auto[1])


test = {'command': 'BattleDungeonResult_V2', 'ret_code': 0, 'win_lose': 1,
        'wizard_info': {'wizard_id': 15286762, 'wizard_name': 'Teambunbun', 'wizard_mana': 39752221,
                        'wizard_crystal': 3389, 'wizard_crystal_paid': 2768, 'wizard_last_login': '2020-08-31 17:05:38',
                        'wizard_last_country': 'US', 'wizard_last_lang': 'en', 'wizard_level': 50,
                        'experience': 3800000, 'wizard_energy': 22, 'energy_max': 100, 'energy_per_min': 0.26,
                        'next_energy_gain': 46, 'arena_energy': 2, 'arena_energy_max': 10,
                        'arena_energy_next_gain': 857, 'unit_slots': {'number': 120}, 'rep_unit_id': 10301252264,
                        'rep_assigned': 1, 'pvp_event': 0, 'mail_box_event': 0, 'social_point_current': 2040,
                        'social_point_max': 3000, 'honor_point': 424, 'guild_point': 310, 'darkportal_energy': 12,
                        'darkportal_energy_max': 10, 'costume_point': 160, 'costume_point_max': 9999,
                        'honor_medal': 127, 'honor_mark': 162, 'event_coin': 195, 'lobby_master_id': 1002,
                        'emblem_master_id': 0, 'period_energy_max': 10, 'gain_exp': 1280},
        'clear_time': {'is_new_record': 0, 'current_time': 88162, 'best_time': 62145}, 'unit_list': [
        {'unit_id': 8595645172, 'wizard_id': 15286762, 'island_id': 4, 'pos_x': 12, 'pos_y': 22,
         'building_id': 177212429, 'unit_master_id': 13413, 'unit_level': 40, 'class': 6, 'con': 615, 'atk': 900,
         'def': 461, 'spd': 103, 'resist': 15, 'accuracy': 0, 'critical_rate': 15, 'critical_damage': 50,
         'experience': 1005420, 'exp_gained': 0, 'exp_gain_rate': 0, 'skills': [[4703, 5], [4708, 5], [4713, 5]],
         'runes': [{'rune_id': 14062541465, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 8595645172,
                    'slot_no': 1, 'rank': 5, 'class': 6, 'set_id': 8, 'upgrade_limit': 15, 'upgrade_curr': 15,
                    'base_value': 451725, 'sell_value': 32179, 'pri_eff': [3, 160], 'prefix_eff': [8, 6],
                    'sec_eff': [[2, 10, 1, 7], [10, 18, 0, 0], [9, 10, 0, 0], [4, 7, 0, 7]], 'extra': 4},
                   {'rune_id': 17558829275, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 8595645172,
                    'slot_no': 5, 'rank': 5, 'class': 6, 'set_id': 8, 'upgrade_limit': 15, 'upgrade_curr': 15,
                    'base_value': 380400, 'sell_value': 27098, 'pri_eff': [1, 2448], 'prefix_eff': [3, 10],
                    'sec_eff': [[4, 20, 0, 10], [8, 12, 0, 4], [10, 11, 0, 0], [9, 7, 1, 0]], 'extra': 5},
                   {'rune_id': 17756475505, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 8595645172,
                    'slot_no': 6, 'rank': 5, 'class': 6, 'set_id': 8, 'upgrade_limit': 15, 'upgrade_curr': 15,
                    'base_value': 404175, 'sell_value': 28792, 'pri_eff': [4, 63], 'prefix_eff': [12, 7],
                    'sec_eff': [[10, 18, 0, 0], [9, 6, 1, 0], [8, 6, 0, 2], [11, 7, 0, 0]], 'extra': 3},
                   {'rune_id': 25403212881, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 8595645172,
                    'slot_no': 4, 'rank': 5, 'class': 6, 'set_id': 8, 'upgrade_limit': 15, 'upgrade_curr': 15,
                    'base_value': 370890, 'sell_value': 26421, 'pri_eff': [10, 80], 'prefix_eff': [0, 0],
                    'sec_eff': [[4, 28, 0, 7], [8, 7, 1, 4], [6, 6, 0, 6], [3, 18, 0, 25]], 'extra': 5},
                   {'rune_id': 32233789826, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 8595645172,
                    'slot_no': 2, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 15,
                    'base_value': 412100, 'sell_value': 29357, 'pri_eff': [4, 63], 'prefix_eff': [0, 0],
                    'sec_eff': [[10, 18, 0, 0], [5, 13, 0, 0], [3, 17, 0, 0], [6, 6, 0, 0]], 'extra': 3},
                   {'rune_id': 32233803074, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 8595645172,
                    'slot_no': 3, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 12,
                    'base_value': 356625, 'sell_value': 25405, 'pri_eff': [5, 118], 'prefix_eff': [1, 165],
                    'sec_eff': [[9, 16, 0, 0], [12, 8, 0, 0], [10, 13, 0, 0], [8, 6, 0, 0]], 'extra': 4}],
         'artifacts': [
             {'rid': 978905, 'wizard_id': 15286762, 'occupied_id': 8595645172, 'slot': 1, 'type': 1, 'attribute': 3,
              'unit_style': 0, 'natural_rank': 3, 'rank': 5, 'level': 12, 'pri_effect': [100, 880, 12, 0, 0],
              'sec_effects': [[200, 5, 0, 0, 2], [219, 10, 2, 0, 0], [220, 2, 0, 0, 0], [221, 24, 0, 0, 0]],
              'locked': 0, 'source': 50001, 'extra': [], 'date_add': '2020-08-01 02:32:16',
              'date_mod': '2020-08-02 20:32:12'},
             {'rid': 2902739, 'wizard_id': 15286762, 'occupied_id': 8595645172, 'slot': 2, 'type': 2, 'attribute': 0,
              'unit_style': 1, 'natural_rank': 3, 'rank': 5, 'level': 12, 'pri_effect': [100, 880, 12, 0, 0],
              'sec_effects': [[408, 4, 0, 0, 0], [402, 13, 2, 0, 0], [205, 2, 0, 0, 0], [404, 5, 0, 0, 0]], 'locked': 0,
              'source': 50001, 'extra': [], 'date_add': '2020-08-02 05:19:31', 'date_mod': '2020-08-03 05:21:09'}],
         'costume_master_id': 0, 'trans_items': [], 'attribute': 3, 'create_time': '2017-02-14 05:04:26', 'source': 5,
         'homunculus': 0, 'homunculus_name': '', 'awakening_info': []},
        {'unit_id': 4130825101, 'wizard_id': 15286762, 'island_id': 4, 'pos_x': 22, 'pos_y': 16, 'building_id': 0,
         'unit_master_id': 10333, 'unit_level': 40, 'class': 6, 'con': 692, 'atk': 648, 'def': 692, 'spd': 111,
         'resist': 15, 'accuracy': 0, 'critical_rate': 15, 'critical_damage': 50, 'experience': 1005420,
         'exp_gained': 0, 'exp_gain_rate': 0, 'skills': [[1353, 1], [1358, 1], [1363, 1]], 'runes': [
            {'rune_id': 21577041644, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4130825101, 'slot_no': 4,
             'rank': 5, 'class': 6, 'set_id': 6, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 456480,
             'sell_value': 31053, 'pri_eff': [2, 63], 'prefix_eff': [9, 6],
             'sec_eff': [[10, 7, 0, 0], [8, 14, 0, 3], [12, 4, 0, 0], [6, 8, 1, 4]], 'extra': 3},
            {'rune_id': 25234899913, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4130825101, 'slot_no': 6,
             'rank': 5, 'class': 6, 'set_id': 10, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 592790,
             'sell_value': 29639, 'pri_eff': [2, 63], 'prefix_eff': [0, 0],
             'sec_eff': [[12, 12, 0, 0], [8, 18, 0, 2], [9, 4, 0, 0], [10, 7, 0, 0]], 'extra': 5},
            {'rune_id': 30972300981, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4130825101, 'slot_no': 5,
             'rank': 5, 'class': 6, 'set_id': 6, 'upgrade_limit': 15, 'upgrade_curr': 12, 'base_value': 405760,
             'sell_value': 27602, 'pri_eff': [1, 1800], 'prefix_eff': [6, 5],
             'sec_eff': [[8, 17, 0, 4], [12, 14, 0, 0], [9, 4, 0, 0], [2, 10, 1, 6]], 'extra': 4},
            {'rune_id': 31822521312, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4130825101, 'slot_no': 2,
             'rank': 15, 'class': 16, 'set_id': 10, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 912960,
             'sell_value': 45648, 'pri_eff': [8, 42], 'prefix_eff': [4, 8],
             'sec_eff': [[2, 6, 0, 0], [12, 24, 0, 0], [11, 4, 0, 0], [3, 10, 0, 0]], 'extra': 13},
            {'rune_id': 32321142214, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4130825101, 'slot_no': 3,
             'rank': 15, 'class': 16, 'set_id': 10, 'upgrade_limit': 15, 'upgrade_curr': 12, 'base_value': 627660,
             'sell_value': 31383, 'pri_eff': [5, 118], 'prefix_eff': [0, 0],
             'sec_eff': [[11, 10, 0, 0], [8, 18, 0, 4], [2, 13, 0, 8], [1, 190, 0, 0]], 'extra': 14},
            {'rune_id': 32339681489, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4130825101, 'slot_no': 1,
             'rank': 15, 'class': 15, 'set_id': 10, 'upgrade_limit': 15, 'upgrade_curr': 12, 'base_value': 383724,
             'sell_value': 21318, 'pri_eff': [3, 99], 'prefix_eff': [0, 0],
             'sec_eff': [[8, 16, 0, 3], [2, 5, 0, 5], [11, 9, 0, 0], [1, 453, 0, 0]], 'extra': 15}], 'artifacts': [
            {'rid': 6054271, 'wizard_id': 15286762, 'occupied_id': 4130825101, 'slot': 2, 'type': 2, 'attribute': 0,
             'unit_style': 4, 'natural_rank': 4, 'rank': 5, 'level': 12, 'pri_effect': [100, 880, 12, 0, 0],
             'sec_effects': [[408, 6, 0, 0, 0], [205, 10, 2, 0, 0], [405, 11, 1, 0, 0], [400, 6, 0, 0, 0]], 'locked': 0,
             'source': 50001, 'extra': [], 'date_add': '2020-08-04 05:44:13', 'date_mod': '2020-08-12 05:22:41'}],
         'costume_master_id': 0, 'trans_items': [], 'attribute': 3, 'create_time': '2015-07-16 12:58:15', 'source': 6,
         'homunculus': 0, 'homunculus_name': '', 'awakening_info': []},
        {'unit_id': 10301252264, 'wizard_id': 15286762, 'island_id': 4, 'pos_x': 7, 'pos_y': 14, 'building_id': 0,
         'unit_master_id': 14715, 'unit_level': 40, 'class': 6, 'con': 747, 'atk': 856, 'def': 538, 'spd': 99,
         'resist': 15, 'accuracy': 0, 'critical_rate': 15, 'critical_damage': 50, 'experience': 1005420,
         'exp_gained': 0, 'exp_gain_rate': 0, 'skills': [[6516, 5], [6510, 6], [6515, 1]], 'runes': [
            {'rune_id': 8148130663, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 10301252264, 'slot_no': 2,
             'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 412100,
             'sell_value': 29357, 'pri_eff': [8, 42], 'prefix_eff': [0, 0],
             'sec_eff': [[10, 10, 0, 0], [9, 12, 0, 0], [4, 9, 1, 0], [2, 18, 0, 7]], 'extra': 5},
            {'rune_id': 21211441395, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 10301252264,
             'slot_no': 1, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 12,
             'base_value': 391495, 'sell_value': 27889, 'pri_eff': [3, 118], 'prefix_eff': [0, 0],
             'sec_eff': [[11, 6, 0, 0], [8, 22, 0, 4], [2, 6, 0, 7], [4, 5, 0, 3]], 'extra': 4},
            {'rune_id': 21780936285, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 10301252264,
             'slot_no': 4, 'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 684720, 'sell_value': 34236, 'pri_eff': [10, 80], 'prefix_eff': [1, 302],
             'sec_eff': [[8, 16, 0, 0], [6, 5, 0, 0], [2, 8, 0, 0], [5, 10, 0, 0]], 'extra': 3},
            {'rune_id': 21826767759, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 10301252264,
             'slot_no': 3, 'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 523050, 'sell_value': 26152, 'pri_eff': [5, 160], 'prefix_eff': [0, 0],
             'sec_eff': [[9, 10, 0, 0], [6, 14, 0, 0], [8, 10, 0, 0], [2, 10, 0, 0]], 'extra': 5},
            {'rune_id': 22205969905, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 10301252264,
             'slot_no': 6, 'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 592790, 'sell_value': 29639, 'pri_eff': [4, 63], 'prefix_eff': [0, 0],
             'sec_eff': [[2, 10, 1, 0], [6, 6, 0, 0], [9, 10, 0, 0], [8, 21, 0, 3]], 'extra': 5},
            {'rune_id': 31973162542, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 10301252264,
             'slot_no': 5, 'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 12,
             'base_value': 608640, 'sell_value': 30432, 'pri_eff': [1, 1800], 'prefix_eff': [2, 7],
             'sec_eff': [[12, 18, 0, 0], [8, 14, 0, 0], [5, 19, 0, 0], [10, 7, 0, 0]], 'extra': 5}], 'artifacts': [
            {'rid': 983657, 'wizard_id': 15286762, 'occupied_id': 10301252264, 'slot': 1, 'type': 1, 'attribute': 5,
             'unit_style': 0, 'natural_rank': 3, 'rank': 3, 'level': 6, 'pri_effect': [102, 34, 6, 0, 0],
             'sec_effects': [[218, 0.5, 1, 0, 0], [219, 7, 1, 0, 0]], 'locked': 0, 'source': 50001, 'extra': [],
             'date_add': '2020-08-01 02:35:16', 'date_mod': '2020-08-01 05:45:19'},
            {'rid': 14707609, 'wizard_id': 15286762, 'occupied_id': 10301252264, 'slot': 2, 'type': 2, 'attribute': 0,
             'unit_style': 1, 'natural_rank': 4, 'rank': 5, 'level': 15, 'pri_effect': [100, 1500, 15, 0, 0],
             'sec_effects': [[401, 9, 1, 0, 0], [408, 5, 0, 0, 0], [406, 13, 2, 0, 0], [202, 5, 0, 0, 1]], 'locked': 0,
             'source': 50001, 'extra': [], 'date_add': '2020-08-12 03:19:50', 'date_mod': '2020-08-15 11:41:30'}],
         'costume_master_id': 16505, 'trans_items': [], 'attribute': 5, 'create_time': '2017-10-16 08:01:15',
         'source': 5, 'homunculus': 0, 'homunculus_name': '', 'awakening_info': []},
        {'unit_id': 4138270260, 'wizard_id': 15286762, 'island_id': 4, 'pos_x': 5, 'pos_y': 8, 'building_id': 177212429,
         'unit_master_id': 11533, 'unit_level': 40, 'class': 6, 'con': 758, 'atk': 549, 'def': 725, 'spd': 111,
         'resist': 15, 'accuracy': 0, 'critical_rate': 15, 'critical_damage': 50, 'experience': 1005420,
         'exp_gained': 0, 'exp_gain_rate': 0, 'skills': [[2553, 1], [2558, 1], [2563, 1]], 'runes': [
            {'rune_id': 7053896796, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4138270260, 'slot_no': 6,
             'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 592790,
             'sell_value': 29639, 'pri_eff': [12, 64], 'prefix_eff': [0, 0],
             'sec_eff': [[10, 6, 0, 0], [9, 17, 0, 0], [8, 12, 0, 3], [4, 7, 0, 6]], 'extra': 0},
            {'rune_id': 18886592967, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4138270260, 'slot_no': 4,
             'rank': 5, 'class': 6, 'set_id': 6, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 456480,
             'sell_value': 31053, 'pri_eff': [10, 80], 'prefix_eff': [6, 5],
             'sec_eff': [[9, 26, 0, 0], [2, 8, 0, 6], [8, 5, 1, 3], [12, 8, 0, 0]], 'extra': 5},
            {'rune_id': 21718482821, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4138270260, 'slot_no': 3,
             'rank': 5, 'class': 6, 'set_id': 6, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 332850,
             'sell_value': 22642, 'pri_eff': [5, 160], 'prefix_eff': [0, 0],
             'sec_eff': [[8, 20, 0, 5], [9, 5, 0, 0], [12, 4, 0, 0], [1, 387, 0, 504]], 'extra': 5},
            {'rune_id': 21854103463, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4138270260, 'slot_no': 5,
             'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 608640,
             'sell_value': 30432, 'pri_eff': [1, 2448], 'prefix_eff': [4, 8],
             'sec_eff': [[8, 17, 0, 3], [5, 30, 0, 0], [9, 6, 0, 0], [12, 12, 0, 0]], 'extra': 5},
            {'rune_id': 22117534162, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4138270260, 'slot_no': 2,
             'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 15, 'base_value': 697400,
             'sell_value': 34870, 'pri_eff': [8, 42], 'prefix_eff': [0, 0],
             'sec_eff': [[9, 16, 0, 0], [1, 224, 0, 0], [2, 8, 0, 0], [11, 8, 0, 0]], 'extra': 3},
            {'rune_id': 31820282945, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 4138270260, 'slot_no': 1,
             'rank': 5, 'class': 6, 'set_id': 13, 'upgrade_limit': 15, 'upgrade_curr': 12, 'base_value': 722760,
             'sell_value': 36138, 'pri_eff': [3, 118], 'prefix_eff': [11, 7],
             'sec_eff': [[4, 8, 1, 6], [9, 9, 0, 0], [8, 15, 0, 3], [10, 5, 0, 0]], 'extra': 4}], 'artifacts': [
            {'rid': 6088427, 'wizard_id': 15286762, 'occupied_id': 4138270260, 'slot': 2, 'type': 2, 'attribute': 0,
             'unit_style': 4, 'natural_rank': 5, 'rank': 5, 'level': 12, 'pri_effect': [102, 58, 12, 0, 0],
             'sec_effects': [[206, 10, 1, 0, 0], [221, 85, 2, 0, 0], [205, 2, 0, 0, 0], [218, 0.3, 1, 0, 0]],
             'locked': 0, 'source': 50001, 'extra': [], 'date_add': '2020-08-04 06:16:29',
             'date_mod': '2020-08-04 07:27:33'},
            {'rid': 6825143, 'wizard_id': 15286762, 'occupied_id': 4138270260, 'slot': 1, 'type': 1, 'attribute': 3,
             'unit_style': 0, 'natural_rank': 4, 'rank': 5, 'level': 15, 'pri_effect': [100, 1500, 15, 0, 0],
             'sec_effects': [[306, 16, 3, 0, 0], [309, 6, 0, 0, 0], [219, 2, 0, 0, 0], [200, 3, 0, 0, 2]], 'locked': 0,
             'source': 50001, 'extra': [], 'date_add': '2020-08-04 19:52:29', 'date_mod': '2020-08-05 05:48:09'}],
         'costume_master_id': 0, 'trans_items': [], 'attribute': 3, 'create_time': '2015-07-17 06:35:11', 'source': 14,
         'homunculus': 0, 'homunculus_name': '', 'awakening_info': []},
        {'unit_id': 14049374972, 'wizard_id': 15286762, 'island_id': 4, 'pos_x': 14, 'pos_y': 5, 'building_id': 0,
         'unit_master_id': 11035, 'unit_level': 40, 'class': 6, 'con': 637, 'atk': 769, 'def': 626, 'spd': 108,
         'resist': 15, 'accuracy': 0, 'critical_rate': 15, 'critical_damage': 50, 'experience': 1005420,
         'exp_gained': 0, 'exp_gain_rate': 0, 'skills': [[2055, 1], [2060, 1], [2065, 1]], 'runes': [
            {'rune_id': 7827837961, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 14049374972, 'slot_no': 3,
             'rank': 5, 'class': 6, 'set_id': 3, 'upgrade_limit': 15, 'upgrade_curr': 12, 'base_value': 332850,
             'sell_value': 22642, 'pri_eff': [5, 118], 'prefix_eff': [0, 0],
             'sec_eff': [[9, 11, 0, 0], [1, 509, 0, 0], [8, 4, 0, 0], [10, 19, 0, 0]], 'extra': 5},
            {'rune_id': 16320461758, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 14049374972,
             'slot_no': 6, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 404175, 'sell_value': 28792, 'pri_eff': [4, 63], 'prefix_eff': [8, 6],
             'sec_eff': [[9, 21, 0, 0], [12, 7, 0, 0], [10, 9, 0, 0], [1, 330, 0, 0]], 'extra': 5},
            {'rune_id': 17365658874, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 14049374972,
             'slot_no': 5, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 12,
             'base_value': 329680, 'sell_value': 23485, 'pri_eff': [1, 1800], 'prefix_eff': [0, 0],
             'sec_eff': [[4, 20, 0, 5], [10, 11, 0, 0], [3, 19, 0, 0], [5, 18, 0, 0]], 'extra': 4},
            {'rune_id': 25386282605, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 14049374972,
             'slot_no': 1, 'rank': 5, 'class': 6, 'set_id': 10, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 662530, 'sell_value': 33126, 'pri_eff': [3, 160], 'prefix_eff': [0, 0],
             'sec_eff': [[9, 10, 0, 0], [4, 21, 0, 0], [8, 6, 1, 2], [10, 14, 0, 0]], 'extra': 5},
            {'rune_id': 32164017362, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 14049374972,
             'slot_no': 2, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 475500, 'sell_value': 33873, 'pri_eff': [8, 42], 'prefix_eff': [1, 223],
             'sec_eff': [[4, 8, 0, 4], [10, 27, 0, 0], [11, 5, 0, 0], [5, 12, 0, 0]], 'extra': 4},
            {'rune_id': 32362448639, 'wizard_id': 15286762, 'occupied_type': 1, 'occupied_id': 14049374972,
             'slot_no': 4, 'rank': 5, 'class': 6, 'set_id': 4, 'upgrade_limit': 15, 'upgrade_curr': 15,
             'base_value': 427950, 'sell_value': 30486, 'pri_eff': [10, 80], 'prefix_eff': [9, 5],
             'sec_eff': [[12, 12, 0, 0], [1, 356, 0, 0], [4, 22, 0, 0], [8, 4, 0, 0]], 'extra': 4}], 'artifacts': [],
         'costume_master_id': 0, 'trans_items': [], 'attribute': 5, 'create_time': '2019-08-22 15:47:03', 'source': 9,
         'homunculus': 0, 'homunculus_name': '', 'awakening_info': []}],
        'reward': {'mana': 4880, 'crystal': 0, 'energy': 0,
                   'event_crate': {'item_master_type': 101, 'item_master_id': 10, 'item_quantity_var': 6,
                                   'item_quantity_curr': 6, 'item_quantity_max': 100}}, 'changed_item_list': [
        {'type': 8,
         'info': {'rune_id': 32853611118, 'wizard_id': 15286762, 'occupied_type': 2, 'occupied_id': 0, 'slot_no': 2,
                  'rank': 3, 'class': 6, 'set_id': 3, 'upgrade_limit': 15, 'upgrade_curr': 0, 'base_value': 317000,
                  'sell_value': 21564, 'pri_eff': [8, 7], 'prefix_eff': [6, 7], 'sec_eff': [[4, 8], [12, 7]],
                  'extra': 3},
         'view': {'item_master_type': 8, 'item_master_id': None, 'item_quantity': 1, 'unit_class': None,
                  'unit_level': None, 'rune_class': 6, 'rune_set_id': 3, 'rune_rank': 3, 'artifact_craft_type': None,
                  'artifact_craft_master_id': None, 'runecraft_type': None, 'runecraft_item_id': None,
                  'runecraft_set_id': None, 'runecraft_effect_id': None, 'runecraft_rank': None, 'artifact_type': None,
                  'artifact_attribute': None, 'artifact_unit_style': None, 'artifact_natural_rank': None,
                  'random_rune_type': None}}], 'ts_val': 1130610398, 'tvalue': 1598863445, 'tvaluelocal': 1598805845,
        'tzone': 'America/Los_Angeles'}
art = {'rid': 21137277, 'wizard_id': 15286762, 'occupied_id': 0, 'slot': 0, 'type': 2, 'attribute': 0, 'unit_style': 2,
       'natural_rank': 3, 'rank': 3, 'level': 0, 'pri_effect': [101, 10, 0, 0, 0],
       'sec_effects': [[408, 3, 0, 0, 0], [202, 3, 0, 0, 0]], 'locked': 0, 'source': 50001, 'extra': [],
       'date_add': '2020-08-21 01:25:24', 'date_mod': '2020-08-21 01:25:24'}

print(test)
print('testing')
refill_energy_auto_func()
print('done')
