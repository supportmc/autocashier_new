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

ExchangeFile=""
DivisaActual={}

def GetExchange():
    global ExchangeFile
    global DivisaActual
    if ExchangeFile=='':
        ExchangeFile=Read_Exchange()
    for divisa in ExchangeFile['exchange']:
        if divisa['Local_Currency']:
            DivisaActual={"currency":'"'+ divisa['currency'] +'"',"NUM_ISO":'"'+ divisa['NUM_ISO'] +'"',"Exchange": divisa['Exchange'] ,"Local_Currency":divisa['Local_Currency']}
    return ExchangeFile

def Read_Exchange():
    global ExchangeFile
    try:
        with open(rutaPrincipal+'exchange.json') as json_file:
            ExchangeFile = json.loads(json_file.read())        
        #print(mijson)
        return ExchangeFile
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return('')
#canales=GetExchangeChannel()

#GetExchange()