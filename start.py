import pointer
import os
import sys
rutaPrincipal=""
def start():
    global rutaPrincipal
    print('starting...')
    
    global ft
    data=pointer.CheckPointer()    
    sys.path.append('/home/pi/Autocashier/'+str(data['SPCA'])+'/') #importa aplicacion y vista actual
    #os.chdir('/home/pi/Autocashier/'+str(data['SPCA'])+'/')
    rutaPrincipal='/home/pi/Autocashier/'+str(data['SPCA'])+'/'
    execute="python3 "+rutaPrincipal+"spca.py"
    os.system(execute)
    exit()



start()