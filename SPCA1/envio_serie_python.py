
import io
import serial
import os
from time import sleep

def ImprimirSerie(mbyte):
    serie = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5, writeTimeout=0)    
    serie.write(bytes(bytearray(mbyte)))#
    print("envio peticion codigo - OK")
    q=''
    while len(q)==0:
        q=serie.read(1024) #aca lee del puerto
        sleep(0.0001)
    q=q.decode()

    while True:
        q=serie.read(1024) #aca lee del puerto
        sleep(0.0001)
        #q=q.decode()
        print(q)

    print(bytearray(q))
    serie.close()


ImprimirSerie([0x53])#aca mandas a la placa lo que queres como parametros

    