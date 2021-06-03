import io
import serial
import os
from time import sleep
import threading
import ports
from datetime import datetime,date,time,timedelta

version='022.012.001.001'

channel_board=0
device_board=0
puerto=ports.GetPort('Board')
serie =None# serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0)    
EnviarPuerto=''
RespuestaPuerto=''
abrio=False
r=False
PuertaAbierta=False

def WriteSerie():
    global EnviarPuerto
    while 1:
        if EnviarPuerto !='':
            
            serie.write(bytes(bytearray(EnviarPuerto)))
            EnviarPuerto=''
            RespuestaPuerto=''
        sleep(0.001)

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
    serie = serial.Serial(puerto, 9600)    # timeout=0.5, writeTimeout=0.5
    EnviarPuerto=''
    RespuestaPuerto=''
    abrio=False
    r=False
    acum=b''
    qq=b''
    while True:
        try:
            
            x=1
            
            qq=serie.read(1) #aca lee del puerto
            #if qq==b'V':
            #    r=True
            
            if qq:
                acum+=qq
            else:
                break
            x+=1
            qq=acum
            abrio=True
        
            print(qq)
            #print(str(len(qq)))
            if len(qq)==1:
                #qq=qq.decode()
                if qq==b'V':
                    r=True
                    acum=b''
                if qq==b'\xb1':
                    PuertaAbierta=True
                    acum=b''
                if qq==b'\xb2':
                    PuertaAbierta=True
                    acum=b''
                if qq==b'\x00V':
                    PuertaAbierta=True
                    acum=b''
                if qq==b'\xb5':
                    PuertaAbierta=False
                    acum=b''
                if qq==b'\xb6':
                    PuertaAbierta=False
                    acum=b''
                if qq==b'\xffV':
                    PuertaAbierta=True
                    acum=b''
                
            #if len(qq)>1:
            #    print(qq)
                
            RespuestaPuerto=qq
            sleep(0.0001)
            if len(qq)>5:#  and qq[0]==170:
                acum=b''
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




            
            
            
        except Exception as e:
            puerto=ports.GetPort('Board')
            print(e)
            sleep(1)
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
            sleep(0.1)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x66]    
        while r==False and to > datetime.now():
            sleep(0.01)
    # -------------------
    
    #--------------------
    #billetero 1
    
    if bill1==True:
        r=False
        EnviarPuerto=[0x56]    
        while r==False and to > datetime.now():
            sleep(0.01)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x64]    
        while r==False and to > datetime.now():
            sleep(0.01)
     
    # -------------------
    #billetero 2 
    if bill2==True:
        r=False
        EnviarPuerto=[0x53]    
        while r==False and to > datetime.now():
            sleep(0.01) 
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x65]    
        while r==False and to > datetime.now():
            sleep(0.01)

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
    to=datetime.now()+timedelta(seconds=5)
    if bill2==True:
        r=False
        EnviarPuerto=[0x52]    
        while r==False and to > datetime.now():
            sleep(0.01)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x75]    
        while r==False and to > datetime.now():
            sleep(0.01)
     
    # -------------------
    #billetero 2 
    if bill1==True:
        r=False
        EnviarPuerto=[0x55]    
        while r==False and to > datetime.now():
            sleep(0.01) 
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x74]    
        while r==False and to > datetime.now():
            sleep(0.01)

    # -------------------
    #monedero
    if mon==True:
        r=False
        EnviarPuerto=[0x57]    
        while r==False and to > datetime.now():
            sleep(0.1)
        #luz
        # -------------------
        r=False
        EnviarPuerto=[0x76]    
        while r==False and to > datetime.now():
            sleep(0.01)
    # -------------------
    if to > datetime.now():
        return True
    else:
        return False
    

def EncenderLucesLectora():
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
        
    
    if  to > datetime.now():
        return True
    else:
        return False

def ApagarLucesLectora():
    global EnviarPuerto
    global r
    r=False
    EnviarPuerto=[0x70]
    to=datetime.now()+timedelta(seconds=3)    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x71]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x72]    
    while r==False and to > datetime.now():
        sleep(0.1) 
        
    
    if  to > datetime.now():
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
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x61]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x62]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x63]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x64]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x65]    
    while r==False and to > datetime.now():
        sleep(0.1)
    r=False
    EnviarPuerto=[0x66]    
    while r==False and to > datetime.now():
        sleep(0.1)
    if  to > datetime.now():
        return True
    else:
        return False
   
def ApagarLuces():
    global EnviarPuerto
    global r
    r=False
    to=datetime.now()+timedelta(seconds=5)    

    EnviarPuerto=[0x70]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x71]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x72]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x73]    
    while r==False and to > datetime.now():
        sleep(0.1) 
    r=False
    EnviarPuerto=[0x74]    
    while r==False and to > datetime.now():
        sleep(0.1)
    r=False
    EnviarPuerto=[0x75]    
    while r==False and to > datetime.now():
        sleep(0.1)
    r=False
    EnviarPuerto=[0x76]    
    while r==False and to > datetime.now():
        sleep(0.1)

    if  to > datetime.now():
        return True
    else:
        return False   


if (abrio==False):
    threading.Thread(target=ReadSerie).start()#ApagarLuces()
    threading.Thread(target=WriteSerie).start()#ApagarLuces()
    sleep(2)
    #r=False
    #EnviarPuerto=[0x81] 
    #sleep(1)
    #EnviarPuerto=[0x83] 
    #sleep(1)
    
    #while desPlata(True,True,True)==False:
    #    sleep(0.1)
    #print("Perfect")
    #while habPlata(True,True,True)==False:
    #    sleep(0.1)
    #print("Perfect")
    




    #ApagarLuces()
    #r=False
    #EnviarPuerto=[0x81] 
    
    
     
      


    #sleep(0.1)
    """ print("ahora")    
    r=False
    EnviarPuerto=[0x81]    
    while r==False and to > datetime.now():
        sleep(0.1) """
    #while 1:    
    #    EncenderLuces()
    #sleep(2)
    ApagarLuces()

    """ sleep(1)
    ApagarLuces()
    #    sleep(2)
    sleep(2)
    print('ya')"""
    #EncenderLucesLectora()