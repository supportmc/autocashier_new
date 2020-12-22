
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
abrio=False
def ReadSerie():
    global EnviarPuerto
    global channel_board
    global device_board
    global serie
    global abrio

    abrio=True
    

    while True:
        try:
            qq=serie.read(1024) #aca lee del puerto
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
        except Exception as e:
            print(e)
            continue

    #print(bytearray(q))
    serie.close()

if (abrio==False):
    threading.Thread(target=ReadSerie).start()
    EnviarPuerto=[0x89]  
    sleep(5)
    EnviarPuerto=[0x53]    
    sleep(1)
    EnviarPuerto=[0x56]
    print('abrio todo')  


  