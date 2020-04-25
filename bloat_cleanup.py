import re
import os
import subprocess

def debloat():
    with open('pkg.list', 'r') as p_file:
        for line in p_file:
            if str(line).startswith('-package'):
                apk = str(line).split(":")[1]
                apk = str(apk).strip()
                # uncomment below line to uninstall the bloat apps
                cmd = "adb shell pm uninstall --user 0 {}".format(apk)
                # uncomment below line to install bloat back if something goes wrong
                # cmd = "adb shell cmd package install-existing {}".format(apk)
                out_data = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read().decode()
                print("Uninstalled {}: {}".format(apk, out_data))

        p_file.close()


debloat()
