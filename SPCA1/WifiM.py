import os
import subprocess
from time import sleep


Version='022.008.001.001'

def GetVersion():
    return(str(Version))

def ChangeWifi(WIFIN,WIFIP):
    WIFIN=WIFIN.strip()
    WIFIP=WIFIP.strip()
    file=open("red.mc",'w')
    file.write('ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev'+'\n')
    file.write('update_config=1'+'\n')
    file.write('country=AR'+'\n')
    file.write('\n')
    file.write('network={'+'\n')
    file.write('    ssid="'+str(WIFIN)+'"'+'\n')
    file.write('    psk="'+str(WIFIP)+'"'+'\n')
    file.write('    key_mgmt=WPA-PSK'+'\n')
    file.write('}')
    file.flush()
    file.close()

    print(os.system("sudo rm /etc/wpa_supplicant/wpa_supplicant.conf"))
    print(os.system("sudo cp red.mc /etc/wpa_supplicant/wpa_supplicant.conf"))
    print(os.system("sudo wpa_cli -i wlan0 reconfigure"))
    sleep(10)
    msj=subprocess.check_output("iw dev wlan0 link|grep SSID|awk '{print $2}'",shell=True).decode('utf8')
    red=msj.strip()
    print(os.system("sudo rm red.mc"))
    if red==WIFIN:
        return True
    else:
        return False
    #print('Ahora esta conectado a '+red)

#print(ChangeWifi('InitController','5050505050'))




