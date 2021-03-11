
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
serie =None# serial.Serial(puerto, 9600, timeout=0.5, writeTimeout=0)    
EnviarPuerto=''
RespuestaPuerto=''
abrio=False
r=False

def ReadSerie():
    global EnviarPuerto
    global channel_board
    global device_board
    global serie
    global abrio
    global RespuestaPuerto
    global r

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
            #print(qq)
            if len(qq)>0:
                qq=qq.decode()
                if qq=='V':
                    r=True
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

def habPlata():
    global EnviarPuerto
    global r

    #--------------------
    #billetero 1
    r=False
    EnviarPuerto=[0x56]    
    while r==False:
        sleep(0.001)
    #luz
    # -------------------
    r=False
    EnviarPuerto=[0x65]    
    while r==False:
        sleep(0.001)
     
    # -------------------
    #billetero 2 
    r=False
    EnviarPuerto=[0x53]    
    while r==False:
        sleep(0.001) 
    #luz
    # -------------------
    r=False
    EnviarPuerto=[0x64]    
    while r==False:
        sleep(0.001)

    # -------------------
    #monedero
    r=False
    EnviarPuerto=[0x58]    
    while r==False:
        sleep(0.01)
    #luz
    # -------------------
    r=False
    EnviarPuerto=[0x66]    
    while r==False:
        sleep(0.001)
    # -------------------

def desPlata():
    global EnviarPuerto
    global r
    r=False
    EnviarPuerto=[0x52]    
    while r==False:
        sleep(0.01)

    r=False
    EnviarPuerto=[0x55]    
    while r==False:
        sleep(0.01)

    r=False
    EnviarPuerto=[0x57]    
    while r==False:#ApagarLuces()
        sleep(0.01)
    
    

def EncenderLuces():
    global EnviarPuerto
    global r
    r=False
    EnviarPuerto=[0x60]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x61]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x62]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x63]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x64]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x65]    
    while r==False:
        sleep(0.01)
    r=False
    EnviarPuerto=[0x66]    
    while r==False:
        sleep(0.01)  
   
def ApagarLuces():
    global EnviarPuerto
    global r
    r=False
    EnviarPuerto=[0x70]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x71]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x72]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x73]    
    while r==False:
        sleep(0.01) 
    r=False
    EnviarPuerto=[0x74]    
    while r==False:
        sleep(0.01)
    r=False
    EnviarPuerto=[0x75]    
    while r==False:
        sleep(0.01)
    r=False
    EnviarPuerto=[0x76]    
    while r==False:
        sleep(0.01)   


if (abrio==False):
    threading.Thread(target=ReadSerie).start()#ApagarLuces()
    sleep(2)
    r=False
    #EnviarPuerto=[0x53] 
    desPlata()
    ApagarLuces()
    
    
     
      


    #sleep(0.001)
    """ print("ahora")    
    r=False
    EnviarPuerto=[0x81]    
    while r==False:
        sleep(0.01) """
    #EncenderLuces()