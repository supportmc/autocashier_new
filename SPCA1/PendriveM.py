import json
import os
import tarfile
import glob, shutil

Version='022.007.001.001'
estado = False

def getUpdates(mpath):
    try:
        a=os.listdir(mpath)
        if mpath[-4:]=='PSAC':
            t='PSAC'
        elif mpath[-3:]=='APP':
            t='APP'
        
        copy_dir(mpath,'/home/pi/Autocashier/SPCA2')
        """ for x in range(len(a)): 
            if (a[x][-4:]=='.tar'):                
                return '{"name":'+'"'+str(t)+'","value":"'+str(a[x][:-4])+'"}' """
        

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


def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def copy_dir(source_item, destination_item):
    if os.path.isdir(source_item):
        make_dir(destination_item)
        sub_items = glob.glob(source_item + '/*')
        for sub_item in sub_items:
            copy_dir(sub_item, destination_item + '/' + sub_item.split('/')[-1])
    else:
        shutil.copy(source_item, destination_item)

print(getPendrive('/media/pi'))
