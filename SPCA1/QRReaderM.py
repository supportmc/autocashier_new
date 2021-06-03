import io
import serial
import os
from time import sleep
import threading
import ports
from datetime import datetime,date,time,timedelta

version='022.020.001.001'

channel_board=0
device_board=0
puerto=ports.GetPort('QRR')
serie =None# serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0)    
EnviarPuerto=''
RespuestaPuerto=''
abrio=False
r=False
PuertaAbierta=False
TarjetaQr=''

def ReadSerie():
    global EnviarPuerto
    global channel_board
    global device_board
    global serie
    global abrio
    global RespuestaPuerto
    global r
    global PuertaAbierta
    global TarjetaQr

    channel_board=0
    device_board=0
    puerto=ports.GetPort('QRR')
    serie = serial.Serial(puerto, 115200, timeout=0.5, writeTimeout=0.5)    
    EnviarPuerto=''
    RespuestaPuerto=''
    abrio=False
    r=True

    while True:
        try:
            qq=serie.read(100) #aca lee del puerto
            abrio=True
            #qq=qq.decode()
            if qq:
                TarjetaQr=qq[:-2].decode()
                if TarjetaQr.find('?')>-1:
                    TarjetaQr=TarjetaQr[:-1]

                print(TarjetaQr)
            
            
        except Exception as e:
            puerto=ports.GetPort('QRR')
            print(e)
            sleep(2)
            
            serie.close()
            serie=None
            #puerto=ports.GetPort('Board')
            #serie = serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0.3)    
            
            
            abrio=False
            #r==True
            #continue
            break

    #print(bytearray(q))
    
    ReadSerie()




if (abrio==False):
    threading.Thread(target=ReadSerie).start()#ApagarLuces()
