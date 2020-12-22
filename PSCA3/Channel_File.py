import json
import os
from time import sleep

import BoardModule
#primer punto Soft
#segundo punto Modulo
#tercer modificaciones de app
Version='001'

JsonChannelFile=""


def GetJsonChannel():
    global JsonChannelFile
    if JsonChannelFile=='':
        JsonChannelFile=Read_ChannelJson()
    return JsonChannelFile

def Read_ChannelJson():
    global JsonChannelFile
    try:
        with open('/home/pi/Autocashier/SPCA1/channel.json') as json_file:
            JsonChannelFile = json.loads(json_file.read())        
        #print(mijson)
        return JsonChannelFile
    #Total_Start=mijson["Total_Start"]

    except Exception as error:
        print(error)
        return('')
#canales=GetJsonChannel()


""" while True:
    if BoardModule.channel_board !=0:
        c='Ch'+ str(BoardModule.channel_board)
        print('Entro '+ str(float(canales['Bill1'][0][c][0]['value'])/100) + ' ' +str(canales['Bill1'][0]['Ch1'][0]['type']))
        BoardModule.channel_board=0
        BoardModule.device_board=''
    sleep(1) """
