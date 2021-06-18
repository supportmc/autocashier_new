import json
import os
import sys
from time import sleep

#------IMPORTO DE ACUERDO AL MODULO ACTIVO--------------------
sys.path.append('/home/pi/Autocashier/')
import pointer
os.chdir('/home/pi/Autocashier/')
data=pointer.CheckPointer()    
sys.path.append('/home/pi/Autocashier/'+str(data['SPCA'])+'/') #importa aplicacion y vista actual
rutaPrincipal='/home/pi/Autocashier/'+str(data['SPCA'])+'/'
sys.path.append(rutaPrincipal)
#-------------------------------------------------------------


#import ViewM
#primer punto Soft
#segundo punto Modulo
#tercer modificaciones de app
Version='022.010.001.001'

JsonPosnet=""
FirstStart=True

#terminalId
#MerchandId
#tax


def GetJsonPosnet():
    global JsonPosnet
    if JsonPosnet=='':
        JsonPosnet=Read_PosnetJson()
    return JsonPosnet

def SetJsonPosnet(q):
    global JsonPosnet
    JsonPosnet=q


def SavePosnet():
    global JsonPosnet
    try:
        
        filename=rutaPrincipal +'posnet.json'      
        
        data = JsonPosnet#Read_Posnet()
        if data=='':
            return False
        

        data['Posnet'] = 0

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False   

def ClosePosnet():
    global JsonPosnet
    try:
        
        filename=rutaPrincipal +'posnet.json'      
        
        data = JsonPosnet#Read_Posnet()
        if data=='':
            return False
        

        data['Posnet'] = 0

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False   


def GetVersion():
    return(str(Version))

def Read_PosnetJson():
    global JsonPosnet
    try:
        with open(rutaPrincipal +'posnet.json') as json_file:
            JsonPosnet = json.loads(json_file.read())        
        #print(mijson)
        return JsonPosnet
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return('')

def Read_Posnet():
    global JsonPosnet
    try:
        with open('posnet.json') as json_file:
            mijson = json.loads(json_file.read())
            JsonPosnet=Read_PosnetJson() #actualizo JsonGral        
        
        return mijson['Posnet']
    

    except Exception as error:
        print(error)
        return('')


        
    
    