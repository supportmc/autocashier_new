#APP DESARROLLADA POR  Ezequiel Ciccotelli - 2019 ---Con su respectivos modulos.
from time import sleep
import os,sys #import dyn modules

#-----------------------------------------------------------------
#importa modulos de magnetic cash
import CustomerModule,SetupModule,UpgradeModule,DownloadModule
import CounterModule 
import mview
#-----------------------------------------------------------------
#importo puntero
sys.path.append('/home/pi/Autocashier/')
import pointer
data=pointer.CheckPointer()
os.chdir("/home/pi/Autocashier/"+data['SPCA'])#aplica carpeta actual
#-----------------------------------------------------------------
import json


Version='000.022.001.001'

#------VARIABLES PARA COMPARAR VERSION ACTUAL CON LA QUE EL SISTEMA INDIQUE AL ENCENDER
AppClose=False
SPCAVersion=""
CounterModuleVersion=""
CustomerModuleVersion=""
SetupModuleVersion=""
UpgradeModuleVersion=""
DownloadModuleVersion=""
Customer=""
Setup=0

#-----------------------------------------

def GetVersion():
    return(str(Version))

def CloseApp():
    AppClose=True

def Start():
    while True:
        try:
            Setup=SetupModule.Read_Setup()
            print ('Setup '+ str(Setup))
            if Setup==0:
                UpgradeModule.CheckUpgrade()
            else:
                CloseApp()
                SetupModule.Show(GetVersion())
            sleep(3)
        except Exception as e:
            print(str(e))
            continue

print('Welcome to Magnetic Cash Autocashier Software')
print('Checking Versions....')
print("SPCA Version ->"+ GetVersion())
print("CounterModule Version ->"+ CounterModule.GetVersion())
print("CustomerModule Version ->"+ CustomerModule.GetVersion())
print("SetupModule Version ->"+ SetupModule.GetVersion())
print("UpgradeModule Version ->"+ UpgradeModule.GetVersion())
print("DownloadModule Version ->"+ DownloadModule.GetVersion())



print('Starting SPCA ...')
sleep(1)
if CounterModule.Change_CounterStart()==True:
    print('CounterModule --> OK')
else:
    print('CounterModule --> Error')

Customer=CustomerModule.Read_Customer()
print ('Customer '+ Customer)
Start()

