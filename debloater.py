import re
import os
import subprocess


def cleanup():
    with open('pkg.list.redmi-note-10', 'r') as p_file:
        for line in p_file:
            if str(line).startswith('-'):
                apk = str(line).split(":")[1]
                apk = str(apk).strip()
                if str(line).startswith('-package'):
                    cmd = "adb shell pm uninstall --user 0 {}".format(apk)
                    # cmd = "adb shell cmd package install-existing {}".format(apk)
                else:
                    cmd = "adb shell pm disable-user --user 0 {}".format(apk)
                out_data = subprocess.Popen(
                    cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                print("Uninstalled {}: {}".format(apk, out_data))

        p_file.close()


cleanup()
