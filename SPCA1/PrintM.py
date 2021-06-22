import os
import json
from time import sleep


enviar="""{"titulo":"MAGNETIC CASH",
"encabezado":"CajeroATM",
"direccion":"San Mauro Castelverde 2559",
"ciudad":"Quilmes",
"Provincia":"Buenos Aires",
"Pais":"Argentina",
"phone":"11-4160-7948",
"email":"lab@magneticash.com",
"web":"www.magneticash.com",
"cashier":"Matias",
"date":"03/06/2021 15:45",
"mpl":"3650011783889",
"symbol":"USD",
"card_price":2.00,
"load":30.00,
"subtotal":32.00,
"iva":21.00,
"iva_monto":6.72,
"total":38.72,
"pie":"thank you!!!"
}"""

parametros=[]

def Print():#pcard,amount,cashier,mpl,symbol,tax
    global enviar
    global parametros

    os.chdir('/home/pi/Autocashier/PrinterTicket')
    
    while 1:
        try:
            sleep(1)
            if len(parametros)>=6:
                r=json.loads(enviar)

                r['cashier']=parametros[2]
                r['load']=(parametros[1] - parametros[0])-((parametros[1]*parametros[5])/100)
                r['card_price']=parametros[0]
                r['subtotal']=r['load'] + parametros[0]
                r['iva_monto']=(parametros[1]*parametros[5]/100)
                r['total']=r['subtotal']+r['iva_monto']
                r['mpl']=parametros[3]
                r['symbol']=parametros[4]
                parametros=[]
                print(r)
                f = open("Parameters.txt", "w")
                for key,value in r.items():
                    f.write(str(value)+'\n')
                f.close()
                os.system("sudo ./Print")
        except:
            continue










