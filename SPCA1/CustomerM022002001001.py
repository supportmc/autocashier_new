import json
import os
import SetupM022003001001

Version='022.002.001.001'

def GetVersion():
    return(str(Version))

def Read_Customer():
    try:
        #with open('Customer.json') as json_file:
        #    mijson = json.loads(json_file.read())        
        #print(mijson)
        a=SetupM022003001001.GetJsonSetup()
        return a['Customer']#mijson['Customer']/
    #Total_Start=mijson["Total_Start"]

    
    except Exception as error:
        print(error)
        return('')


        
    
    