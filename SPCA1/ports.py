import serial.tools.list_ports as port

def GetPort(ptype):
    portlist = list(port.comports())
    print(portlist)
    for p in portlist:
        print(p.product)
        if ptype=='Board':
            if str(p.product).find('FT232R')>-1:# USB UART':
                return (p.device)
        if ptype=='Dispenser':
            if str(p.product).find('USB-Serial Controller D')>-1:#USB2.0
                return (p.device)
        if ptype=='QRR':
            if str(p.product).find('USB-Serial Controller D')>-1:
                return (p.device)

    
    return(None)

def GetSpecialPort(ptype,anterior):
    portlist = list(port.comports())
    print(portlist)
    for p in portlist:
        print(p.product)
        if ptype=='Board':
            if str(p.product).find('FT232R')>-1:# USB UART':
                return (p.device)
        if ptype=='Dispenser':
            if str(p.product).find('USB-Serial Controller D')>-1:#USB2.0
                if p.device not in anterior:
                    return (p.device)
        if ptype=='QRR':
            if str(p.product).find('USB-Serial Controller D')>-1:
                return (p.device)

    
    return(None)


#GetPort('1')