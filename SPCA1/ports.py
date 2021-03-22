import serial.tools.list_ports as port

def GetPort(ptype):
    portlist = list(port.comports())
    for p in portlist:
        print(p.product)
        #if ptype=='Board':
        #    if str(p.product).find('FT232R')>-1:# USB UART':
        #        return (p.device)
        #if ptype=='Dispenser':
        #    if str(p.product).find('USB2.0')>-1:
        #        return (p.device)
    
    return(None)


