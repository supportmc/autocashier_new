
import io
import serial
import os
from time import sleep

channel_board=0
device_board=0


def ImprimirSerie(mbyte):
    global channel_board
    global device_board
    serie = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5, writeTimeout=0)    
    serie.write(bytes(bytearray(mbyte)))#
    print("envio peticion codigo - OK")
    q=''
    while len(q)==0:
        q=serie.read(1024) #aca lee del puerto
        sleep(0.0001)
    #q=q.decode()

    while True:
        qq=serie.read(1024) #aca lee del puerto
        sleep(0.0001)
        if len(qq)>5:
            q=qq[2]
            channel_board=q
            print('canal '+str(q))
            q=qq[3]
            device_board=q
            print('billetero '+str(q))

    print(bytearray(q))
    serie.close()


ImprimirSerie([0x56])#aca mandas a la placa lo que queres como parametros

    