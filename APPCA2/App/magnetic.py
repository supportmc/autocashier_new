import socket
import time
import json
from time import sleep
from datetime import datetime
Host=''
Port=0

date_open=''
terminal=''
card_price=0

def client_program(data):
    try:
        host = Host  # as both code is running on same pc
        port = Port  # socket server port number
        
        client_socket = socket.socket()  # instantiate
        client_socket.settimeout(2)
        client_socket.connect((host, port))  # connect to the server
        client_socket.settimeout(3)

        

        
        client_socket.send(data.encode())  # send message
        data = client_socket.recv(16000).decode()  # receive response

        client_socket.close()  # close the connection

        if data:
            return data
        else:
            return '{"status":"Error","msg":"error"}'
    except Exception as e:
        return '{"status":"Error","msg":"'+str(e)+'"}'

    

    

    

def opencash(name,device):
    global Host
    global Port
    global date_open
    global card_price
    #Host=h
    #Port=p
    data='{"transaction_type": "opencash","cashier_name": "'+str(name)+'","cashier_id": 0,"device_name": "'+str(device)+'","datetime_device": datetime.now()}'
    r=client_program(data)
    rr=json.loads(r)    
    if rr['status']=='ok':
        date_open=rr['dateopen']
        card_price=rr['card_price']

    return r

def balance(mpl):
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"transaction_type": "balance","mpl": "'+str(mpl)+'"}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r

def movements(mpl):
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"transaction_type": "movements","mpl": "'+str(mpl)+'"}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r

def Charge(mpl,vmpl,amount,name,device,cp,oc):
    #ts=time.time()
    #ts=str(ts)[:8]
    data='{"opencash":"'+str(oc)+'","transaction_type": "charge","mpl": "'+str(mpl)+'","vmpl": "'+str(vmpl)+'","msj": "","transaction_id": "0123456786","charge": [{"balance_type": "Pesos","amount": '+str(amount)+',"cashier_name": "'+str(name)+'","cashier_id": 0,"device_name": "'+str(device)+'","datetime_device":"'+ str(datetime.now())+'","payments": [{"currency": "Pesos","payment_method": "efectivo","Amount": '+str(amount)+',"rate": 1.0 }],"total_payment_local_currency": '+str(amount)+',"promotions": []}],"card_price":'+str(cp) + '}'
    data=json.dumps(data)
    data=json.loads(data)
    r=client_program(str(data))
    return r


Host='192.168.1.158'#158
Port=4000#r=Charge(';9999999999999','',15.50,'CajeroEze','Autocashier',1.0,'10/08/21 12:05:08')
#r=Posnet_Init(Host,Port)
#r=Posnet_Config()
#print(r)
""" while 1:
    r=Posnet_Status()
    r=json.loads(r)
    r=r['Resultado']['Status']
    if r!='Ocupado':
        break
    sleep(1)
#r=Posnet_Config()
#print(r)
r=Posnet_Pay(20,1)
r=json.loads(r)
Charge(';9999999999999','',15.50,'CajeroEze','Autocashier',1.0,'10/08/21 12:05:08')esultado']['Cod']==15:
    r=Posnet_Config()
    print(r) """

#r=Posnet_Pay(20,1)
#r=json.loads(r)
#print(r)



#now = str(time.ctime((time.time()+40000000000)))
#print("t,"opencash":"'+str(oc)+'"he now time is " + str(now))
#r=Charge(';9999999999999','',15.50,'CajeroEze','Autocashier',1.0,'10/08/21 12:05:08')
#r=balance(';6230012703787')
#print(r)
#sleep(1)