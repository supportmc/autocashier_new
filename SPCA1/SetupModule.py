import json
import os
from time import sleep
import mview
#primer punto Soft
#segundo punto Modulo
#tercer modificaciones de app
Version='022.003.001.001'

JsonSetup=""
FirstStart=True

def GetJsonSetup():
    global JsonSetup
    if JsonSetup=='':
        JsonSetup=Read_SetupJson()
    return JsonSetup

def SetJsonSetup(q):
    global JsonSetup
    JsonSetup=q


def SaveSetup():
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
        return False   

def CloseSetup():
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
        return False   


def GetVersion():
    return(str(Version))

def Read_SetupJson():
    global JsonSetup
    try:
        with open('setup.json') as json_file:
            JsonSetup = json.loads(json_file.read())        
        #print(mijson)
        return JsonSetup
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return('')

def Read_Setup():
    global JsonSetup
    try:
        with open('setup.json') as json_file:
            mijson = json.loads(json_file.read())
            JsonSetup=Read_SetupJson() #actualizo JsonGral        
        
        return mijson['Setup']
    

    except Exception as error:
        print(error)
        return('')

def Show(sversion):
    global FirstStart
    #while True:
    # Read_Setup()==1:
    #    sleep(1)
    #    print("showing Setup Screen")
    #if FirstStart==True:
    mview.creoVentana(sversion)
   #     FirstStart=False
    #else:
    #    mview.muestraVentana()

        
    
    