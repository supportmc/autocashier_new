import os.path #IMPORTA MODULO DE LIBRERIAS
import time #IMPORTA MODULO DE LIBRERIAS
import sys
from os import remove #IMPORTA MODULO DE LIBRERIAS

RedActual = '/home/pi/Autocashier/NUC/RedActual.txt' #VARIABLE CON RUTA DEL ARCHIVO TXT
Perfil_UNK = '/home/pi/Autocashier/NUC/PerfilesGenerados/PerfilUNK.xml' #VARIABLE CON RUTA DE SALIDA DEL XML QUE IRA A LA NUC
Perfil_WEP = '/home/pi/Autocashier/NUC/PerfilesGenerados/PerfilWEP.xml'
Perfil_WPA = '/home/pi/Autocashier/NUC/PerfilesGenerados/PerfilWPA.xml'
Perfil_WPA2 = '/home/pi/Autocashier/NUC/PerfilesGenerados/PerfilWPA2.xml'

PerfilNUC_UNK = '/home/pi/Autocashier/NUC/PerfilNUC/PerfilUNK.xml'
PerfilNUC_WEP = '/home/pi/Autocashier/NUC/PerfilNUC/PerfilWEP.xml'
PerfilNUC_WPA = '/home/pi/Autocashier/NUC/PerfilNUC/PerfilWPA.xml'
PerfilNUC_WPA2 = '/home/pi/Autocashier/NUC/PerfilNUC/PerfilWPA2.xml'
BanderaConectado = '/home/pi/Autocashier/NUC/conectado'
log = '/home/pi/Autocashier/NUC/log.txt'

SSID = "MAL"
PASS = "MAL"

if os.path.exists(Perfil_UNK): #PREGUNTA SI EXISTE UN ARCHIVO XML GENENERADO CON ANTERIORIDAD
    remove(Perfil_UNK) #BORRA EL VIEJO ARCHIVO XML
if os.path.exists(Perfil_WEP): #PREGUNTA SI EXISTE UN ARCHIVO XML GENENERADO CON ANTERIORIDAD
    remove(Perfil_WEP) #BORRA EL VIEJO ARCHIVO XML
if os.path.exists(Perfil_WPA): #PREGUNTA SI EXISTE UN ARCHIVO XML GENENERADO CON ANTERIORIDAD
    remove(Perfil_WPA) #BORRA EL VIEJO ARCHIVO XML
if os.path.exists(Perfil_WPA2): #PREGUNTA SI EXISTE UN ARCHIVO XML GENENERADO CON ANTERIORIDAD
    remove(Perfil_WPA2) #BORRA EL VIEJO ARCHIVO XML

if os.path.exists(BanderaConectado): #PREGUNTA SI EXISTE ARCHIVO "CONECTADO"
    remove(BanderaConectado)
    if os.path.exists(RedActual): #PREGUNTA SI EXISTE ARCHIVO TXT Y REALIZA LO SIGUIENTE
        with open(RedActual, "r") as ArchivoTXT: #ABRE EL ARCHIVO TXT COMO LECTURA
            SSID = ArchivoTXT.readline()
            PASS = ArchivoTXT.readline()
        ArchivoTXT.close()
        
        if os.path.exists(PerfilNUC_UNK):
            with open(PerfilNUC_UNK, "r") as XML_NUC_UNK: #LEE EL PERFIL XML DE LA NUC
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_UNK.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = SSID_NUC.replace('\t\t\t<name>', '') #LIMPIA LA LINEA 8 DEJANDO SOLO EL SSID
                SSID_NUC = SSID_NUC.replace('</name>\n', '') #LIMPIA LA LINEA 8 DEJANDO SOLO EL SSID
            XML_NUC_UNK.close() #CIERRA EL ARCHIVO XML DE LA NUC
            print(SSID)
            print(SSID_NUC)
            if SSID == SSID_NUC: #PREGUNTA SI SSID DEL TXT ES IGUAL AL XML DE LA NUC
                print("FIN DEL PROGRAMA") #DEVUELVE EN PANTALLA "FIN DEL PROGRAMA" 
                sys.exit() #CIERRA EL PROGRAMA
        
        if os.path.exists(PerfilNUC_WEP):
            with open(PerfilNUC_WEP, "r") as XML_NUC_WEP: #LEE EL PERFIL XML DE LA NUC
                SSID_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = SSID_NUC.replace('\t\t\t<name>', '') #LIMPIA LA LINEA 6 DEJANDO SOLO EL SSID
                SSID_NUC = SSID_NUC.replace('</name>\n', '') #LIMPIA LA LINEA 6 DEJANDO SOLO EL SSID
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WEP.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = PASS_NUC.replace('\t\t\t\t<keyMaterial>', '') #LIMPIA LA LINEA 21 DEJANDO SOLO LA CONTRASEÑA
                PASS_NUC = PASS_NUC.replace('</keyMaterial>\n', '') #LIMPIA LA LINEA 21 DEJANDO SOLO LA CONTRASEÑA
            XML_NUC_WEP.close() #CIERRA EL ARCHIVO XML DE LA NUC
            print(SSID)
            print(SSID_NUC)
            print(PASS)
            print(PASS_NUC)
            if (SSID == SSID_NUC) and (PASS == PASS_NUC): #PREGUNTA SI SSID DEL TXT ES IGUAL AL XML DE LA NUC
                print("FIN DEL PROGRAMA") #DEVUELVE EN PANTALLA "FIN DEL PROGRAMA" 
                sys.exit() #CIERRA EL PROGRAMA

        if os.path.exists(PerfilNUC_WPA):
            with open(PerfilNUC_WPA, "r") as XML_NUC_WPA: #LEE EL PERFIL XML DE LA NUC
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = SSID_NUC.replace('\t\t\t<name>', '') #LIMPIA LA LINEA 8 DEJANDO SOLO EL SSID
                SSID_NUC = SSID_NUC.replace('</name>\n', '') #LIMPIA LA LINEA 8 DEJANDO SOLO EL SSID
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = PASS_NUC.replace('\t\t\t\t<keyMaterial>', '') #LIMPIA LA LINEA 21 DEJANDO SOLO LA CONTRASEÑA
                PASS_NUC = PASS_NUC.replace('</keyMaterial>\n', '') #LIMPIA LA LINEA 21 DEJANDO SOLO LA CONTRASEÑA
            XML_NUC_WPA.close() #CIERRA EL ARCHIVO XML DE LA NUC
            print(SSID)
            print(SSID_NUC)
            print(PASS)
            print(PASS_NUC)
            if (SSID == SSID_NUC) and (PASS == PASS_NUC): #PREGUNTA SI SSID DEL TXT ES IGUAL AL XML DE LA NUC
                print("FIN DEL PROGRAMA") #DEVUELVE EN PANTALLA "FIN DEL PROGRAMA" 
                sys.exit() #CIERRA EL PROGRAMA

        if os.path.exists(PerfilNUC_WPA2):
            with open(PerfilNUC_WPA2, "r") as XML_NUC_WPA2: #LEE EL PERFIL XML DE LA NUC
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 6 DEL XML
                SSID_NUC = SSID_NUC.replace('\t\t\t<name>', '') #LIMPIA LA LINEA 8 DEJANDO SOLO EL SSID
                SSID_NUC = SSID_NUC.replace('</name>\n', '') #LIMPIA LA LINEA 8 DEJANDO SOLO EL SSID
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = XML_NUC_WPA2.readline() #BAJA HASTA LA LINEA 21 DEL XML
                PASS_NUC = PASS_NUC.replace('\t\t\t\t<keyMaterial>', '') #LIMPIA LA LINEA 21 DEJANDO SOLO LA CONTRASEÑA
                PASS_NUC = PASS_NUC.replace('</keyMaterial>\n', '') #LIMPIA LA LINEA 21 DEJANDO SOLO LA CONTRASEÑA
            XML_NUC_WPA2.close() #CIERRA EL ARCHIVO XML DE LA NUC
            print(SSID)
            print(SSID_NUC)
            print(PASS)
            print(PASS_NUC)
            if (SSID == SSID_NUC) and (PASS == PASS_NUC): #PREGUNTA SI SSID DEL TXT ES IGUAL AL XML DE LA NUC
                print("FIN DEL PROGRAMA") #DEVUELVE EN PANTALLA "FIN DEL PROGRAMA" 
                sys.exit() #CIERRA EL PROGRAMA
        
        with open(Perfil_UNK, "w") as XML_UNK: #EMPIEZA A CREAR EL ARCHIVO XML
            XML_UNK.write('<?xml version="1.0"?>\n') 
            XML_UNK.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_UNK.write('\t<name>')
            XML_UNK.write(SSID)
            XML_UNK.write('</name>\n')
            XML_UNK.write('\t<SSIDConfig>\n')
            XML_UNK.write('\t\t<SSID>\n')
            XML_UNK.write('\t\t\t<name>')
            XML_UNK.write(SSID)
            XML_UNK.write('</name>\n')
            XML_UNK.write('\t\t</SSID>\n')
            XML_UNK.write('\t</SSIDConfig>\n')
            XML_UNK.write('\t<connectionType>ESS</connectionType>\n')
            XML_UNK.write('\t<connectionMode>auto</connectionMode>\n')
            XML_UNK.write('\t<MSM>\n')
            XML_UNK.write('\t\t<security>\n')
            XML_UNK.write('\t\t\t<authEncryption>\n')
            XML_UNK.write('\t\t\t\t<authentication>open</authentication>\n')
            XML_UNK.write('\t\t\t\t<encryption>none</encryption>\n')
            XML_UNK.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_UNK.write('\t\t\t</authEncryption>\n')
            XML_UNK.write('\t\t\t</security>\n')
            XML_UNK.write('\t</MSM>\n')
            XML_UNK.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_UNK.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_UNK.write('\t</MacRandomization>\n')
            XML_UNK.write('</WLANProfile>')
        XML_UNK.close() #CIERRA EL ARCHIVO XML
        
        with open(Perfil_WEP, "w") as XML_WEP: #EMPIEZA A CREAR EL ARCHIVO XML
            XML_WEP.write('<?xml version="1.0"?>\n')
            XML_WEP.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_WEP.write('\t<name>')
            XML_WEP.write(SSID)
            XML_WEP.write('</name>\n')
            XML_WEP.write('\t<SSIDConfig>\n')
            XML_WEP.write('\t\t<SSID>\n')
            XML_WEP.write('\t\t\t<name>')
            XML_WEP.write(SSID)
            XML_WEP.write('</name>\n')
            XML_WEP.write('\t\t</SSID>\n')
            XML_WEP.write('\t</SSIDConfig>\n')
            XML_WEP.write('\t<connectionType>ESS</connectionType>\n')
            XML_WEP.write('\t<connectionMode>auto</connectionMode>\n')
            XML_WEP.write('\t<MSM>\n')
            XML_WEP.write('\t\t<security>\n')
            XML_WEP.write('\t\t\t<authEncryption>\n')
            XML_WEP.write('\t\t\t\t<authentication>open</authentication>\n')
            XML_WEP.write('\t\t\t\t<encryption>WEP</encryption>\n')
            XML_WEP.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_WEP.write('\t\t\t</authEncryption>\n')
            XML_WEP.write('\t\t\t<sharedKey>\n')
            XML_WEP.write('\t\t\t\t<keyType>networkKey</keyType>\n')
            XML_WEP.write('\t\t\t\t<protected>false</protected>\n')
            XML_WEP.write('\t\t\t\t<keyMaterial>')
            XML_WEP.write(PASS)
            XML_WEP.write('</keyMaterial>\n')
            XML_WEP.write('\t\t\t</sharedKey>\n')
            XML_WEP.write('\t\t</security>\n')
            XML_WEP.write('\t</MSM>\n')
            XML_WEP.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_WEP.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_WEP.write('\t</MacRandomization>\n')
            XML_WEP.write('</WLANProfile>')
        XML_WEP.close() #CIERRA EL ARCHIVO XML

        with open(Perfil_WPA, "w") as XML_WPA:
            XML_WPA.write('<?xml version="1.0"?>\n')
            XML_WPA.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_WPA.write('\t<name>')
            XML_WPA.write(SSID)
            XML_WPA.write('</name>\n')
            XML_WPA.write('\t<SSIDConfig>\n')
            XML_WPA.write('\t\t<SSID>\n')
            XML_WPA.write('\t\t\t<name>')
            XML_WPA.write(SSID)
            XML_WPA.write('</name>\n')
            XML_WPA.write('\t\t</SSID>\n')
            XML_WPA.write('\t</SSIDConfig>\n')
            XML_WPA.write('\t<connectionType>ESS</connectionType>\n')
            XML_WPA.write('\t<connectionMode>auto</connectionMode>\n')
            XML_WPA.write('\t<MSM>\n')
            XML_WPA.write('\t\t<security>\n')
            XML_WPA.write('\t\t\t<authEncryption>\n')
            XML_WPA.write('\t\t\t\t<authentication>WPAPSK</authentication>\n')
            XML_WPA.write('\t\t\t\t<encryption>AES</encryption>\n')
            XML_WPA.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_WPA.write('\t\t\t</authEncryption>\n')
            XML_WPA.write('\t\t\t<sharedKey>\n')
            XML_WPA.write('\t\t\t\t<keyType>passPhrase</keyType>\n')
            XML_WPA.write('\t\t\t\t<protected>false</protected>\n')
            XML_WPA.write('\t\t\t\t<keyMaterial>')
            XML_WPA.write(PASS)
            XML_WPA.write('</keyMaterial>\n')
            XML_WPA.write('\t\t\t</sharedKey>\n')
            XML_WPA.write('\t\t</security>\n')
            XML_WPA.write('\t</MSM>\n')
            XML_WPA.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_WPA.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_WPA.write('\t</MacRandomization>\n')
            XML_WPA.write('</WLANProfile>')
        XML_WPA.close()

        with open(Perfil_WPA2, "w") as XML_WPA2:
            XML_WPA2.write('<?xml version="1.0"?>\n')
            XML_WPA2.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_WPA2.write('\t<name>')
            XML_WPA2.write(SSID)
            XML_WPA2.write('</name>\n')
            XML_WPA2.write('\t<SSIDConfig>\n')
            XML_WPA2.write('\t\t<SSID>\n')
            XML_WPA2.write('\t\t\t<name>')
            XML_WPA2.write(SSID)
            XML_WPA2.write('</name>\n')
            XML_WPA2.write('\t\t</SSID>\n')
            XML_WPA2.write('\t</SSIDConfig>\n')
            XML_WPA2.write('\t<connectionType>ESS</connectionType>\n')
            XML_WPA2.write('\t<connectionMode>auto</connectionMode>\n')
            XML_WPA2.write('\t<MSM>\n')
            XML_WPA2.write('\t\t<security>\n')
            XML_WPA2.write('\t\t\t<authEncryption>\n')
            XML_WPA2.write('\t\t\t\t<authentication>WPA2PSK</authentication>\n')
            XML_WPA2.write('\t\t\t\t<encryption>AES</encryption>\n')
            XML_WPA2.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_WPA2.write('\t\t\t</authEncryption>\n')
            XML_WPA2.write('\t\t\t<sharedKey>\n')
            XML_WPA2.write('\t\t\t\t<keyType>passPhrase</keyType>\n')
            XML_WPA2.write('\t\t\t\t<protected>false</protected>\n')
            XML_WPA2.write('\t\t\t\t<keyMaterial>')
            XML_WPA2.write(PASS)
            XML_WPA2.write('</keyMaterial>\n')
            XML_WPA2.write('\t\t\t</sharedKey>\n')
            XML_WPA2.write('\t\t</security>\n')
            XML_WPA2.write('\t</MSM>\n')
            XML_WPA2.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_WPA2.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_WPA2.write('\t</MacRandomization>\n')
            XML_WPA2.write('</WLANProfile>')
        XML_WPA2.close()
    else:
        with open(log, "w") as log_txt:
            log_txt.write('Error en la rama comparativa: No se encuentra Archivo TXT')
        log_txt.close()
        print("FIN DEL PROGRAMA")
        sys.exit()
else:
    if os.path.exists(RedActual): #PREGUNTA SI EXISTE ARCHIVO TXT Y REALIZA LO SIGUIENTE
        with open(RedActual, "r") as ArchivoTXT: #ABRE EL ARCHIVO TXT COMO LECTURA
            SSID = ArchivoTXT.readline()
            PASS = ArchivoTXT.readline()
        ArchivoTXT.close()
        
        with open(Perfil_UNK, "w") as XML_UNK: #EMPIEZA A CREAR EL ARCHIVO XML
            XML_UNK.write('<?xml version="1.0"?>\n') 
            XML_UNK.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_UNK.write('\t<name>')
            XML_UNK.write(SSID)
            XML_UNK.write('</name>\n')
            XML_UNK.write('\t<SSIDConfig>\n')
            XML_UNK.write('\t\t<SSID>\n')
            XML_UNK.write('\t\t\t<name>')
            XML_UNK.write(SSID)
            XML_UNK.write('</name>\n')
            XML_UNK.write('\t\t</SSID>\n')
            XML_UNK.write('\t</SSIDConfig>\n')
            XML_UNK.write('\t<connectionType>ESS</connectionType>\n')
            XML_UNK.write('\t<connectionMode>auto</connectionMode>\n')
            XML_UNK.write('\t<MSM>\n')
            XML_UNK.write('\t\t<security>\n')
            XML_UNK.write('\t\t\t<authEncryption>\n')
            XML_UNK.write('\t\t\t\t<authentication>open</authentication>\n')
            XML_UNK.write('\t\t\t\t<encryption>none</encryption>\n')
            XML_UNK.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_UNK.write('\t\t\t</authEncryption>\n')
            XML_UNK.write('\t\t\t</security>\n')
            XML_UNK.write('\t</MSM>\n')
            XML_UNK.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_UNK.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_UNK.write('\t</MacRandomization>\n')
            XML_UNK.write('</WLANProfile>')
        XML_UNK.close() #CIERRA EL ARCHIVO XML
        
        with open(Perfil_WEP, "w") as XML_WEP: #EMPIEZA A CREAR EL ARCHIVO XML
            XML_WEP.write('<?xml version="1.0"?>\n')
            XML_WEP.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_WEP.write('\t<name>')
            XML_WEP.write(SSID)
            XML_WEP.write('</name>\n')
            XML_WEP.write('\t<SSIDConfig>\n')
            XML_WEP.write('\t\t<SSID>\n')
            XML_WEP.write('\t\t\t<name>')
            XML_WEP.write(SSID)
            XML_WEP.write('</name>\n')
            XML_WEP.write('\t\t</SSID>\n')
            XML_WEP.write('\t</SSIDConfig>\n')
            XML_WEP.write('\t<connectionType>ESS</connectionType>\n')
            XML_WEP.write('\t<connectionMode>auto</connectionMode>\n')
            XML_WEP.write('\t<MSM>\n')
            XML_WEP.write('\t\t<security>\n')
            XML_WEP.write('\t\t\t<authEncryption>\n')
            XML_WEP.write('\t\t\t\t<authentication>open</authentication>\n')
            XML_WEP.write('\t\t\t\t<encryption>WEP</encryption>\n')
            XML_WEP.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_WEP.write('\t\t\t</authEncryption>\n')
            XML_WEP.write('\t\t\t<sharedKey>\n')
            XML_WEP.write('\t\t\t\t<keyType>networkKey</keyType>\n')
            XML_WEP.write('\t\t\t\t<protected>false</protected>\n')
            XML_WEP.write('\t\t\t\t<keyMaterial>')
            XML_WEP.write(PASS)
            XML_WEP.write('</keyMaterial>\n')
            XML_WEP.write('\t\t\t</sharedKey>\n')
            XML_WEP.write('\t\t</security>\n')
            XML_WEP.write('\t</MSM>\n')
            XML_WEP.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_WEP.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_WEP.write('\t</MacRandomization>\n')
            XML_WEP.write('</WLANProfile>')
        XML_WEP.close() #CIERRA EL ARCHIVO XML

        with open(Perfil_WPA, "w") as XML_WPA:
            XML_WPA.write('<?xml version="1.0"?>\n')
            XML_WPA.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_WPA.write('\t<name>')
            XML_WPA.write(SSID)
            XML_WPA.write('</name>\n')
            XML_WPA.write('\t<SSIDConfig>\n')
            XML_WPA.write('\t\t<SSID>\n')
            XML_WPA.write('\t\t\t<name>')
            XML_WPA.write(SSID)
            XML_WPA.write('</name>\n')
            XML_WPA.write('\t\t</SSID>\n')
            XML_WPA.write('\t</SSIDConfig>\n')
            XML_WPA.write('\t<connectionType>ESS</connectionType>\n')
            XML_WPA.write('\t<connectionMode>auto</connectionMode>\n')
            XML_WPA.write('\t<MSM>\n')
            XML_WPA.write('\t\t<security>\n')
            XML_WPA.write('\t\t\t<authEncryption>\n')
            XML_WPA.write('\t\t\t\t<authentication>WPAPSK</authentication>\n')
            XML_WPA.write('\t\t\t\t<encryption>AES</encryption>\n')
            XML_WPA.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_WPA.write('\t\t\t</authEncryption>\n')
            XML_WPA.write('\t\t\t<sharedKey>\n')
            XML_WPA.write('\t\t\t\t<keyType>passPhrase</keyType>\n')
            XML_WPA.write('\t\t\t\t<protected>false</protected>\n')
            XML_WPA.write('\t\t\t\t<keyMaterial>')
            XML_WPA.write(PASS)
            XML_WPA.write('</keyMaterial>\n')
            XML_WPA.write('\t\t\t</sharedKey>\n')
            XML_WPA.write('\t\t</security>\n')
            XML_WPA.write('\t</MSM>\n')
            XML_WPA.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_WPA.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_WPA.write('\t</MacRandomization>\n')
            XML_WPA.write('</WLANProfile>')
        XML_WPA.close()

        with open(Perfil_WPA2, "w") as XML_WPA2:
            XML_WPA2.write('<?xml version="1.0"?>\n')
            XML_WPA2.write('<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n')
            XML_WPA2.write('\t<name>')
            XML_WPA2.write(SSID)
            XML_WPA2.write('</name>\n')
            XML_WPA2.write('\t<SSIDConfig>\n')
            XML_WPA2.write('\t\t<SSID>\n')
            XML_WPA2.write('\t\t\t<name>')
            XML_WPA2.write(SSID)
            XML_WPA2.write('</name>\n')
            XML_WPA2.write('\t\t</SSID>\n')
            XML_WPA2.write('\t</SSIDConfig>\n')
            XML_WPA2.write('\t<connectionType>ESS</connectionType>\n')
            XML_WPA2.write('\t<connectionMode>auto</connectionMode>\n')
            XML_WPA2.write('\t<MSM>\n')
            XML_WPA2.write('\t\t<security>\n')
            XML_WPA2.write('\t\t\t<authEncryption>\n')
            XML_WPA2.write('\t\t\t\t<authentication>WPA2PSK</authentication>\n')
            XML_WPA2.write('\t\t\t\t<encryption>AES</encryption>\n')
            XML_WPA2.write('\t\t\t\t<useOneX>false</useOneX>\n')
            XML_WPA2.write('\t\t\t</authEncryption>\n')
            XML_WPA2.write('\t\t\t<sharedKey>\n')
            XML_WPA2.write('\t\t\t\t<keyType>passPhrase</keyType>\n')
            XML_WPA2.write('\t\t\t\t<protected>false</protected>\n')
            XML_WPA2.write('\t\t\t\t<keyMaterial>')
            XML_WPA2.write(PASS)
            XML_WPA2.write('</keyMaterial>\n')
            XML_WPA2.write('\t\t\t</sharedKey>\n')
            XML_WPA2.write('\t\t</security>\n')
            XML_WPA2.write('\t</MSM>\n')
            XML_WPA2.write('\t<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n')
            XML_WPA2.write('\t\t<enableRandomization>false</enableRandomization>\n')
            XML_WPA2.write('\t</MacRandomization>\n')
            XML_WPA2.write('</WLANProfile>')
        XML_WPA2.close()
    else:
        with open(log, "w") as log_txt:
            log_txt.write('Error en la rama directa: No se encuentra Archivo TXT')
        log_txt.close()
        print("FIN DEL PROGRAMA")
        sys.exit()