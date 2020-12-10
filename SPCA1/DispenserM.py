""" 

import io
import serial
import os
from time import sleep

def ImprimirSerie(mbyte):
#    serie = serial.Serial('/dev/serial0', 9600, timeout=0.5, writeTimeout=0)    
#    serie = serial.Serial('/dev/ttyUSB1', 9600, timeout=0.5, writeTimeout=0)    
    serie = serial.Serial('/dev/ttyUSB0', 38400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=1 )    
    serie.write(bytes(bytearray(mbyte)))
    print("envio peticion codigo - OK")
    q=''
    while len(q)==0:
        q=serie.read(1024) #aca lee del puerto
#    q=q.decode()
    print(q)
    serie.close()

while True:
    print("1-Version")
    print("2-Estado del dispencer")
    print("3-Pre-send tarjeta")
    print("4-Estado del lector de RF")
    print("5-Dispensar tarjeta")
    print("6-Verificar KEYA")
    print("7-Leer sector 0 bloque 1")
    print("8-Expender tarjeta")
    print("9-Reciclar tarjeta")
    valor=input("ingrese opcion:")
    print("Valor:",valor)
    if valor=='1':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x03,0x9B,0x0B,0xB0])#Version
    if valor=='5':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x62,0xFA,0x0B,0xB0])#dispensar tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
    if valor=='8': 
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x32,0x30,0x03,0x01,0xA8,0x0B,0xB0])#Expender tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)operacion ok  si P[12]='N'(0x4E)operacion fallida
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='E'(0x45)no hay tarjeta en el dispencer  si P[12]='W'(0x57)Tarjeta no esta en la  posciocon de  operacion permitida
    if valor=='9':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x66,0xFE,0x0B,0xB0])#seteo de reciclar  tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x32,0x33,0x03,0x02,0xA8,0x0B,0xB0])#reciclar  tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)operacion ok  si P[12]='N'(0x4E)operacion fallida
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='E'(0x45)no hay tarjeta en el dispencer  si P[12]='W'(0x57)Tarjeta no esta en la  posciocon de  operacion permitida
    if valor=='6':
#        ImprimirSerie([0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x45,0x30,0x30,0x32,0x03,0x72,0xA8,0x0B,0xB0])#leer track2 en tarjeta magnetica
        ImprimirSerie([0x0A,0xA0,0x00,0x10,0x98,0x30,0x02,0x00,0x09,0x35,0x32,0x00,0x54,0x45,0x4E,0x47,0x41,0x4D,0x03,0x1B,0xA8,0x0B,0xB0])#Verificar KEYA=TENGAM 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='Y'(0x59)OK  si P[13]='N'(0x4E)no verifica
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='E'(0x45)NO hay tarjeta en el lector  si P[13]='W'(0x57)la tarjeta no esta en la posicion de operacion permitida
    if valor=='7':
#        ImprimirSerie([0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x45,0x30,0x30,0x37,0x03,0x77,0xA8,0x0B,0xB0])#leer los 3 track en tarjeta magnetica
        ImprimirSerie([0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x35,0x33,0x00,0x01,0x03,0x02,0xA8,0x0B,0xB0])#leer bloque 0 sector 1
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='0'(0x30)fallo en encontrar tarjeta RF  si P[14]='1'(0x31)numero de sector operado error
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='3'(0x33)error de password verificada  si P[14]='4'(0x34)error de dato leido
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='E'(0x45)No hay tarjeta en el lector  si P[14]='W'(0x57)Tarjeta no esta la  posicion permitida
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='Y'(0x59)Lectura OK  

    if valor=='2':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x63,0xFB,0x0B,0xB0])#estado del dispensador
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.7]=''(1)hopper vacio  si P[7.7]=''(0)hopper con tarjetas
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.6]=''(1)tarjeta montada   si P[7.6]=''(0)tarjeta no esta montada 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.5]=''(1)tarjeta no esta en pos de pre-envio   si P[7.5]=''(0)tarjeta no esta en pos de pre-envio
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.4]=''(1)pocas tarjetas  si P[7.4]=''(0)Cantidad normal de tarjetas
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.3]=''(1)dispensando tarjetas  si P[7.3]=''(0)reposo
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.2]=''(1)reciclando tarjetas  si P[7.2]=''(0)reposo
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.1]=''(1)error dispensando tarjetas  si P[7.4]=''(0)normal
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.0]=''(1)tiene funcion de timepo max de reciclado  si P[7.0]=''(0)No tiene esta funcion

    if valor=='4':
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x31,0x30,0x03,0x02,0xA8,0x0B,0xB0])#CHECK Estado del lectorde RF     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='H'(0x48)no esta sosteniendo tarjeta en el lector, tarjeta en el frente 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='I'(0x49)tarjeta en el extremo frontal 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='J'(0x4A)tarjeta en la posicion de reposo del lector
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='K'(0x4B)tarjeta IC en posicion de operacion 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='L'(0x4C)punta trasera del lector contiene una tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='M'(0x4D)punta trasera del lector no contiene tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='N'(0x4E)No hay tarjeta dentro del lector  
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='I'(0x49)Entrada para tarjeta mangetica permitida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='J'(0x4A)Entrada para tarjeta IC/mangetica/RF permitida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='N'(0x4E)Entrada para tarjeta  prohibida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='J'(0x4A)Entrada punta trasera para tarjeta mangetica/IC/RF permitida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='J'(0x4A)Entrada punta trasera para tarjeta  prohibida 
        sleep(0.1)
#        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x3A,0x30,0x03,0x09,0xA8,0x0B,0xB0])#Estado del lector     
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x3A,0x30,0x03,0x09,0xA8,0x0B,0xB0])#Estado del lector     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)seteo ok  si P[12]='N'(0x4E)seteo no OK
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x0A,0x98,0x30,0x02,0x00,0x03,0x2F,0x31,0x30,0x03,0x2C,0xA8,0x0B,0xB0])#Permitir entrada desde  atras prohihibir enrtrada frontal     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='Y'(0x59)seteo ok  si P[13]='N'(0x4E)seteo no OK
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x2e,0x32,0x03,0x1F,0xA8,0x0B,0xB0])#Setear la poscion de permanecia de tarjeta IC     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)seteo ok  si P[12]='N'(0x4E)seteo no OK
    if valor=='3':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x62,0xFA,0x0B,0xB0])#dispensar tarjeta a posicion pre-send
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK """



import io
import serial
import os
from time import sleep

def ImprimirSerie(mbyte):
#    serie = serial.Serial('/dev/serial0', 9600, timeout=0.5, writeTimeout=0)    
#    serie = serial.Serial('/dev/ttyUSB1', 9600, timeout=0.5, writeTimeout=0)    
    serie = serial.Serial('/dev/ttyUSB0', 38400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=1 )    
    serie.write(bytes(bytearray(mbyte)))
    print("envio peticion codigo - OK")
    q=''
    while len(q)==0:
        q=serie.read(1024) #aca lee del puerto
        
    #q=q.decode()
    print(q)
    x=0
    r=[]
    while x < len(q):
        #print(chr(q[x]))
        r.append(q[x])
        x+=1

    x=0
    #r=[]
    tt=''
    while x < len(r):
        if x>=18 and x<31:
            tt=tt+chr(r[x])
        x+=1
    print('tarjeta '+ tt)
        
        
    #t=q.encode('ascii')
    #print(t)
    
    
    serie.close()

while True:
    print("1-Version")
    print("2-Estado del dispencer")
    print("3-Pre-send tarjeta")
    print("4-Estado del lector")
    print("5-Dispensar tarjeta")
    print("6-Leer track2")
    print("7-Leer los tres tracks")
    print("8-Expender tarjeta")
    print("9-Reciclar tarjeta")
    valor=input("ingrese opcion:")
    print("Valor:",valor)
    if valor=='1':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x03,0x9B,0x0B,0xB0])#Version
    if valor=='5':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x62,0xFA,0x0B,0xB0])#dispensar tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
    if valor=='8': 
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x32,0x30,0x03,0x01,0xA8,0x0B,0xB0])#Expender tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)operacion ok  si P[12]='N'(0x4E)operacion fallida
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='E'(0x45)no hay tarjeta en el dispencer  si P[12]='W'(0x57)Tarjeta no esta en la  posciocon de  operacion permitida
    if valor=='9':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x66,0xFE,0x0B,0xB0])#seteo de reciclar  tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x32,0x33,0x03,0x02,0xA8,0x0B,0xB0])#reciclar  tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)operacion ok  si P[12]='N'(0x4E)operacion fallida
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='E'(0x45)no hay tarjeta en el dispencer  si P[12]='W'(0x57)Tarjeta no esta en la  posciocon de  operacion permitida
    if valor=='6':
        ImprimirSerie([0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x45,0x30,0x30,0x32,0x03,0x72,0xA8,0x0B,0xB0])#leer track2 en tarjeta magnetica


    if valor=='7':
        ImprimirSerie([0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x45,0x30,0x30,0x37,0x03,0x77,0xA8,0x0B,0xB0])#leer los 3 track en tarjeta magnetica
    if valor=='2':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x63,0xFB,0x0B,0xB0])#estado del dispensador
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.7]=''(1)hopper vacio  si P[7.7]=''(0)hopper con tarjetas
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.6]=''(1)tarjeta montada   si P[7.6]=''(0)tarjeta no esta montada 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.5]=''(1)tarjeta no esta en pos de pre-envio   si P[7.5]=''(0)tarjeta no esta en pos de pre-envio
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.4]=''(1)pocas tarjetas  si P[7.4]=''(0)Cantidad normal de tarjetas
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.3]=''(1)dispensando tarjetas  si P[7.3]=''(0)reposo
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.2]=''(1)reciclando tarjetas  si P[7.2]=''(0)reposo
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.1]=''(1)error dispensando tarjetas  si P[7.4]=''(0)normal
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.0]=''(1)tiene funcion de timepo max de reciclado  si P[7.0]=''(0)No tiene esta funcion

    if valor=='4':
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x31,0x30,0x03,0x02,0xA8,0x0B,0xB0])#CHECK Estado del lector     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='H'(0x48)no esta sosteniendo tarjeta en el lector, tarjeta en el frente 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='I'(0x49)tarjeta en el extremo frontal 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='J'(0x4A)tarjeta en la posicion de reposo del lector
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='K'(0x4B)tarjeta IC en posicion de operacion 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='L'(0x4C)punta trasera del lector contiene una tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='M'(0x4D)punta trasera del lector no contiene tarjeta
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='N'(0x4E)No hay tarjeta dentro del lector  
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='I'(0x49)Entrada para tarjeta mangetica permitida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='J'(0x4A)Entrada para tarjeta IC/mangetica/RF permitida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='N'(0x4E)Entrada para tarjeta  prohibida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='J'(0x4A)Entrada punta trasera para tarjeta mangetica/IC/RF permitida 
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[14]='J'(0x4A)Entrada punta trasera para tarjeta  prohibida 
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x3A,0x30,0x03,0x09,0xA8,0x0B,0xB0])#Estado del lector     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)seteo ok  si P[12]='N'(0x4E)seteo no OK
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x0A,0x98,0x30,0x02,0x00,0x03,0x2F,0x31,0x30,0x03,0x2C,0xA8,0x0B,0xB0])#Permitir entrada desde  atras prohihibir enrtrada frontal     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='Y'(0x59)seteo ok  si P[13]='N'(0x4E)seteo no OK
        sleep(0.1)
        ImprimirSerie([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x2e,0x32,0x03,0x1F,0xA8,0x0B,0xB0])#Setear la poscion de permanecia de tarjeta IC     
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)seteo ok  si P[12]='N'(0x4E)seteo no OK
    if valor=='3':
        ImprimirSerie([0x0A,0xA0,0x00,0x02,0x98,0x64,0xFC,0x0B,0xB0])#dispensar tarjeta a posicion pre-send
#Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
   
    


    

