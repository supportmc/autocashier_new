import json
import io
import serial
import os
from time import sleep
import ports

intentos=0

version="022.009.001.001"

def SendDispenser(transaction):
    global intentos
    puerto=ports.GetPort('Dispenser')   
    try:
        serie = serial.Serial(puerto, 38400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=2 )    

        """ print("1-Version")
        print("2-Estado del dispencer")
        print("3-Pre-send tarjeta")
        print("4-Estado del lector")
        print("5-Dispensar tarjeta")
        print("6-Leer track2")
        print("7-Leer los tres tracks")
        print("8-Expender tarjeta")
        print("9-Reciclar tarjeta")
        valor=input("ingrese opcion:")
        print("Valor:",valor) """
        if transaction=='1':
            mbyte=[0x0A,0xA0,0x00,0x02,0x98,0x03,0x9B,0x0B,0xB0]#Version
            serie.write(bytes(bytearray(mbyte)))
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
            print(q)
        if transaction=='5':
            mbyte=[0x0A,0xA0,0x00,0x02,0x98,0x62,0xFA,0x0B,0xB0]#dispensar tarjeta
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
            serie.write(bytes(bytearray(mbyte)))
            print("envio peticion codigo - OK")
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
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
                if x==6:
                    tt=r[x]
                x+=1
            print('tarjeta preparada '+ str(tt))


        if transaction=='8': 
            mbyte=[0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x32,0x30,0x03,0x01,0xA8,0x0B,0xB0]#Expender tarjeta
            serie.write(bytes(bytearray(mbyte))) 
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)operacion ok  si P[12]='N'(0x4E)operacion fallida
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='E'(0x45)no hay tarjeta en el dispencer  si P[12]='W'(0x57)Tarjeta no esta en la  posciocon de  operacion permitida
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
            print(q)
        if transaction=='9':
            mbyte=[0x0A,0xA0,0x00,0x02,0x98,0x66,0xFE,0x0B,0xB0]#seteo de reciclar  tarjeta
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
            serie.write(bytes(bytearray(mbyte)))
            sleep(0.5)
            mbyte=[0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x32,0x33,0x03,0x02,0xA8,0x0B,0xB0]#reciclar  tarjeta
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)operacion ok  si P[12]='N'(0x4E)operacion fallida
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='E'(0x45)no hay tarjeta en el dispencer  si P[12]='W'(0x57)Tarjeta no esta en la  posciocon de  operacion permitida
            serie.write(bytes(bytearray(mbyte)))
            sleep(0.5)
        if transaction=='6':
            mbyte=[0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x45,0x30,0x30,0x32,0x03,0x72,0xA8,0x0B,0xB0]#leer track2 en tarjeta magnetica
            serie.write(bytes(bytearray(mbyte)))
            print("envio peticion codigo - OK")
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
            print(q)
            x=0
            r=[]
            while x < len(q):
                #print(chr(q[x]))
                r.append(q[x])
                x+=1

            x=0
            #r=[]

            """ tt=''
            while x < len(r):
                if x>=18 and x<31:
                    tt=tt+chr(r[x])
                x+=1
            try:
                a=float(tt)
                return(str(tt))
            except:
                if intentos <3:
                    intentos+=1
                    print('reintenta')
                    SendDispenser(transaction)
                else:
                    return '' """
            tt=''
            p=str(q).find('1fY')
            if p> -1:
                tt=str(q)[p+3:p+16]
            
                return(tt)
            else:
                if intentos <3:
                    intentos+=1
                    print('reintenta')
                    sleep(0.15)
                    return(SendDispenser(transaction))
                else:
                    return ''


        #------
        if transaction=='16':
            mbyte=[0x0A,0xA0,0x00,0x10,0x98,0x30,0x02,0x00,0x09,0x35,0x32,0x00,0x54,0x45,0x4E,0x47,0x41,0x4D,0x03,0x1B,0xA8,0x0B,0xB0]#Verificar KEYA=TENGAM
            serie.write(bytes(bytearray(mbyte)))
            sleep(0.12)
            print("envio peticion codigo - OK")
            mbyte=[0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x35,0x33,0x00,0x01,0x03,0x02,0xA8,0x0B,0xB0]#leer bloque 0 sector 1
            serie.write(bytes(bytearray(mbyte)))
            sleep(0.12)
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
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
            p=str(q).find('01Y')
            if p> -1:
                tt=str(q)[p+4:p+17]
                print(tt)
                return(tt)
            else:
                if intentos <3:
                    intentos+=1
                    print('reintenta')
                    sleep(0.1)
                    return(SendDispenser(transaction))
                else:
                    return ''
        
        if transaction=='7':
            mbyte=[0x0A,0xA0,0x00,0x0B,0x98,0x30,0x02,0x00,0x04,0x45,0x30,0x30,0x37,0x03,0x77,0xA8,0x0B,0xB0]#leer los 3 track en tarjeta magnetica
        if transaction=='2':
            mbyte=[0x0A,0xA0,0x00,0x02,0x98,0x63,0xFB,0x0B,0xB0]#estado del dispensador
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.7]=''(1)hopper vacio  si P[7.7]=''(0)hopper con tarjetas
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.6]=''(1)tarjeta montada   si P[7.6]=''(0)tarjeta no esta montada 
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.5]=''(1)tarjeta no esta en pos de pre-envio   si P[7.5]=''(0)tarjeta no esta en pos de pre-envio
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.4]=''(1)pocas tarjetas  si P[7.4]=''(0)Cantidad normal de tarjetas
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.3]=''(1)dispensando tarjetas  si P[7.3]=''(0)reposo
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.2]=''(1)reciclando tarjetas  si P[7.2]=''(0)reposo
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.1]=''(1)error dispensando tarjetas  si P[7.4]=''(0)normal
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7.0]=''(1)tiene funcion de timepo max de reciclado  si P[7.0]=''(0)No tiene esta funcion
            serie.write(bytes(bytearray(mbyte)))
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
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
                if x==6:
                    tt=r[x]
                x+=1
            """ if tt==200:
            if tt==201:
            if tt==202:
            if tt==203:
            if tt==204:
            if tt==205:
            if tt==206:
            if tt==207: """

            aa=str(bin(tt)).lstrip('0b')
            jsonreturn={"Hopper Status":aa[0:1],"Bezel Status":aa[1:2],"Pre Send Status":aa[2:3],"LessCard Status":aa[3:4],"Dispensing":aa[4:5],"Collecting":aa[5:6],"Error":aa[6:7]}

            
            return(jsonreturn)

        if transaction=='4':
            mbyte=[0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x31,0x30,0x03,0x02,0xA8,0x0B,0xB0]#CHECK Estado del lector     
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
            serie.write(bytes(bytearray(mbyte)))
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
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
                if x==11:
                    if chr(r[x])=='H':
                        print('tarjeta en el frente')
                        return {"Lector Ocupado":1}
                    if chr(r[x])=='I':
                        print('tarjeta en el  extremo frontal')
                        return {"Lector Ocupado":1}
                    if chr(r[x])=='J':
                        print('tarjeta en reposo')
                        return {"Lector Ocupado":1}
                    if chr(r[x])=='K':
                        print('tarjeta IC en posicion de operacion')
                        return {"Lector Ocupado":1}
                    if chr(r[x])=='L':
                        print('punta trasera del lector ocupado')
                    if chr(r[x])=='M':
                        print('punta trasera del lector libre')
                    if chr(r[x])=='N':
                        print('sin tarjeta en el lector')
                        return {"Lector Ocupado":0}
                if x==12:
                    if chr(r[x])=='I':
                        print('tarjeta en el  extremo frontal')
                    if chr(r[x])=='J':
                        print('tarjeta en reposo')
                    if chr(r[x])=='N':
                        print('sin tarjeta en el lector')
                if x==13:
                    
                    if chr(r[x])=='J':
                        print('entrada trasera para tarjeta permitida')
                    if chr(r[x])=='K':
                        print('entrada trasera para tarjeta prohibida')
                    
                x+=1
            #print('pre dispensar tarjeta '+ str(tt)) 
            sleep(0.1)
            mbyte=[0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x2e,0x32,0x03,0x1F,0xA8,0x0B,0xB0]#Setear la poscion de permanecia de tarjeta IC     ([0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x3A,0x30,0x03,0x09,0xA8,0x0B,0xB0])#Estado del lector     
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)seteo ok  si P[12]='N'(0x4E)seteo no OK
            serie.write(bytes(bytearray(mbyte))) 
            sleep(0.1)
            mbyte=[0x0A,0xA0,0x00,0x0A,0x98,0x30,0x02,0x00,0x03,0x2F,0x31,0x30,0x03,0x2C,0xA8,0x0B,0xB0]#Permitir entrada desde  atras prohihibir enrtrada frontal 
            serie.write(bytes(bytearray(mbyte)))     
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[13]='Y'(0x59)seteo ok  si P[13]='N'(0x4E)seteo no OK
            sleep(0.1)
            mbyte=[0x0A,0xA0,0x00,0x09,0x98,0x30,0x02,0x00,0x02,0x2e,0x32,0x03,0x1F,0xA8,0x0B,0xB0]#Setear la poscion de permanecia de tarjeta IC     
            serie.write(bytes(bytearray(mbyte))) 
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[12]='Y'(0x59)seteo ok  si P[12]='N'(0x4E)seteo no OK
        if transaction=='3':
            mbyte=[0x0A,0xA0,0x00,0x02,0x98,0x64,0xFC,0x0B,0xB0]#dispensar tarjeta a posicion pre-send
            #Verificar  el byte P de estado de opraecion  en la respuesta , si P[7]=''(0x00)estado ok  si P[7]=''(0x01)estado no OK
            serie.write(bytes(bytearray(mbyte)))
            print("envio peticion codigo - OK")
            q=''
            while len(q)==0:
                q=serie.read(1024) #aca lee del puerto
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
                if x==6:
                    tt=r[x]
                x+=1
            jsonreturn={"pre send":tt}
            return (jsonreturn)
    except Exception as er:
        if er.args[0]=='Attempting to use a port that is not open':
            return('Port Error')

    

    serie.close()

#print(str(SendDispenser('1')))
#sleep(1)
#print(str(SendDispenser('2')))


""" SendDispenser('4')
sleep(4)
SendDispenser('3')
sleep(4)
SendDispenser('2')
sleep(4)
SendDispenser('5')
sleep(4)
SendDispenser('6')
sleep(4)
SendDispenser('8') """
    

def sacarTarjeta(tipo):
    tarjeta=''
    
    while tarjeta=='':
        r=SendDispenser('4')
        if r=='Port Error':
            return  {"status":"Error"}
        if r['Lector Ocupado']==0:
            r=SendDispenser('2')
            rj=r
            #"Bezel Status":aa[1:2],"Pre Send Status"
            if rj['Bezel Status']=='0':
                print('tarjeta no preparada')
            if rj['Pre Send Status']=='0':
                print('No hay tarjeta')
                #return
            if rj['LessCard Status']=='1' and  rj['Pre Send Status']=='0':
                print('precaucion, no hay tarjetas')
                #return
                break
            if rj['Error']=='1':
                SendDispenser('9')


            SendDispenser('3')
            sleep(0.11)
            SendDispenser('4')
            sleep(0.11)
            SendDispenser('5')
            sleep(0.11)
        
        sleep(0.1)
        if tipo=='M':
            tm=SendDispenser('6')
            tarjeta=tm
        else:
            tn=SendDispenser('16')
            tarjeta=tn
        
        if tarjeta !='' and tarjeta !=None:
            print('leyo tarjeta '+ str(tarjeta))
        
        if tarjeta!='' and tarjeta !=None:
            sleep(0.1)
            r=SendDispenser('2')
            rj=r
            #"Bezel Status":aa[1:2],"Pre Send Status"
            if rj['Bezel Status']=='0':
                print('tarjeta no preparada')
            if rj['Pre Send Status']=='0':
                print('No hay tarjeta')
                #return
            if rj['LessCard Status']=='1' and  rj['Pre Send Status']=='0' and tarjeta =='':
                print('precaucion, no hay tarjetas')
                #SendDispenser('9')
                break
            if rj['Error']=='1':
                SendDispenser('9')
        else:
            break
        
            
        

    sleep(1)
    if tarjeta!='' and tarjeta !=None:
        t=tarjeta
        SendDispenser('8')
        return {"status":"Ok","card_number":t}
    else:
        #SendDispenser('8')
        SendDispenser('9')
        return {"status":"Error","msg":"Invalid Card"}
        
    

#r={"status":"Error"}
#while r['status']=='Error':
#    r=sacarTarjeta('N')
#    sleep(1.5)
#print(r)
sacarTarjeta('N')

#SendDispenser('3') 
#SendDispenser('4') 
#SendDispenser('5') 
#SendDispenser('8')
