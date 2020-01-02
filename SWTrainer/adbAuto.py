import adbutils

replay_button_cord = [500, 500]


adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
print(adb.devices())

output = adb.connect("127.0.0.1:5555")
print(output)

d = adb.device(serial="emulator-5554")
# d.keyevent("HOME")
d.click(replay_button_cord[0], replay_button_cord[1])