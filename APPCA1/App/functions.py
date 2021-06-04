import os
import sys
from time import sleep
from datetime import timedelta
from datetime import datetime
#------IMPORTO DE ACUERDO AL MODULO ACTIVO--------------------
sys.path.append('/home/pi/Autocashier/')
import pointer
os.chdir('/home/pi/Autocashier/')
data=pointer.CheckPointer()    
sys.path.append('/home/pi/Autocashier/'+str(data['SPCA'])+'/') #importa aplicacion y vista actual
rutaPrincipal='/home/pi/Autocashier/'+str(data['SPCA'])+'/'
sys.path.append(rutaPrincipal)
#------IMPORTO DE ACUERDO AL MODULO ACTIVO--------------------
import SetupM
import BoardModule
import Channel_File
import Exchange_File
#-----


#VARIABLES:
SALDO=0
LeerFiat=False
Ingreso=False
ReaderActivos=False

def Saldo():
    a=1

def TarjetaNueva():
    a=1

def GuardarTransaccion():
    a=1

def GuardarEvento():
    a=1

def Incrementar(valor):
    global SALDO
    global ReaderActivos
    try:
        if SALDO==0:
            ReaderActivos=True
        if valor>0:
            SALDO+=valor
    except Exception as e:
        print(e)
    
    
    return SALDO

def ResetearSaldo():
    global SALDO
    SALDO=0


def LeerIncompleto():
    a=1

def LeerIngresoFiat(bill1Enabled,bill2Enabled,coinEnabled):
    global LeerFiat
    global Ingreso
    
    x=0
    if Channel_File.JsonChannelFile=='':
        Channel_File.GetJsonChannel()
    if Exchange_File.ExchangeFile=='':
        Exchange_File.GetExchange()

    

    to=datetime.now()+timedelta(seconds=1)
    while LeerFiat and to > datetime.now():
        
        
        
        if BoardModule.PuertaAbierta:
                BoardModule.device_board=0
                BoardModule.channel_board=0
                return {}
        
        if BoardModule.device_board !=0:
            
            c='Ch'+ str(BoardModule.channel_board)
            #print('Entro '+ str(float(canales['Bill1'][0][c][0]['value'])/100) + ' ' +str(canales['Bill1'][0]['Ch1'][0]['type']))
            
            # if bill1Enabled==True or bill2Enabled==True or coinEnabled==True:
            #     if BoardModule.device_board==1:
            #         ruta='channel_test.html' +'?hardware=Bill '+str(BoardModule.device_board)+'&amount='+str(float(Channel_File.JsonChannelFile['Bill1'][0][c][0]['value'])/100)+'&currency='+str(Channel_File.JsonChannelFile['Bill1'][0]['Ch1'][0]['type'])+'&symbol=$&rate=1&moneda=Pesos&simbolo=$'
            #     elif BoardModule.device_board==2:
            #         ruta='channel_test.html' +'?hardware=Bill '+str(BoardModule.device_board)+'&amount='+str(float(Channel_File.JsonChannelFile['Bill1'][0][c][0]['value'])/100)+'&currency='+str(Channel_File.JsonChannelFile['Bill1'][0]['Ch1'][0]['type'])+'&symbol=$&rate=1&moneda=Pesos&simbolo=$'
            #     elif BoardModule.device_board==3:
            #         ruta='channel_test.html' +'?hardware=Coin&amount='+str(float(Channel_File.JsonChannelFile['Coin'][0][c][0]['value'])/100)+'&currency='+str(Channel_File.JsonChannelFile['Coin'][0]['Ch1'][0]['type'])+'&symbol=$&rate=1&moneda=Pesos&simbolo=$'
            valor=0
            valorOriginal=0
            if BoardModule.device_board==1 and bill1Enabled:
                valor=(float(Channel_File.JsonChannelFile['Bill1'][0][c][0]['value'])* float(Exchange_File.DivisaActual['Exchange']))                
                valorOriginal=float(Channel_File.JsonChannelFile['Bill1'][0][c][0]['value'])
            if BoardModule.device_board==2 and bill2Enabled:
                valor=(float(Channel_File.JsonChannelFile['Bill2'][0][c][0]['value'])* float(Exchange_File.DivisaActual['Exchange']))                
                valorOriginal=float(Channel_File.JsonChannelFile['Bill2'][0][c][0]['value'])
            if BoardModule.device_board==3 and coinEnabled:
                valor=(float(Channel_File.JsonChannelFile['Coin'][0][c][0]['value'])* float(Exchange_File.DivisaActual['Exchange']))                
                valorOriginal=float(Channel_File.JsonChannelFile['Coin'][0][c][0]['value'])
            if valor:
                Incrementar(valor)
                print('Total ingresado '+ str(SALDO))
                snd={"Device":str(BoardModule.device_board),"Channel":str(BoardModule.channel_board),"Currency": str(valorOriginal),"Total_amount_local_currency": str(valor)}
                BoardModule.device_board=0
                BoardModule.channel_board=0
                Ingreso=True
                return snd


            
            #agregar para controlar desde config o app
            
        sleep(0.1)

#LeerFiat=True
#LeerIngresoFiat()