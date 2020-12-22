import json
import os
import tarfile

Version='022.007.001.001'
estado = False

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




def Descargar(Version, Dtype, Cual):
    global error
    global estado
    global ruta
    Cual1 = Cual + '.tar'
    if Dtype == 'Soft':
        try:
            url = rutasoft + cual
            urllib.request.urlretrieve(url, '/home/pi/MC_Controller/Version_' + str(Version) + '/View/' + str(Cual))
            fname = ruta + cual
            print('--------------------------------------------')
            print('Downloading ' + str(Dtype) + ' for version ' + str(Version))
            try:
                if fname.endswith('tar'):
                    tar = tarfile.open(fname, 'r:')
                    tar.extractall()
                    tar.close()
                    os.sys('sudo rm ' + str(cual))
                    print(str(cual) + ' Downloaded OK')
                    estado = True
            except Exception as e:
                print(str(e))
                estado = False

        except:
            print('error to download soft')
            error = error + 1
            if error < 3:
                Descargar(Version, Dtype, Cual)
            else:
                estado = False

    elif Dtype == 'App':
        try:
                url = rutaapp + Cual1 #+ ' --o /home/pi/MC_Controller/Version_' + str(Version) + '/View/ -c "' + str(Cual1)+'"'
                #print(str(url))
                os.system(url)
                fname = '/home/pi/MC_Controller/Version_' + str(Version) +'/'+ str(Cual1) #+ '/View/' + str(Cual1)
                print('--------------------------------------------')
                print('Downloading ' + str(Dtype) + ' for version ' + str(Version) + ' - ' + str(Cual1))
                try:
                    sleep(3)
                    if fname.endswith('tar'):
                        #print(fname)
                        tar = tarfile.open(fname, 'r:')
                        tar.extractall()
                        tar.close()
                        os.system('sudo mv ' + str(Cual) + '/ App/')
                        os.system('sudo rm ' + str(fname))
                        print(str(Cual) + ' Downloaded OK')
                        estado = True
                except Exception as e:
                    print(str(e))
                    estado = False

        except:
            print('error to download app')
            error = error + 1
            if error < 3:
                Descargar(Version, Dtype, Cual)
            else:
                estado = False

    else:
        if Dtype == 'View':
            try:
                url = rutaview + Cual1 #+ ' --o /home/pi/MC_Controller/Version_' + str(Version) + '/View/ -c "' + str(Cual1)+'"'
                ruta_descargaOriginal='/home/pi/MC_Controller/Version_' + str(Version) +'/'
                
                #coto
                ruta_descarga='/home/pi/'

                os.system(url)
                print('Downloading ' + str(Dtype) + ' for version ' + str(Version) + ' - ' + str(Cual1))
                print('--------------------------------------------')
                print('Downloaded Ok -> ' + str(Dtype) + ' for version ' + str(Version) + ' - ' + str(Cual1))

                fname = ruta_descarga + str(Cual1) #+ '/View/' + str(Cual1)
                try:
                    
                    #print(str(carpeta))
                    x=0
                    while os.path.isfile(fname)==False and x < 100:
                        print('esperando que aparezca el archivo descargado...% '+ str(x))
                        x+=1
                        sleep(0.5)

                    print('Esta archivo ' + str(os.path.isfile(fname)))
                    if x==100:
                        print('error to download view ' + str(Cual))
                        return 'Error'

                    #sleep(2)
                    if fname.endswith('tar'):
                        #print(fname)
                        try:
                            tar = tarfile.open(fname, 'r:')
                            tar.extractall()
                            tar.close()
                        except Exception as e:
                            print('Error al extraer '+str(e))
                        #sleep(5)    
                        os.system('sudo mv '+str(ruta_descarga) + str(Cual) + '/ '+ str(ruta_descargaOriginal) +'View/')
                        os.system('sudo rm ' + str(fname))
                        print(str(Cual) + ' Extracted OK')
                        estado = True
                except Exception as e:
                    print(str(e))
                    estado = False

            except Exception as e:
                print('error to download view ' + str(e))
                error = error + 1
                if error < 3:
                    Descargar(Version, Dtype, Cual)
                else:
                    estado = False

        if estado == True:
            return 'OK'
        else:
            return 'Error'

print(getPendrive('/media/pi'))
