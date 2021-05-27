#primer punto Soft
#segundo punto App
#tercer punto vista
#cuarto modificaciones de vista
Version='101.501.001.001'

from furl import furl #para la url en python
import webview
from time import sleep
import threading


#import App
#import view

import sys
#----------------------------------------------------------------------------------
#importo puntero
sys.path.append('/home/pi/Autocashier/')
import pointer
data=pointer.CheckPointer()
sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/App/') #importa aplicacion y vista actual
import functions
rutaVista='/home/pi/Autocashier/'+str(data['APPCA'])+'/View/'

sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/View/')

sys.path.append("/home/pi/Autocashier/"+data['SPCA'])
import BoardModule
import SetupM
#import sapp
#import sview
#import SetupM
#import start
ruta=''
nfc=''
mercadoPago=''
insertCash=''
swipeCard=''
card=''
scanApp=''
newCard=''
simbolo=''
bill1=''
bill2=''
coin=''

#-----------------------------------------------------------------------------------

import datetime
import json
import os
entro=False
x=1
entroProbador=False

def GetVersion():
    return(str(Version))


def CambioVentana():
    global softversion
    global entro
    global ruta
    # //traigo conteos de todo \\
    #softversion=sversion
    

    #Channel_File.GetJsonChannel()

    #os.chdir(start.rutaPrincipal)

    mdir=os.getcwd()
    print(mdir)
    #webview.windows[0].load_url('setup.html') 
    #Paso todo los parametros a la vista
    ruta=rutaVista+ruta
    print(ruta)
    #ruta=mdir+'/'+ruta
    #entro=False
    #window = webview.create_window('Get current URL1', ruta,fullscreen=True)
    #webview.start(change_url, window,http_server=True)
    webview.windows[0].load_url(ruta)
    webview.windows[0].show()

def creoVentana():
    global softversion
    global entro
    # //traigo conteos de todo \\
    #softversion=sversion
    

    #Channel_File.GetJsonChannel()

    #os.chdir(start.rutaPrincipal)

    mdir=os.getcwd()
    print(mdir)
    #webview.windows[0].load_url('setup.html') 
    #Paso todo los parametros a la vista
    
    ruta=rutaVista+'index.html'
    #ruta=mdir+'/'+ruta
    entro=False
    window = webview.create_window('Get current URL1', ruta,fullscreen=True)
    webview.start(change_url, window,http_server=True)
    webview.windows[0].hide()
    
    

def change_url(window):
    #global x
    a=1
    #if x==1:
        #x+=1
        #window.load_url('C:\\Users\\LP\\Documents\\Interface_2020\\CajeroNuevo\\setup.html')
    imprime()

def Read_Setup():
    try:
        with open('setup.json') as json_file:
            mijson = json.loads(json_file.read())        
        #print(mijson)
        return mijson
    #Total_Start=mijson["Total_Start"]

    
    except Exception as error:
        print(error)
        return('')       
def CloseApp():
    try:
        
        """ filename='setup.json'            
        
        data = Read_Setup()
        if data=='':
            return False
        

        data['Setup'] = 0

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4) """
        webview.windows[0].hide()
        webview.windows[0].destroy()
        
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False   

def miboleano(q):
    if q=='false':
        return False
    else:
        return True
def miboleano2(q):
    if q==True:
        return 'true'
    else:
        return ''

def muestraVentana():
    webview.windows[0].show()
    imprime()

def VerificoHabilitaciones():
    global nfc
    global mercadoPago
    global insertCash
    global swipeCard
    global card
    global scanApp
    global newCard
    global simbolo
    global bill1
    global bill2
    global coin

    data=SetupM.GetJsonSetup()
    bill1=miboleano2(data["Peripherals"][0]["bill1Enabled"])
    bill2=miboleano2(data["Peripherals"][0]["bill2Enabled"])
    coin=miboleano2(data["Peripherals"][0]["coinEnabled"])
    swipeCard=miboleano2(data["Peripherals"][0]["magnetic_reader_Enabled"])
    nfc=miboleano2(data["Peripherals"][0]["nfc_reader_Enabled"])
    scanApp=miboleano2(data["Peripherals"][0]["barcode_reader_Enabled"])
    newCard=miboleano2(data["Peripherals"][0]["magnetic_card_dispenser_Enabled"])
    mercadoPago='True'
    card='True'
    if bill1=='strue' or bill2=='true' or  coin=='true':
        insertCash='true'
    #data["Peripherals"][0]["nfc_card_dispenser_Enabled"]=miboleano(f.args['nfc_dispenser'])
    #data["Peripherals"][0]["printer_Enabled"]=miboleano(f.args['printer'])

def EventosPlaca():
    global ruta
    ruta='index.html?nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$'#'C:\\Users\\LP\\Documents\\Interface_2020\\CajeroNuevo\\setup.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
    CambioVentana()
    functions.LeerFiat=True
    functions.LeerIngresoFiat()
    functions.LeerFiat=False
    



def imprime():
    global entro
    global entroProbador
    global ruta
    VerificoHabilitaciones()
    while 1:
        try:
            
            if BoardModule.PuertaAbierta: #cierra app si abren puerta
                CloseApp()
                break

            EventosPlaca()#eventos placa
                      

            page=webview.windows[0].get_current_url()
            #print(page[-10:])
            
            """ if  page[-9:]=='exit.html' and entro==False or BoardModule.PuertaAbierta==False:#webview.windows[0].get_current_url()=='file:///C:/Users/LP/Documents/Interface_2020/CajeroNuevo/exit':
                entro=True
                webview.windows[0].hide()
                #SetupM.GetJsonSetup() #recupero el anterior
                #SetupM.SaveSetup() #guardo el viejo
                CloseSetup()
                #webview.windows[0].load_url('setup.html')
                #webview.windows[0].destroy()
                return

            if  page[-9:]=='save.html' and entro==False:#webview.windows[0].get_current_url()=='file:///C:/Users/LP/Documents/Interface_2020/CajeroNuevo/exit':
                entro=True
                webview.windows[0].hide()
                SetupM.SaveSetup() #guardo el nuevo
                CloseSetup() #cierro
                webview.windows[0].destroy() 
                #webview.windows[0].load_url('setup.html') 
                #cambia setup.json
                return """

            # if (page.find('r=0') != -1) and entro==False:
            #     entro=True
                

            sleep(0.0001)
                
                
            
        except Exception as e:
            entro=False
            print('error '+ str(e))
            sleep(0.0001)
            continue
if __name__ == '__main__':
    #client_thread  = threading.Thread(target=imprime)#,kwargs={'btcNoTocar': notocar}
    #client_thread.start()
    a=1
#threading.Thread(target=CambioVentana.start()
#creoVentana()