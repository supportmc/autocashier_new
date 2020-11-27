import json
import os
import datetime

import time
import SetupM022003001001


Version='022.001.001.001'

def GetVersion():
    return(str(Version))

def Read_CounterStart():
    try:
        #with open('setup.json') as json_file:
        #    mijson = json.loads(json_file.read())        
        #print(mijson)
        j=SetupM022003001001.GetJsonSetup()

        return j
    #Total_Start=mijson["Total_Start"]

    
    except Exception as error:
        print(error)
        return('')

def Reset_CounterStart():
    try:
        
        #filename='setup.json'            
        
        data = SetupM022003001001.GetJsonSetup()#Read_CounterStart()
        if data=='':
            return False
        

        data['Total_Start'] = data['Total_Start']
        data['Parcial_Start'] = 0
        data['SPAC_Start'] = data['SPAC_Start']
        data['APPAC_Start'] = data['APPAC_Start']
        data['VAC_Start'] = data['VAC_Start']
        data['LastReset'] = time.strftime("%d/%m/%y")+' '+time.strftime("%H:%M:%S")

        SetupM022003001001.SetJsonSetup(data)#send update json file
        #os.remove(filename)
        #with open(filename, 'w') as f:
        #    json.dump(data, f, indent=4)
        print('Partial Counter start reset Ok')
        return(True)


    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False

def Change_CounterStart():
    try:
        
        filename='setup.json'            
        
        data = Read_CounterStart()
        if data=='':
            return False
        

        data['Total_Start'] = round(int(data['Total_Start'])+1,0)
        data['Parcial_Start'] = round(int(data['Parcial_Start'])+1,0)
        data['SPAC_Start'] = round(int(data['SPAC_Start'])+1,0)
        data['APPAC_Start'] = round(int(data['APPAC_Start'])+1,0)
        data['VAC_Start'] = round(int(data['VAC_Start'])+1,0)
        data['LastReset'] = data['LastReset']

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return(True)


    except Exception as error:
        print(error)
        return False
        
    
   