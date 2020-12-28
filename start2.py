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

    
    rutaPrincipal='/home/pi/Autocashier/'

    sys.path.append(rutaPrincipal)
    #import spca

    #spca.Start()

    execute="sudo python3 "+rutaPrincipal+"start.py"
    os.system(execute)
    
    
    exit()



start()