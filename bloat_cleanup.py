import re
import os
import subprocess

def cleanup():
    with open('pkg.list', 'r') as p_file:
        for line in p_file:
            if str(line).startswith('-package'):
                apk = str(line).split(":")[1]
                apk = str(apk).strip()
                cmd = "adb shell pm uninstall --user 0 {}".format(apk)
                # cmd = "adb shell cmd package install-existing {}".format(apk)
                out_data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                print("Uninstalled {}: {}".format(apk, out_data))

        p_file.close()


cleanup()
