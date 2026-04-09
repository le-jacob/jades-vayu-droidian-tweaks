#!/bin/python3

import os, sys, time

#basic config
delay = 10
file_path = "/tmp/phosh-brightness-level"
default_brightness = "100"
backlight_file = "/sys/class/backlight/panel0-backlight/bl_power"


print("MUST BE RAN WITH ROOT!")

no_loop = False
if len(sys.argv) > 1:
    levelfile = open(file_path, "w")
    levelfile.write(sys.argv[1])
    levelfile.close()
    no_loop = True

#wait for phosh stuff
os.system("""
kbd_loaded="$(pgrep -ac "wvkbd|osk")"
while [ "${kbd_loaded}" -eq "0" ]; do
    echo "Waiting for keyboard" | tee -a "${ADAPTATION_LOG}"
    sleep 3
    kbd_loaded="$(pgrep -ac "wvkbd|osk")"
done""")


while True:
    if os.path.isfile(file_path):
    	level = open(file_path, "r").read()
    else:
        level = default_brightness

    with open(backlight_file, "r") as f:
        value = f.read()
        f.close()
    if int(value) > 0:
        time.sleep(delay)
        continue

    os.system('''
    bright_max="4095"
    bright_lvl="$1"

    [ -z "${bright_lvl}" ]''' + f''' && bright_lvl="{level}"''' + '''

    [ "${bright_lvl}" -gt "0" ] || exit 1

    bright_to_set=$((bright_max * bright_lvl / 100))

    echo "bright_max = ${bright_max}" | tee -a "${ADAPTATION_LOG}"
    echo "bright_to_set = ${bright_to_set}" | tee -a "${ADAPTATION_LOG}"
    echo "bright_lvl = ${bright_lvl}" | tee -a "${ADAPTATION_LOG}"

    echo "${bright_to_set}" | tee /sys/class/backlight/backlight/brightness
    echo "${bright_to_set}" | tee /sys/class/backlight/panel0-backlight/brightness
    ''')
    if no_loop:
        exit()
    time.sleep(delay)
