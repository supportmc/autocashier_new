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
    window = webview.create_window('Get current URL1', ruta)
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
    
def imprime():
    while 1:
        try:
            page=webview.windows[0].get_current_url()
            #print(page[-10:])
            if  page[-9:]=='exit.html':#webview.windows[0].get_current_url()=='file:///C:/Users/LP/Documents/Interface_2020/CajeroNuevo/exit':
                webview.windows[0].hide()
                CloseSetup()
                webview.windows[0].destroy()
                
                #cambia setup.json

            if (page.find('r=0') != -1):
                if CounterModule.Reset_CounterStart() ==True:
                    print('reset ok')
                else:
                    print('reset error')
                data=CounterModule.Read_CounterStart()
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
                #//customer
                data=CustomerModule.Read_Customer()
                customer=data


                #Paso todo los parametros a la vista
                #file:///home/pi/Autocashier/
                #ruta= 'file://'+os.getcwd()+'/' +'setup.html'+'?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)
                ruta='setup.html' +'?t='+str(t)+'&p='+str(p)+'&r='+str(r)+'&spacs='+str(spacs)+'&appacs='+str(appacs)+'&vacs='+str(vacs)+'&spacv='+str(spacv)+'&appacv='+str(appacv)+'&vacv='+str(vacv)+'&c='+str(customer)#'?t=000000000100&p=000000000037&r=28-09-20 2019:48:35&spacs=000000000100&appacs=000000000100&vacs=000000000100&spacv=000.022.001.001&appacv=022.101.001.001&vacv=101.501.001.001&c=Lepark_5400001'
                print('lo q hice ' + ruta)
                webview.windows[0].load_url(ruta)
            

            sleep(0.0001)
                
                
            
        except Exception as e:
            #print('error '+ str(e))
            sleep(0.0001)
            continue

if __name__ == '__main__':
    #client_thread  = threading.Thread(target=imprime)#,kwargs={'btcNoTocar': notocar}
    #client_thread.start()
    creoVentana('')
    
    
    