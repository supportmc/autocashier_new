import json
import os


Version='001'

def GetVersion():
    return(str(Version))

def CheckPointer():
    try:
        data = Read_Pointer()
        if data=='':
            return False
        return {"SPCA":data['StartSPCA'],"APPCA":data['StartAPPCA']}    
    except Exception as e:
        return False

def Read_Pointer():
    try:
        with open('pointer.json') as json_file:
            mijson = json.loads(json_file.read())        
        #print(mijson)
        return mijson

    

    
    except Exception as error:
        print(error)
        return('')

def Change_Pointer(newpointerSP,newpointerAPP):
    try:
        
        filename='pointer.json'            
        
        data = Read_Pointer()
        if data=='':
            return False
        
        #Change Principal Software
        if newpointerSP=='SPCA1':
            data['StartSPCA'] = 'SPCA1'
            data['DownloadSPCA'] = 'SPCA2'
        else:
            data['StartSPCA'] = 'SPCA2'
            data['DownloadSPCA'] = 'SPCA1'

        #Change Principal App
        if newpointerAPP=='APPCA1':
            data['StartAPPCA'] = 'APPCA1'
            data['DownloadAPPCA'] = 'APPCA2'
        else:
            data['StartAPPCA'] = 'APPCA2'
            data['DownloadAPPCA'] = 'APPCA1'

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print('Partial Counter start reset Ok')
        return(True)
    except Exception as error:
        print(str(error) + ' Error to reset partial start counter')
        return False

#print(Change_Pointer('SPCA1','APPCA1'))