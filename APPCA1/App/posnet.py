import socket
import time
import json
from time import sleep
Host=''
Port=0
def client_program(data):
    try:
        host = Host  # as both code is running on same pc
        port = Port  # socket server port number
        
        client_socket = socket.socket()  # instantiate
        client_socket.settimeout(2)
        client_socket.connect((host, port))  # connect to the server
        client_socket.settimeout(60)

        

        
        client_socket.send(data.encode())  # send message
        data = client_socket.recv(16000).decode()  # receive response

        client_socket.close()  # close the connection

        if data:
            return data
        else:
            return 'Error'
    except:
        return 'Error'

    

    
#Command.Format("{\"Funcion\" : \"Config\", \"Datos\":{\"MerchantId\": \"%s\", \"TerminalId\": \"%s\"} }",m_MerchantId,m_TerminalId);
#Command.Format("{\"Funcion\":\"Inicializar\"}");
#Command.Format("{\"Funcion\":\"Status\"}");
#Command.Format("{\"Funcion\":\"Cerrar\"}");
#Command.Format("{\"Funcion\": \"Cobro\",   \"Datos\":{\"Ticket No\": \"%s\",\"Importe\": %0.2f,\"Impuesto\": %0.2f,\"Moneda\": \"usd\"} }",m_TicketId,m_ImporteTotal,m_Impuestos);
    
def Posnet_Status():
    data='{"Funcion":"Status"}'
    r=client_program(data)
    return r
def Posnet_Init(h,p):
    global Host
    global Port
    Host=h
    Port=p
    data='{"Funcion":"Inicializar"}'
    r=client_program(data)
    return r
def Posnet_Close():
    data='{"Funcion":"Cerrar"}'
    r=client_program(data)
    return r
def Posnet_Config():
    data='{"Funcion":"Config","Datos":{"MerchantId": "MAGNEQUIL0GP", "TerminalId":"00000001"}}'
    r=client_program(data)
    return r
def Posnet_Pay(importe,tax):
    ts=time.time()
    ts=str(ts)[:8]
    data='{"Funcion": "Cobro","Datos":{"Ticket No": "'+ ts +'","Importe":'+str(importe)+',"Impuesto":'+str(tax)+',"Moneda":"usd"}}'
    r=client_program(data)
    return r


Host='10.0.0.5'
Port=11000
#r=Posnet_Pay(20,1)
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

if r['Resultado']['Cod']==15:
    r=Posnet_Config()
    print(r) """

#r=Posnet_Pay(20,1)
#r=json.loads(r)
#print(r)



#now = str(time.ctime((time.time()+40000000000)))
#print("the now time is " + str(now))