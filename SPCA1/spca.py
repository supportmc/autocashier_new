#APP DESARROLLADA POR  Ezequiel Ciccotelli - 2019 ---Con su respectivos modulos.
from time import sleep
import datetime
import os,sys #import dyn modules

#-----------------------------------------------------------------
#importa modulos de magnetic cash
import CustomerM,SetupM,UpgradeM,DownloadM
import CounterM
import ViewM
import BoardModule
#-----------------------------------------------------------------
#importo puntero
sys.path.append('/home/pi/Autocashier/')
import pointer
data=pointer.CheckPointer()
os.chdir("/home/pi/Autocashier/"+data['SPCA'])#aplica carpeta actual
sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/App/')#importo app actual
import sapp
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
    ViewM.CloseSetup()

def Start():
    while True:
        try:
            #Setup=SetupM.Read_Setup()
            #print ('Setup '+ str(Setup))
            #if Setup==0:
            if BoardModule.PuertaAbierta==False:
                UpgradeM.CheckUpgrade()
                sapp.Start()
            else:
                CloseApp()                
                ViewM.creoVentana(GetVersion())
            sleep(3)
        except Exception as e:
            print(str(e))
            filename='spca_log.json'                
            data ={"Error":str(e)}
            #os.remove(filename)
            #fo = open(filename, "wb")
            #print ("Name of the file: ", fo.name)
            #fo.close()

            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            continue

#start App-----------------------------------------
filename='spca_log.json'                
data ={"Last_Start":str(datetime.datetime.now())}
#os.remove(filename)
#fo = open(filename, "wb")
#print ("Name of the file: ", fo.name)
#fo.close()

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
print('Welcome to Magnetic Cash Autocashier Software')
print('Starting SPCA ...')
sleep(1)
if CounterM.Change_CounterStart()==True:
    print('CounterModule --> OK')
else:
    print('CounterModule --> Error')


print('Checking Versions....')
print("SPCA Version ->"+ GetVersion())
print("CounterModule Version ->"+ CounterM.GetVersion())
print("CustomerModule Version ->"+ CustomerM.GetVersion())
print("SetupModule Version ->"+ SetupM.GetVersion())
print("UpgradeModule Version ->"+ UpgradeM.GetVersion())
print("DownloadModule Version ->"+ DownloadM.GetVersion())

Customer=CustomerM.Read_Customer()
print ('Customer '+ Customer)
Start()



