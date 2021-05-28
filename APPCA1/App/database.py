import sqlite3
from datetime import datetime
import json

dbpath='/home/pi/Autocashier/Database/'

def saveHistoryEvent(event,data,ttype):
    try:
        conn=None
        conn=sqlite3.connect(dbpath+'Autocashier.db')
    except Exception as e:
        print(e)
        return False
    finally:
        if conn:
            try:
                c=conn.cursor()
                v=json.loads(event)
                sql='insert'
                c.execute(event)
                conn.comit()
                lrow=c.lastrowid
                c.close()
                conn.close()
                
                if ttype=='device':
                    data=json.loads(data)
                    data['id']
                    saveMoneyInDevice(data)
                if ttype=='process':
                    saveMoneyInProcess(data)
                if ttype=='special':
                    saveSpecialOperation(data)
                if ttype=='close':
                    saveCloseTransaction(data)



                
                return True
            except Exception as e:
                print(e)
                return False


def saveMoneyInDevice(event):
    try:
        conn=None
        conn=sqlite3.connect(dbpath)
    except Exception as e:
        print(e)
        return False
    finally:
        if conn:
            try:
                c=conn.cursor()
                c.execute(event)
                conn.comit()
                c.close()
                conn.close()
                return True
            except:
                return False

def saveMoneyInProcess(event):
    try:
        conn=None
        conn=sqlite3.connect(dbpath)
    except Exception as e:
        print(e)
        return False
    finally:
        if conn:
            try:
                c=conn.cursor()
                c.execute(event)
                conn.comit()
                c.close()
                conn.close()
                return True
            except:
                return False

def saveSpecialOperation(event):
    try:
        conn=None
        conn=sqlite3.connect(dbpath)
    except Exception as e:
        print(e)
        return False
    finally:
        if conn:
            try:
                c=conn.cursor()
                c.execute(event)
                conn.comit()
                c.close()
                conn.close()
                return True
            except:
                return False

def saveCloseTransaction(event):
    try:
        conn=None
        conn=sqlite3.connect(dbpath)
    except Exception as e:
        print(e)
        return False
    finally:
        if conn:
            try:
                c=conn.cursor()
                c.execute(event)
                conn.comit()
                c.close()
                conn.close()
                return True
            except:
                return False
            #resuelvo

#events:
#Start
#Button
#Reader
#Money
#Postnet
#NewCard


event='{"tipo":"Money","timestamp":"'+str(datetime.now())+'"}'
#device example
eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
#process
#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
saveHistoryEvent(event,eventDevice,'device')
