import pointer
import os
import sys
import datetime
import json
rutaPrincipal=""
def start():
    global rutaPrincipal
    print('starting...')
    
    global ft
    os.chdir('/home/pi/Autocashier/')

    filename='log.json'                
    data ={"Last_Start":str(datetime.datetime.now())}
    #os.remove(filename)
    #fo = open(filename, "wb")
    #print ("Name of the file: ", fo.name)
    #fo.close()
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4) 

    data=pointer.CheckPointer()    
    sys.path.append('/home/pi/Autocashier/'+str(data['SPCA'])+'/') #importa aplicacion y vista actual
    #os.chdir('/home/pi/Autocashier/'+str(data['SPCA'])+'/')
    rutaPrincipal='/home/pi/Autocashier/'+str(data['SPCA'])+'/'

    sys.path.append(rutaPrincipal)
    #import spca

    #spca.Start()

    #execute="python3 "+rutaPrincipal+"spca.py"
    #os.system(execute)
    
    
    exit()



start()