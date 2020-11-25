
import io
import serial
import os
from time import sleep
import threading

channel_board=0
device_board=0
serie = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5, writeTimeout=0)    
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
        qq=serie.read(1024) #aca lee del puerto
        sleep(0.001)
        if len(qq)>5:
            q=qq[2]
            channel_board=q
            print('canal '+str(q))
            q=qq[3]
            device_board=q
            print('billetero '+str(q))
        else:
            print(qq.decode())
        if EnviarPuerto !='':
            serie.write(bytes(bytearray(EnviarPuerto)))
            EnviarPuerto=''

    #print(bytearray(q))
    serie.close()

if (abrio==False):
    threading.Thread(target=ReadSerie).start()


    