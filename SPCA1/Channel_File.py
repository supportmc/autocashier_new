import json
import os
from time import sleep
import sys

#------IMPORTO DE ACUERDO AL MODULO ACTIVO--------------------
sys.path.append('/home/pi/Autocashier/')
import pointer
os.chdir('/home/pi/Autocashier/')
data=pointer.CheckPointer()    
sys.path.append('/home/pi/Autocashier/'+str(data['SPCA'])+'/') #importa aplicacion y vista actual
rutaPrincipal='/home/pi/Autocashier/'+str(data['SPCA'])+'/'
sys.path.append(rutaPrincipal)
#-------------------------------------------------------------

#import BoardModule
#primer punto Soft
#segundo punto Modulo
#tercer modificaciones de app
Version='001'

JsonChannelFile=""


def GetJsonChannel():
    global JsonChannelFile
    if JsonChannelFile=='':
        JsonChannelFile=Read_ChannelJson()
    return JsonChannelFile

def Read_ChannelJson():
    global JsonChannelFile
    try:
        with open(rutaPrincipal+'channel.json') as json_file:
            JsonChannelFile = json.loads(json_file.read())        
        #print(mijson)
        return JsonChannelFile
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return('')

