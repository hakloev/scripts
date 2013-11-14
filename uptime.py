import os
import subprocess

def getRawUptime():
    rawInput = subprocess.Popen("uptime", stdout=subprocess.PIPE, shell=True)
    (out, err) = rawInput.communicate()
    stringStriped = out.rstrip('\n')
    prefix, postfix = stringStriped.find('up') + 3, stringStriped.find('up') + 5
    return int(stringStriped[prefix:postfix])
        
def checkUptime(time):
    if (time >= 10):
        os.system("echo Reboot? Uptime is now " + str(time) + " days | wall")

checkUptime(getRawUptime())

