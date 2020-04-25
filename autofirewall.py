#!/usr/bin/python
# AutoFirewall Layer4/Layer3 Protec/Shld.
# Coded by Ertugrul TURAN / T13R
# NinjaNetwork - www.Obir.Ninja
import os
import time
timer = time.sleep
os.system("clear")
timer(0.25)
os.system("curl -O http://www.inetbase.com/scripts/ddos/install.sh || wget http://www.inetbase.com/scripts/ddos/install.sh")
os.system("screen bash install.sh > /dev/null 2>/dev/null &")
print("Waiting..")
timer(5.25)
os.system("pkill screen")
os.system("curl -O http://www.rfxn.com/downloads/apf-current.tar.gz || wget http://www.rfxn.com/downloads/apf-current.tar.gz")
os.system("tar -xzf apf-current.tar.gz")
os.system("rm -rf apf-current.tar.gz")
os.system("mv apf-1.7.6 .fw")
os.system("bash .fw/install.sh")
os.system("clear")
#BANNER
        print("\n         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        timer(0.25)
        print("         ┃             NinjaNetwork Project               ┃")
        timer(0.25)
        print("         ┃             GITHUB: @obirninja                 ┃")
        timer(0.25)
        print("         ┃             Web: https://obir.ninja            ┃")
        timer(0.25)
        print("         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
        timer(0.25)
timer(1.25)
print("Edit Rule /usr/local/ddos/ddos.conf")
