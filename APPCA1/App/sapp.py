#primer punto Soft
#segundo punto App
#tercer modificaciones de app
Version='022.101.001.001'
import sys
#----------------------------------------------------------------------------------
#importo puntero
sys.path.append('/home/pi/Autocashier/')
import pointer
data=pointer.CheckPointer()
sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/View/')
import sview
import functions
import database
from time import sleep
from datetime import datetime
import threading
#------
sys.path.append("/home/pi/Autocashier/"+data['SPCA'])
#import SetupM
import Exchange_File


def GetVersion():
    return(str(Version))






def Start():
    
    #read current Divise
    if Exchange_File.ExchangeFile=='':
        Exchange_File.GetExchange()
    
    #save event in database
    event='{"tipo":"Special","timestamp":"'+str(datetime.now())+'"}'
    eventSpecial='{"App_Version_Name":"","App_Version_Number":"'+GetVersion()+'","Event":"Open_App","Loc_Currency_Type":'+str(Exchange_File.DivisaActual['currency'])+'}'#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
    database.saveHistoryEvent(event,eventSpecial,'special')

    sview.creoVentana()
    """ while 1:

        ruta='index.html?nfc=1&mercadoPago=1?insertCash=1&swipeCard=1&card=1&scanApp=1&newCard=1&saldo='+ str(functions.SALDO) +'&simbolo=$'#'C:\\Users\\LP\\Documents\\Interface_2020\\CajeroNuevo\\setup.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
        sview.CambioVentana(ruta)
        functions.LeerFiat=True
        functions.LeerIngresoFiat()
        sleep(0.1) """


