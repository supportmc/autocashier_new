import os

def getUpdates(mpath):
    try:
        a=os.listdir(mpath)
        
        for x in range(len(a)): 
            print ('---> encontre archivos de update ->'+a[x])
    except:
        print('Carpeta no Legible')


def getFolders(mpath):
    try:
        a=os.listdir(mpath)
        #print('encontre pendrive -'+mpath)
        for x in range(len(a)): 
            
            if a[x]=='PSAC' or a[x]=='APP':
                getUpdates(mpath+'/'+a[x])
            #else:
            #    print ('---> encontre carpeta ->'+a[x] + ' INVALIDA')
    except:
        print('Carpeta no Legible')


def getPendrive(mpath):
    a=os.listdir(mpath)
    for x in range(len(a)): 
        print (a[x])
        getFolders(mpath+'/'+a[x])

getPendrive('/media/pi')
#getFolders('E:/')