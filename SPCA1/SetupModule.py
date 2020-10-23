import json
import os
from time import sleep
import mview
#primer punto Soft
#segundo punto Modulo
#tercer modificaciones de app
Version='022.003.001.001'

def GetVersion():
    return(str(Version))

def Read_Setup():
    try:
        with open('setup.json') as json_file:
            mijson = json.loads(json_file.read())        
        #print(mijson)
        return mijson['Setup']
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return('')

def Show(sversion):
    #while True:
    # Read_Setup()==1:
    #    sleep(1)
    #    print("showing Setup Screen")
    mview.creoVentana(sversion)

        
    
    