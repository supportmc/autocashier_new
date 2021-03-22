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
puerto=ports.GetPort('Board')
serie =None# serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0)    
EnviarPuerto=''
RespuestaPuerto=''
abrio=False
r=False
PuertaAbierta=False

def ReadSerie():
    global EnviarPuerto
    global channel_board
    global device_board
    global serie
    global abrio
    global RespuestaPuerto
    global r
    global PuertaAbierta

    channel_board=0
    device_board=0
    puerto=ports.GetPort('Board')
    serie = serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0)    
    EnviarPuerto=''
    RespuestaPuerto=''
    abrio=False
    r=True

    while True:
        try:
            qq=serie.read(1024) #aca lee del puerto
            abrio=True
            print(qq)
            #print(str(len(qq)))
            if len(qq)==1:
                #qq=qq.decode()
                if qq==b'V':
                    r=True
                if qq==b'\xb1':
                    PuertaAbierta=True
                if qq==b'\xb2':
                    PuertaAbierta=True
                if qq==b'\x00V':
                    PuertaAbierta=True
                if qq==b'\xb5':
                    PuertaAbierta=False
                if qq==b'\xb6':
                    PuertaAbierta=False
                if qq==b'\xffV':
                    PuertaAbierta=True
                
            #if len(qq)>1:
            #    print(qq)
                
            RespuestaPuerto=qq
            sleep(0.01)
            if len(qq)>5:#  and qq[0]==170:
                if qq[0]==170:
                    q=qq[2]
                else:
                    q=qq[3]
                channel_board=q
                print('canal '+str(q))
                if qq[0]==170:
                    q=qq[3]
                else:
                    q=qq[4]
                device_board=q
                print('billetero '+str(q))
            else:
                #print(qq.decode())
                a=1
            if EnviarPuerto !='':
                serie.write(bytes(bytearray(EnviarPuerto)))
                EnviarPuerto=''
                RespuestaPuerto=''
        except Exception as e:
            puerto=ports.GetPort('Board')
            print(e)
            sleep(2)
            channel_board=0
            device_board=0
            serie.close()
            serie=None
            #puerto=ports.GetPort('Board')
            #serie = serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0.3)    
            EnviarPuerto=''
            RespuestaPuerto=''
            abrio=False
            #r==True
            #continue
            break

    #print(bytearray(q))
    
    ReadSerie()

def habPlata(bill1,bill2,mon):
    global EnviarPuerto
    global r
    to=datetime.now()+timedelta(seconds=3)

    #monedero
    if mon==True:
        r=False
        EnviarPuerto=[0x58]    
        while r==False and to > datetime.now():
            sleep(0.01)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x66]    
        while r==False and to > datetime.now():
            sleep(0.001)
    # -------------------
    
    #--------------------
    #billetero 1
    
    if bill1==True:
        r=False
        EnviarPuerto=[0x56]    
        while r==False and to > datetime.now():
            sleep(0.001)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x64]    
        while r==False and to > datetime.now():
            sleep(0.001)
     
    # -------------------
    #billetero 2 
    if bill2==True:
        r=False
        EnviarPuerto=[0x53]    
        while r==False and to > datetime.now():
            sleep(0.001) 
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x65]    
        while r==False and to > datetime.now():
            sleep(0.001)

    # -------------------
    
    if  to > datetime.now():
        return True
    else:
        return False

def desPlata(bill1,bill2,mon):
    global EnviarPuerto
    global r
    #--------------------
    #billetero 2
    to=datetime.now()+timedelta(seconds=3)
    if bill2==True:
        r=False
        EnviarPuerto=[0x52]    
        while r==False and to > datetime.now():
            sleep(0.001)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x75]    
        while r==False and to > datetime.now():
            sleep(0.001)
     
    # -------------------
    #billetero 2 
    if bill1==True:
        r=False
        EnviarPuerto=[0x55]    
        while r==False and to > datetime.now():
            sleep(0.001) 
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x74]    
        while r==False and to > datetime.now():
            sleep(0.001)

    # -------------------
    #monedero
    if mon==True:
        r=False
        EnviarPuerto=[0x57]    
        while r==False and to > datetime.now():
            sleep(0.01)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x76]    
        while r==False and to > datetime.now():
            sleep(0.001)
    # -------------------
    if to > datetime.now():
        return True
    else:
        return False
    
    

def EncenderLuces():
    global EnviarPuerto
    global r
    r=False
    EnviarPuerto=[0x60]
    to=datetime.now()+timedelta(seconds=3)    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x61]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x62]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x63]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x64]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x65]    
    while r==False and to > datetime.now():
        sleep(0.01)
    r=False
    EnviarPuerto=[0x66]    
    while r==False and to > datetime.now():
        sleep(0.01)
    if  to > datetime.now():
        return True
    else:
        return False
   
def ApagarLuces():
    global EnviarPuerto
    global r
    r=False
    to=datetime.now()+timedelta(seconds=3)    

    EnviarPuerto=[0x70]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x71]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x72]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x73]    
    while r==False and to > datetime.now():
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x74]    
    while r==False and to > datetime.now():
        sleep(0.01)
    r=False
    EnviarPuerto=[0x75]    
    while r==False and to > datetime.now():
        sleep(0.01)
    r=False
    EnviarPuerto=[0x76]    
    while r==False and to > datetime.now():
        sleep(0.01)

    if  to > datetime.now():
        return True
    else:
        return False   


if (abrio==False):
    threading.Thread(target=ReadSerie).start()#ApagarLuces()
    sleep(2)
    r=False
    EnviarPuerto=[0x82] 
    sleep(1)
    EnviarPuerto=[0x83] 
    sleep(1)
    
    #while desPlata(True,True,True)==False:
    #    sleep(0.01)
    #print("Perfect")
    #while habPlata(True,True,True)==False:
    #    sleep(0.01)
    #print("Perfect")
    




    #ApagarLuces()
    #r=False
    #EnviarPuerto=[0x81] 
    
    
     
      


    #sleep(0.001)
    """ print("ahora")    
    r=False
    EnviarPuerto=[0x81]    
    while r==False and to > datetime.now():
        sleep(0.01) """
    #while 1:    
    #    EncenderLuces()
    #    sleep(2)
    #    ApagarLuces()
    #    sleep(2)