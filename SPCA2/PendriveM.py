import json
import os
import tarfile
import glob, shutil
import sys


Version='022.007.001.001'
estado = False

def IsUpdate(json1,json2):
    

def getUpdates(mpath):
    try:
        a=os.listdir(mpath)
        if mpath[-4:]=='PSAC':
            t='PSAC'
        elif mpath[-3:]=='APP':
            t='APP'
        
        #-----------------------------------------------------------------
        #importo puntero
        sys.path.append('/home/pi/Autocashier/')
        import pointer
        data=pointer.CheckPointer()
        #-----------------------------------------------------------------
        where=''
        if t=='PSAC':
            where=data['Download_SPCA']
        elif t=='APP':
            where=data['Download_APPCA']

        estado=False
        if copy_dir(mpath,'/home/pi/Autocashier/'+where)==True:
            #cambia puntero
            
            if t=='PSAC':
                estado=pointer.Change_Pointer(where,'')
            else:
                estado=pointer.Change_Pointer('',where)
            print('puntero cambiado correctamente :)')
        else:
            print('Error al copiar')

        """ for x in range(len(a)): #lista archivos de carpeta
            if (a[x][-4:]=='.tar'):                
                return '{"name":'+'"'+str(t)+'","value":"'+str(a[x][:-4])+'"}' """
        if estado==True:
            return True
        else:
            return False

    except:
        print('Carpeta no Legible')
        return False


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
    try:
        if os.path.isdir(source_item):
            make_dir(destination_item)
            sub_items = glob.glob(source_item + '/*')
            for sub_item in sub_items:
                copy_dir(sub_item, destination_item + '/' + sub_item.split('/')[-1])
        else:
            shutil.copy(source_item, destination_item)
        return True
    except:
        return False

print(getPendrive('/media/pi'))
