#APP DESARROLLADA POR  Ezequiel Ciccotelli - 2019 ---Con su respectivos modulos.
from time import sleep
import os,sys #import dyn modules

#-----------------------------------------------------------------
#importa modulos de magnetic cash
import CustomerM022002001001,SetupM022003001001,UpgradeM022004001001,DownloadM022005001001
import CounterM022001001001
import mview022005001001
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
#JsonSetup=""
#-----------------------------------------

""" def Read_Setup():
    global JsonSetup
    try:
        with open('setup.json') as json_file:
            JsonSetup = json.loads(json_file.read())        
        #print(mijson)
        return JsonSetup
    #Total_Start=mijson["Total_Start"]

    
    except Exception as error:
        print(error)
        return('')    """    
""" def CloseSetup():
    global JsonSetup
    try:
        
        filename='setup.json'            
        
        data = JsonSetup#Read_Setup()
        if data=='':
            return False
        

        data['Setup'] = 0

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False    """

""" def GetSetupJson():
    global JsonSetup
    return JsonSetup """
def GetVersion():
    return(str(Version))

def CloseApp():
    AppClose=True

def Start():
    while True:
        try:
            Setup=SetupM022003001001.Read_Setup()
            print ('Setup '+ str(Setup))
            if Setup==0:
                UpgradeM022004001001.CheckUpgrade()
            else:
                CloseApp()
                
                SetupM022003001001.Show(GetVersion())
            sleep(3)
        except Exception as e:
            print(str(e))
            continue

#start App-----------------------------------------
print('Welcome to Magnetic Cash Autocashier Software')
print('Starting SPCA ...')
sleep(1)
if CounterM022001001001.Change_CounterStart()==True:
    print('CounterModule --> OK')
else:
    print('CounterModule --> Error')


print('Checking Versions....')
print("SPCA Version ->"+ GetVersion())
print("CounterModule Version ->"+ CounterM022001001001.GetVersion())
print("CustomerModule Version ->"+ CustomerM022002001001.GetVersion())
print("SetupModule Version ->"+ SetupM022003001001.GetVersion())
print("UpgradeModule Version ->"+ UpgradeM022004001001.GetVersion())
print("DownloadModule Version ->"+ DownloadM022005001001.GetVersion())

Customer=CustomerM022002001001.Read_Customer()
print ('Customer '+ Customer)
Start()



