
import io
import serial
import os
from time import sleep
import threading
import ports

version='022.012.001.001'

channel_board=0
device_board=0
puerto=ports.GetPort('Board')
serie = serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0)    
EnviarPuerto=''
RespuestaPuerto=''
abrio=False
def ReadSerie():
    global EnviarPuerto
    global channel_board
    global device_board
    global serie
    global abrio
    global RespuestaPuerto

    abrio=True
    

    while True:
        try:
            qq=serie.read(1024) #aca lee del puerto
            #print(qq)
            RespuestaPuerto=qq
            sleep(0.001)
            if len(qq)>5:
                q=qq[2]
                channel_board=q
                #print('canal '+str(q))
                q=qq[3]
                device_board=q
                #print('billetero '+str(q))
            else:
                #print(qq.decode())
                a=1
            if EnviarPuerto !='':
                serie.write(bytes(bytearray(EnviarPuerto)))
                EnviarPuerto=''
                RespuestaPuerto=''
        except Exception as e:
            print(e)
            sleep(1)
            channel_board=0
            device_board=0
            puerto=ports.GetPort('Board')
            serie = serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0.1)    
            EnviarPuerto=''
            RespuestaPuerto=''
            abrio=False
            continue

    #print(bytearray(q))
    serie.close()

if (abrio==False):
    threading.Thread(target=ReadSerie).start()
    EnviarPuerto=[0x59]  
      


  