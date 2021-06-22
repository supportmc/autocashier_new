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
import database
import posnet

rutaVista='/home/pi/Autocashier/'+str(data['APPCA'])+'/View/'

sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/View/')

sys.path.append("/home/pi/Autocashier/"+data['SPCA'])
import BoardModule
import SetupM

import DispenserM
import QRReaderM
import PrintM


#import sapp
#import sview
#import SetupM
#import start
Tarjeta=''
ruta=''
nfc=''
mercadoPago=''
insertCash=''
swipeCard=''
card=''
scanApp=''
newCard=''
newCardNfc=''
newCardMagnetic=''
simbolo=''
bill1=''
bill2=''
coin=''
newCardPrice=0
simboloTNueva=''

bill1Enabled=False
bill2Enabled=False
coinEnabled=False

LectorTeclado=False
LectorscanApp=False

PosnetActivo=False
PostnetCon=[]
#-----------------------------------------------------------------------------------

import datetime
import json
import os
entro=False
x=1
entroProbador=False


from pynput import keyboard
from datetime import timedelta
from datetime import datetime
import threading
from time import sleep
entrada=''
t=datetime.now()
def on_press(key):
    try:
        print(key.char)
    except:
        a=1



def TiempoEntrada():
    global t
    global entrada
    global Tarjeta
    while 1:
        if t < datetime.now() and entrada !='':
            Tarjeta=entrada[:-1]
            functions.LeerFiat=False
            print('llego '+str(Tarjeta))
            entrada=''
        if QRReaderM.TarjetaQr:
            functions.LeerFiat=False
            print('llego '+str(Tarjeta))
            entrada=''
        sleep(0.1)
    
    


def on_release(key):
    global entrada
    global t
    try:
        if entrada=='':
            t=datetime.now() + timedelta(seconds=1)
        if t> datetime.now():
            entrada+=key.char
        
            

    except Exception as e:
        #print(e)
        a=1

def EscuchoTeclas():
    while 1:
        try:
            with keyboard.Listener(
            #on_press=on_press,
            on_release=on_release)as listener:
                listener.join()
        except:
            continue

th=threading.Thread(target=TiempoEntrada).start()
tl=threading.Thread(target=EscuchoTeclas).start()


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

def VerificaPosnet():
    global PostnetCon
    global PosnetActivo
    if PostnetCon:
        for d in PostnetCon:
            r=posnet.Posnet_Init(d[0],int(d[1]))
            if r!='Error':
                r=json.loads(r)

                if r['Resultado']['Cod']==0:
                    r=posnet.Posnet_Status()
                    r=json.loads(r)
                    if r['Resultado']['Cod']==15:
                        threading.Thread(target=posnet.Posnet_Config).start()
                        PosnetActivo=True
                    elif r['Resultado']['Cod']!=0:
                        print('Error en Posnet')
                    elif r['Resultado']['Cod']==0:
                        print('Postnet Operativo')
                        PosnetActivo=True
                else:
                    print('Error al inicializar posnet')
                    if r['Resultado']['Cod']==15:
                        threading.Thread(target=posnet.Posnet_Config).start()
            else:
                PosnetActivo=False

def creoVentana():
    global softversion
    global entro
    global bill1Enabled
    global bill2Enabled
    global coinEnabled
    global PosnetActivo


    # //traigo conteos de todo \\
    #softversion=sversion
    

    #Channel_File.GetJsonChannel()

    #os.chdir(start.rutaPrincipal)

    mdir=os.getcwd()
    print(mdir)
    #webview.windows[0].load_url('setup.html') 
    #Paso todo los parametros a la vista
    threading.Thread(target=DispenserM.sacarTarjeta, args=('M',)).start()
    threading.Thread(target=PrintM.Print).start()
    
    VerificoHabilitaciones()
    VerificaPosnet()
    

    functions.LeerFiat=True
    
    data=SetupM.GetJsonSetup()
    bill1Enabled= data["Peripherals"][0]["bill1Enabled"]
    bill2Enabled= data["Peripherals"][0]["bill2Enabled"]
    coinEnabled= data["Peripherals"][0]["coinEnabled"]
    x=0
    if functions.SALDO==0:
        while BoardModule.habPlata(bill1Enabled,bill2Enabled,coinEnabled)and x<2:
            sleep(0.001)
            x+=1

    #ruta=rutaVista+'index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$'
    if PosnetActivo:        
        ruta=rutaVista+'index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$'
    else:
        ruta=rutaVista+'index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$'
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
    global newCardNfc
    global newCardMagnetic
    global simbolo
    global bill1
    global bill2
    global coin
    global newCardPrice
    global simboloTNueva
    global PostnetCon
    global PosnetActivo

    data=SetupM.GetJsonSetup()
    bill1=miboleano2(data["Peripherals"][0]["bill1Enabled"])
    bill2=miboleano2(data["Peripherals"][0]["bill2Enabled"])
    coin=miboleano2(data["Peripherals"][0]["coinEnabled"])
    swipeCard=miboleano2(data["Peripherals"][0]["magnetic_reader_Enabled"])
    nfc=miboleano2(data["Peripherals"][0]["nfc_reader_Enabled"])
    scanApp=miboleano2(data["Peripherals"][0]["barcode_reader_Enabled"])
    newCardMagnetic=miboleano2(data["Peripherals"][0]["magnetic_card_dispenser_Enabled"])
    newCardNfc=miboleano2(data["Peripherals"][0]["nfc_card_dispenser_Enabled"])
    mercadoPago=''
    card='True'
    newCardPrice=float(data["PriceNewCard"])
    simboloTNueva=data["PriceNewCardSymbol"]
    if bill1=='strue' or bill2=='true' or  coin=='true':
        insertCash='true'

    if data['Payment_url'] and data['Payment_port']:
        PostnetCon.append([data['Payment_url'],data['Payment_port'] ])
        #PosnetActivo=True

    #data["Peripherals"][0]["nfc_card_dispenser_Enabled"]=miboleano(f.args['nfc_dispenser'])
    #data["Peripherals"][0]["printer_Enabled"]=miboleano(f.args['printer'])

def FinalizaTransaccion():
    global Tarjeta
    global LectorTeclado
    global simbolo

    if Tarjeta and Tarjeta.find(';')>-1:

        if swipeCard and nfc:
            vr='nfc/swipe'
        elif swipeCard:
            vr='swipe'
        elif nfc:
            vr='nfc'
        vmpl='mpl'
        tcard=Tarjeta
    elif scanApp and QRReaderM.TarjetaQr:
        vr='QR'
        vmpl='vmpl'
        
        tcard=QRReaderM.TarjetaQr
        QRReaderM.TarjetaQr=''
    elif Tarjeta:
        vr='Dispenser'
        vmpl='mpl'
        
        tcard=';'+Tarjeta

        

        


    #PrintM.Print(0,functions.SALDO,"Autocashier",tcard,simbolo,21)
    PrintM.parametros.append(0) #ptarjeta
    PrintM.parametros.append(functions.SALDO)#saldo
    PrintM.parametros.append("Autocashier")#nomb cajero
    PrintM.parametros.append(tcard)#mpl
    PrintM.parametros.append(simbolo)#simbolo
    PrintM.parametros.append(21)#tax


    #Close_Transaction
    event='{"tipo":"Close","timestamp":"'+str(datetime.now())+'"}'
    eventClose='{"Reader":"'+ str(vr) +'","MPL":"'+ str(vmpl)+'","MPL_Number":"'+str(tcard)+'","System":"Autocashier","Total_amount_local_currency":"'+str(functions.SALDO)+'"}'
    database.saveHistoryEvent(event,eventClose,'close')
    
    functions.SALDO=0
    Tarjeta=''
    LectorTeclado=False

    



    #VerificaPosnet()
    
    

def Eventos():
    global ruta
    global Tarjeta
    #muestra boton tarjeta nueva si esta hab y alcanza
    if functions.SALDO>=newCardPrice and newCardNfc=='true' or functions.SALDO>newCardPrice and newCardMagnetic=='true' and DispenserM.TPreparada:
        newCard='True'
        newCardValue=simboloTNueva+' '+ str(newCardPrice)
    else:
        newCard=''
        newCardValue=''
    
    

    if Tarjeta and functions.SALDO==0 or QRReaderM.TarjetaQr and functions.SALDO==0:
        t=''
        if Tarjeta:
            data=database.GetHistory(Tarjeta)
            t=Tarjeta
        elif QRReaderM.TarjetaQr:
            data=database.GetHistory(QRReaderM.TarjetaQr)
            t=QRReaderM.TarjetaQr
        if data:
            #tableHistory='<table><tr><th>Date</th><th>System</th><th>Amount</th></tr>'
            tt=[]
            tableHistory=[]
            for registro in data:
                #tableHistory+='<tr><td>'+ str(registro[6])+'</td><td>Autocashier</td><td>'+ str(registro[5])+'</td></tr>'
                tableHistory.append('"'+ registro[6][:-7]+'"')
                tableHistory.append('"'+ registro[4]+'"')
                tableHistory.append('"'+ registro[5]+'"')
                
                tt.append(tableHistory)            
                tableHistory=[]
            #tableHistory+='</table>'
            tt=json.dumps(tt)
            tt=tt.replace('\\"','')
            ruta='index.html?&chargeInfo=true&cardNumber='+str(t)+'&chargeInfoTable='+str(tt)#&cardNumber='+str(Tarjeta)+'&chargeInfo=true&
            CambioVentana()
        Tarjeta=''
        QRReaderM.TarjetaQr=''
    
    if Tarjeta and functions.SALDO>0 or QRReaderM.TarjetaQr and functions.SALDO>0:
        

        FinalizaTransaccion()
        
        ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
        CambioVentana()
        BoardModule.ApagarLucesLectora()
        
        #sleep(4)
        #ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&saldo='+ str(functions.SALDO) +'&simbolo=$'
        #CambioVentana()
        functions.LeerFiat=True

        if functions.SALDO==0:
            while BoardModule.habPlata(bill1Enabled,bill2Enabled,coinEnabled)and x<2:
                sleep(0.001)
                x+=1

        
    elif functions.Ingreso:
        if PosnetActivo:        
            ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ newCardValue
        else:
            ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ newCardValue
        CambioVentana()
        functions.Ingreso=False
    
    if functions.ReaderActivos:
        BoardModule.EncenderLucesLectora()
        functions.ReaderActivos=False

    functions.LeerFiat=True
    vif=functions.LeerIngresoFiat(bill1Enabled,bill2Enabled,coinEnabled)
    if vif:
        #device example
        event='{"tipo":"Device","timestamp":"'+str(datetime.now())+'"}'
        eventDevice='{"Device":"'+vif['Device']+'","Channel":"'+vif['Channel']+'","Currency":"'+ vif['Currency'] +'","Total_amount_local_currency":"'+vif['Total_amount_local_currency']+'"}'
        database.saveHistoryEvent(event,eventDevice,'device')

    functions.LeerFiat=False
    



def imprime():
    global entro
    global entroProbador
    global ruta
    global newCardPrice
    global Tarjeta
    if newCardPrice < 0:
        newCardPrice=0
    while 1:
        try:
            
            if BoardModule.PuertaAbierta: #cierra app si abren puerta
                CloseApp()
                break

            #Eventos placa
            Eventos()#eventos placa
            #Evento Readers
            


            
                      

            page=webview.windows[0].get_current_url()
            #print(page[-10:])
            page=str(page)
            #

            if page.find('btnBackFromMovimientos=true')>-1:
                #ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)
                if PosnetActivo:        
                    ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)
                else:
                    ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)
                CambioVentana()
                

            if page.find('newCardBtnActivado=true')>-1:
                #ruta='index.html?&btnCardActivado=true'
                #CambioVentana()
                #functions.Ingreso=False
                #r=DispenserM.sacarTarjeta('M')
                
                #r=DispenserM.EstadoTarjetero()
                Tarjeta=DispenserM.LeerTarjeta('M')
                if Tarjeta:#r['Lector Ocupado']==1:
                    
                    #Tarjeta=r['card_number']
                    FinalizaTransaccion()
                    #ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice=$'+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
                    if PosnetActivo:        
                        ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
                    else:
                        ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
                    CambioVentana()
                    
                                        
                    #if Tarjeta:
                    BoardModule.EncenderLuzTarjetero()
                    DispenserM.ExpulsarTarjeta()
                    #DispenserM.TPreparada=False
                    sleep(2.5)
                    BoardModule.ApagarLucesLectora()
                    BoardModule.ApagarLuzTarjetero()
                elif not Tarjeta:
                    DispenserM.TPreparada=False
                    #sleep(0.2)
                    Tarjeta=DispenserM.LeerTarjeta('M')
                    if Tarjeta:
                        FinalizaTransaccion()
                        #ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice=$'+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
                        if PosnetActivo:        
                            ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
                        else:
                            ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice='+ str(newCardPrice)+'&finTransaccion=true&msj=Transaction OK!'
                        CambioVentana()
                        DispenserM.ExpulsarTarjeta()
                        sleep(2)
                        BoardModule.ApagarLucesLectora()
                        BoardModule.ApagarLuzTarjetero()
                        
                    else:
                        DispenserM.sacarTarjeta('M')
                        DispenserM.TPreparada=False

                
                    
                    
                    
                    

                else:                
                    ruta='index.html?&nfc='+ nfc +'&mercadoPago='+mercadoPago+'&insertCash='+insertCash+'&swipeCard='+swipeCard+'&card='+card+'&scanApp='+scanApp+'&newCard='+newCard+'&saldo='+ str(functions.SALDO) +'&simbolo=$&newCardPrice=$'+ newCardPrice
                    CambioVentana()
                    functions.Ingreso=False
                

                

            if page.find('confirmedValue')>-1:
                t=page.find('=')
                ruta=rutaVista+'index.html?&saldo3='+ str(functions.SALDO) +'&simbolo3=$&screen3=1&valueSimboloSelected=$&valueMontoSelected='+str(page[t+1:])                
                webview.windows[0].load_url(ruta)


            if page.find('valuePersonalizado=true')>-1:
                t=page.find('=')
                

                if t>-1:
                    ruta=rutaVista+'index.html?&saldo3='+ str(functions.SALDO) +'&simbolo3=$&screen3Personalizado=1&valueSimboloSelected=$'                
                    webview.windows[0].load_url(ruta)

            if page.find('valueSelected=')>-1 or page.find('valueMontoSelected=')>-1:
                p=0
                p=page.find('valueMontoSelected=')
                if p> -1:
                    t=page[p:].find('=')
                    t=t+p
                else:
                    t=page.find('=')

                if t>-1:
                    ruta=rutaVista+'index.html?&saldo3='+ str(functions.SALDO) +'&simbolo3=$&screen3=1&valueSimboloSelected=$&valueMontoSelected='+str(page[t+1:])                
                    webview.windows[0].load_url(ruta)
                    for d in PostnetCon:
                        r=posnet.Posnet_Status()
                        r=json.loads(r)
                        if r['Resultado']['Cod']==15:
                            threading.Thread(target=posnet.Posnet_Config).start()
                        elif r['Resultado']['Cod']==0:
                            r=posnet.Posnet_Pay(float(page[t+1:]),1)
                            r=json.loads(r)
                            if r['Resultado']['Cod']==0:
                                functions.Incrementar(float(page[t+1:]))
                                print('Total ingresado '+ str(page[t+1:]))                                                               
                                ruta=rutaVista+'index.html?&saldo3='+ str(functions.SALDO) +'&simbolo3=$&screen3=1&valueSimboloSelected=$&valueMontoSelected='+str(page[t+1:])+'&successProcessPersonalizado=true'                
                                webview.windows[0].load_url(ruta)
                                sleep(2)
                                functions.Ingreso=True
                            else:
                                ruta=rutaVista+'index.html?&saldo3='+ str(functions.SALDO) +'&simbolo3=$&screen3=1&valueSimboloSelected=$&valueMontoSelected='+str(page[t+1:])+'&errorProcessPersonalizado=true'                
                                webview.windows[0].load_url(ruta)
                                sleep(2)
                                functions.Ingreso=True


                            
                        elif r['Resultado']['Cod']!=0:
                            print('Error en Posnet')
                            ruta=rutaVista+'index.html?&saldo3='+ str(functions.SALDO) +'&simbolo3=$&screen3=1&valueSimboloSelected=$&valueMontoSelected='+str(page[t+1:])+'&errorProcessPersonalizado=true'                
                            webview.windows[0].load_url(ruta)
                            sleep(2)
                            functions.Ingreso=True
                    #print(todo[t+1:])

            if page.find('btnCardActivado=true')>-1:
                ruta=rutaVista+'index.html?&saldo2='+ str(functions.SALDO) +'&simbolo2=$&valueMonto1=10&valueMonto2=50&valueMonto3=100&valueMonto4=1000&montoPersonalizado=1&screen2=1'                
                webview.windows[0].load_url(ruta)
                
            
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
                

            sleep(0.000001)
                
                
            
        except Exception as e:
            entro=False
            print('error '+ str(e))
            sleep(0.000001)
            continue
if __name__ == '__main__':
    #client_thread  = threading.Thread(target=imprime)#,kwargs={'btcNoTocar': notocar}
    #client_thread.start()
    a=1
#threading.Thread(target=CambioVentana.start()
#creoVentana()



