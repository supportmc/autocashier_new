from furl import furl #para la url en python
import webview
from time import sleep
import threading
import CounterM
import Channel_File
#import App
#import view
import CustomerM
import sys
#----------------------------------------------------------------------------------
#importo puntero
sys.path.append('/home/pi/Autocashier/')
import pointer
data=pointer.CheckPointer()
sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/App/') #importa aplicacion y vista actual
sys.path.append('/home/pi/Autocashier/'+str(data['APPCA'])+'/View/')
import sapp
import sview
import SetupM
#import start
import BoardModule
#-----------------------------------------------------------------------------------

import datetime
import json
import os
softversion='022.006.001.001'
entro=False
x=1
entroProbador=False

def creoVentana(sversion):
    global softversion
    global entro
    # //traigo conteos de todo \\
    softversion=sversion
    """ data=CounterModule.Read_CounterStart()
    t=str(data["Total_Start"]).zfill(12)
    p=str(data["Parcial_Start"]).zfill(12)
    spacs=str(data["SPAC_Start"]).zfill(12)
    appacs=str(data["APPAC_Start"]).zfill(12)
    vacs=str(data["VAC_Start"]).zfill(12)
    r=data["LastReset"]
    spacv=sversion
    appacv=sapp.GetVersion()
    vacv=sview.GetVersion()
    #//customer
    data=CustomerModule.Read_Customer()
    customer=data """

    Channel_File.GetJsonChannel()

    #os.chdir(start.rutaPrincipal)

    mdir=os.getcwd()
    print(mdir)
    #Paso todo los parametros a la vista
    ruta='setup.html'#'C:\\Users\\LP\\Documents\\Interface_2020\\CajeroNuevo\\setup.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
    print(ruta)
    #ruta=mdir+'/'+ruta
    entro=False
    window = webview.create_window('Get current URL1', ruta,fullscreen=True)
    webview.start(change_url, window,http_server=True)
    

def change_url(window):
    #global x
    #a=1
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
def CloseSetup():
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

def muestraVentana():
    webview.windows[0].show()
    imprime()

def imprime():
    global entro
    global entroProbador
    while 1:
        try:
            page=webview.windows[0].get_current_url()
            #print(page[-10:])
            
            if  page[-9:]=='exit.html' and entro==False or BoardModule.PuertaAbierta==False:#webview.windows[0].get_current_url()=='file:///C:/Users/LP/Documents/Interface_2020/CajeroNuevo/exit':
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
                return

            if (page.find('r=0') != -1) and entro==False:
                entro=True
                if CounterM.Reset_CounterStart() ==True:
                    print('reset ok')
                else:
                    print('reset error')
                data=SetupM.GetJsonSetup()#CounterModule.Read_CounterStart()
                t=str(data["Total_Start"]).zfill(12)
                p=str(data["Parcial_Start"]).zfill(12)
                r=datetime.datetime.strptime(data["LastReset"], "%d/%m/%y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                ruta='scounter.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)
                webview.windows[0].load_url(ruta)

            
                
            if (page.find('channel_test') != -1):#and entro==False:
                entroProbador=True
                data=SetupM.JsonSetup
                bill1Enabled= data["Peripherals"][0]["bill1Enabled"]
                bill2Enabled= data["Peripherals"][0]["bill2Enabled"]
                coinEnabled= data["Peripherals"][0]["coinEnabled"]
                if entro==False:
                    x=0
                    while BoardModule.habPlata(bill1Enabled,bill2Enabled,coinEnabled)and x<2:
                        sleep(0.01)
                        x+=1
                entro=True
                
                if BoardModule.device_board !=0:
                    
                    c='Ch'+ str(BoardModule.channel_board)
                    #print('Entro '+ str(float(canales['Bill1'][0][c][0]['value'])/100) + ' ' +str(canales['Bill1'][0]['Ch1'][0]['type']))
                    
                    if bill1Enabled==True or bill2Enabled==True or coinEnabled==True:
                        if BoardModule.device_board==1:
                            ruta='channel_test.html' +'?hardware=Bill '+str(BoardModule.device_board)+'&amount='+str(float(Channel_File.JsonChannelFile['Bill1'][0][c][0]['value'])/100)+'&currency='+str(Channel_File.JsonChannelFile['Bill1'][0]['Ch1'][0]['type'])+'&symbol=$&rate=1&moneda=Pesos&simbolo=$'
                        elif BoardModule.device_board==2:
                            ruta='channel_test.html' +'?hardware=Bill '+str(BoardModule.device_board)+'&amount='+str(float(Channel_File.JsonChannelFile['Bill1'][0][c][0]['value'])/100)+'&currency='+str(Channel_File.JsonChannelFile['Bill1'][0]['Ch1'][0]['type'])+'&symbol=$&rate=1&moneda=Pesos&simbolo=$'
                        elif BoardModule.device_board==3:
                            ruta='channel_test.html' +'?hardware=Coin&amount='+str(float(Channel_File.JsonChannelFile['Coin'][0][c][0]['value'])/100)+'&currency='+str(Channel_File.JsonChannelFile['Coin'][0]['Ch1'][0]['type'])+'&symbol=$&rate=1&moneda=Pesos&simbolo=$'

                        webview.windows[0].load_url(ruta)
                    
                    #agregar para controlar desde config o app
                    BoardModule.device_board=0
                    BoardModule.channel_board=0
                
                

                    
                    

            if  page[-10:]=='setup.html':#(page.find('setup.html') != -1):
                entro=True               

                data=CounterM.Read_CounterStart()
                t=str(data["Total_Start"]).zfill(12)
                p=str(data["Parcial_Start"]).zfill(12)
                spacs=str(data["SPAC_Start"]).zfill(12)
                appacs=str(data["APPAC_Start"]).zfill(12)
                vacs=str(data["VAC_Start"]).zfill(12)
                r=datetime.datetime.strptime(data["LastReset"], "%d/%m/%y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                spacv=softversion
                appacv=sapp.GetVersion()
                vacv=sview.GetVersion()
                
                #data=[CustomerModule.Read_Customer()]
                
                customer=data["Customer"]
                ssid=data["SSID"]
                Pass=data["Password"]
                channelFile= data["Channel_file_Update"]
                exchangeFile= data["Exchange_file_Update"]
                purl=data["Payment_url"]
                pport=data["Payment_port"]
                nurl=data["Node_url"]
                nport=data["Node_port"]
                surl=data["System_url"]
                sport=data["System_port"]
                dname=data["device_name"]
                did=data["device_id"]

                bill1Enabled= data["Peripherals"][0]["bill1Enabled"]
                bill2Enabled= data["Peripherals"][0]["bill2Enabled"]
                coinEnabled= data["Peripherals"][0]["coinEnabled"]
                magnetic_reader_Enabled= data["Peripherals"][0]["magnetic_reader_Enabled"]
                nfc_reader_Enabled= data["Peripherals"][0]["nfc_reader_Enabled"]
                barcode_reader_Enabled= data["Peripherals"][0]["barcode_reader_Enabled"]
                magnetic_card_dispenser_Enabled= data["Peripherals"][0]["magnetic_card_dispenser_Enabled"]
                nfc_card_dispenser_Enabled= data["Peripherals"][0]["nfc_card_dispenser_Enabled"]
                printer_Enabled= data["Peripherals"][0]["printer_Enabled"]

                #+'&bill1='+str(bill1Enabled)+'&bill2='+str(bill2Enabled)+'&coin='+str(coinEnabled)+'&magnetic_reader='+str(magnetic_reader_Enabled)+'&nfc_reader='+str(nfc_reader_Enabled)+'&barcode_reader='+str(barcode_reader_Enabled)+'&magnetic_dispenser='+str(magnetic_card_dispenser_Enabled)+'&nfc_dispenser_='+str(nfc_card_dispenser_Enabled)+'&printer='+str(printer_Enabled)
                
                if nfc_card_dispenser_Enabled == True:
                    nfc_card_dispenser_Enabled=1
                    magnetic_card_dispenser_Enabled=""
                elif magnetic_card_dispenser_Enabled ==True:
                    magnetic_card_dispenser_Enabled=1 
                    nfc_card_dispenser_Enabled=""

                if bill1Enabled== False:
                    bill1Enabled=""
                if bill2Enabled== False:
                    bill2Enabled=""
                if coinEnabled==False:
                    coinEnabled=""
                if magnetic_card_dispenser_Enabled==False:
                    magnetic_card_dispenser_Enabled=""
                if magnetic_reader_Enabled==False:
                    magnetic_reader_Enabled=""
                if nfc_reader_Enabled==False:
                    nfc_reader_Enabled=""
                if nfc_card_dispenser_Enabled==False:
                    nfc_card_dispenser_Enabled=""
                if printer_Enabled==False:
                    printer_Enabled=""
                if channelFile==False:
                    channelFile=""
                if exchangeFile==False:
                    exchangeFile=""
                if barcode_reader_Enabled==False:
                    barcode_reader_Enabled=""
                



                #Paso todo los parametros a la vista
                #file:///home/pi/Autocashier/
                #ruta= 'file://'+os.getcwd()+'/' +'setup.html'+'?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
                ruta='setup.html' +'?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)+'&bill1='+str(bill1Enabled)+'&bill2='+str(bill2Enabled)+'&coin='+str(coinEnabled)+'&magnetic_reader='+str(magnetic_reader_Enabled)+'&nfc_reader='+str(nfc_reader_Enabled)+'&barcode_reader='+str(barcode_reader_Enabled)+'&nfc_dispenser='+str(nfc_card_dispenser_Enabled)+'&magnetic_dispenser='+str(magnetic_card_dispenser_Enabled)+'&printer='+str(printer_Enabled)+'&channel_file='+str(channelFile)+'&exchange_file='+str(exchangeFile)+'&ssid='+str(ssid)+'&pass='+str(Pass)+'&purl='+str(purl)+'&pport='+str(pport)+'&nurl='+str(nurl)+'&nport='+str(nport)+'&surl='+str(surl)+'&sport='+str(sport)+'&dname='+str(dname)+'&did='+str(did)
                print('lo q hice ' + ruta)
                webview.windows[0].load_url(ruta)
                #BoardModule.desPlata(True,True,True)
                x=0
                if entroProbador==True:
                    while BoardModule.desPlata(bill1Enabled,bill2Enabled,coinEnabled)and x<2:
                            sleep(0.01)
                            x+=1
                entro=False
                entroProbador=False
        
            if (page.find('setup.html?bill')!=-1) and entro==False:
                entro=True
                f = furl(page) 
                try:
                    if f.args['bill1']!=None:
                        print('guarda datos de perifericos')

                        data["Channel_file_Update"]=miboleano(f.args['channel_file'])
                        data["Exchange_file_Update"]=miboleano(f.args['exchange_file'])
                        data["Peripherals"][0]["bill1Enabled"]=miboleano(f.args['bill1'])
                        data["Peripherals"][0]["bill2Enabled"]=miboleano(f.args['bill2'])
                        data["Peripherals"][0]["coinEnabled"]=miboleano(f.args['coin'])
                        data["Peripherals"][0]["magnetic_reader_Enabled"]=miboleano(f.args['magnetic_reader'])
                        data["Peripherals"][0]["nfc_reader_Enabled"]=miboleano(f.args['nfc_reader'])
                        data["Peripherals"][0]["barcode_reader_Enabled"]=miboleano(f.args['barcode_reader'])
                        data["Peripherals"][0]["magnetic_card_dispenser_Enabled"]=miboleano(f.args['magnetic_dispenser'])
                        data["Peripherals"][0]["nfc_card_dispenser_Enabled"]=miboleano(f.args['nfc_dispenser'])
                        data["Peripherals"][0]["printer_Enabled"]=miboleano(f.args['printer'])
                        SetupM.SetJsonSetup(data)
                        webview.windows[0].load_url('setup.html')
                except:
                    entro=False
                    continue
            if (page.find('setup.html?ssid')!=-1) and entro==False:
                    entro=True
                    f = furl(page) 
                    try:
                        if f.args['ssid']!=None:
                            print('guarda datos de wifi')

                            data=SetupM.GetJsonSetup()

                            data["SSID"]=f.args['ssid']
                            data["Password"]=f.args['pass']
                            
                            if data["Payment_url"] != '' or data["Payment_url"] !=None:
                                #NUC activado
                                ar=open("/home/pi/Autocashier/RedActual.txt","w")
                                ar.write(str(f.args['ssid'])+"\r\n"+ str(f.args['pass']))
                                ar.close()



                            SetupM.SetJsonSetup(data)
                            webview.windows[0].load_url('setup.html')

                            
                    except Exception as e:
                        print(str(e))
                        continue
                        sigue=True   

            if (page.find('setup.html?purl')!=-1) and entro==False:
                    entro=True
                    f = furl(page) 
                    try:
                        if f.args['purl']!=None:
                            print('guarda datos de payment')

                            data=SetupM.GetJsonSetup()

                            data["Payment_url"]=f.args['purl']
                            data["Payment_port"]=f.args['pport']
                            data["Node_url"]=f.args['nurl']
                            data["Node_port"]=f.args['nport']
                            data["System_url"]=f.args['surl']
                            data["System_port"]=f.args['sport']
                            
                            SetupM.SetJsonSetup(data)
                            webview.windows[0].load_url('setup.html')
            
            

                            
                    except:
                        sigue=True
                        continue

            if (page.find('setup.html?dname')!=-1)and entro==False:
                    entro=True
                    f = furl(page) 
                    try:
                        if f.args['dname']!=None:
                            print('guarda datos de autocashier')

                            data=SetupM.GetJsonSetup()

                            data["device_name"]=f.args['dname']
                            data["device_id"]=f.args['did']
                            
                            
                            SetupM.SetJsonSetup(data)
                            webview.windows[0].load_url('setup.html') 
                    except:
                        sigue=True
                        continue          

            sleep(0.0001)
                
                
            
        except Exception as e:
            entro=False
            print('error '+ str(e))
            sleep(0.0001)
            continue

if __name__ == '__main__':
    #client_thread  = threading.Thread(target=imprime)#,kwargs={'btcNoTocar': notocar}
    #client_thread.start()
    creoVentana('')
    
    
    