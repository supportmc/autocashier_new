import json
import os

def getUpdates(mpath):
    try:
        a=os.listdir(mpath)
        if mpath[-4:]=='PSAC':
            t='PSAC'
        elif mpath[-3:]=='APP':
            t='APP'
        
        for x in range(len(a)): 
            if (a[x][-4:]=='.tar'):                
                return '{"name":'+'"'+str(t)+'","value":"'+str(a[x][:-4])+'"}'

    except:
        print('Carpeta no Legible')


def getFolders(mpath):
    try:
        a=os.listdir(mpath)
        #print('encontre pendrive -'+mpath)
        findUpdate=[]

        for x in range(len(a)): 
        
            if a[x]=='PSAC' or a[x]=='APP':
                re=getUpdates(mpath+'/'+a[x])
                re=json.loads(re)
                
                findUpdate.append(re)#add to response
        
        return(findUpdate)
            
    except:
        print('Carpeta no Legible')


def getPendrive(mpath):
    a=os.listdir(mpath)
    for x in range(len(a)): 
        print (a[x])
        return getFolders(mpath+'/'+a[x])

print(getPendrive('/media/pi'))
#getFolders('E:/')