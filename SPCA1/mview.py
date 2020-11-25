from furl import furl #para la url en python
import webview
from time import sleep
import threading
import CounterModule
#import App
#import view
import CustomerModule
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
import SetupModule

import BoardModule
#-----------------------------------------------------------------------------------

import datetime
import json
import os
softversion='0'
x=1

def creoVentana(sversion):
    global softversion
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


    #Paso todo los parametros a la vista
    ruta='setup.html'#'C:\\Users\\LP\\Documents\\Interface_2020\\CajeroNuevo\\setup.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
    print(ruta)
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
        
        filename='setup.json'            
        
        data = Read_Setup()
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

def miboleano(q):
    if q=='false':
        return False
    else:
        return True

def muestraVentana():
    webview.windows[0].show()
    imprime()

def imprime():
    while 1:
        try:
            page=webview.windows[0].get_current_url()
            #print(page[-10:])
            if  page[-9:]=='exit.html':#webview.windows[0].get_current_url()=='file:///C:/Users/LP/Documents/Interface_2020/CajeroNuevo/exit':
                webview.windows[0].hide()
                SetupModule.GetJsonSetup() #recupero el anterior
                #SetupModule.SaveSetup() #guardo el viejo
                CloseSetup()
                #webview.windows[0].load_url('setup.html')
                webview.windows[0].destroy()
                return

            if  page[-9:]=='save.html':#webview.windows[0].get_current_url()=='file:///C:/Users/LP/Documents/Interface_2020/CajeroNuevo/exit':
                webview.windows[0].hide()
                SetupModule.SaveSetup() #guardo el nuevo
                CloseSetup() #cierro
                webview.windows[0].destroy() 
                #webview.windows[0].load_url('setup.html') 
                #cambia setup.json
                return

            if (page.find('r=0') != -1):
                if CounterModule.Reset_CounterStart() ==True:
                    print('reset ok')
                else:
                    print('reset error')
                data=SetupModule.GetJsonSetup()#CounterModule.Read_CounterStart()
                t=str(data["Total_Start"]).zfill(12)
                p=str(data["Parcial_Start"]).zfill(12)
                r=datetime.datetime.strptime(data["LastReset"], "%d/%m/%y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
                ruta='scounter.html?t='+str(t)+'&p='+str(p)+'&r='+str(r)
                webview.windows[0].load_url(ruta)
            if  page[-10:]=='setup.html':#(page.find('setup.html') != -1):

                
                data=CounterModule.Read_CounterStart()
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
                channelFile= data["Channel_file_Update"]
                exchangeFile= data["Exchange_file_Update"]

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
                ruta='setup.html' +'?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)+'&bill1='+str(bill1Enabled)+'&bill2='+str(bill2Enabled)+'&coin='+str(coinEnabled)+'&magnetic_reader='+str(magnetic_reader_Enabled)+'&nfc_reader='+str(nfc_reader_Enabled)+'&barcode_reader='+str(barcode_reader_Enabled)+'&nfc_dispenser='+str(nfc_card_dispenser_Enabled)+'&magnetic_dispenser='+str(magnetic_card_dispenser_Enabled)+'&printer='+str(printer_Enabled)+'&channel_file='+str(channelFile)+'&exchange_file='+str(exchangeFile)
                print('lo q hice ' + ruta)
                webview.windows[0].load_url(ruta)
        
            if (page.find('setup.html?bill')!=-1):
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
                        SetupModule.SetJsonSetup(data)
                        webview.windows[0].load_url('setup.html')

                        
                except:
                    sigue=True
            

            sleep(0.001)
                
                
            
        except Exception as e:
            #print('error '+ str(e))
            sleep(0.0001)
            continue

if __name__ == '__main__':
    #client_thread  = threading.Thread(target=imprime)#,kwargs={'btcNoTocar': notocar}
    #client_thread.start()
    creoVentana('')
    
    
    