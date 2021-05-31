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
                sql=("insert into TBL_History_Event (tipo,time_stamp) values('%s','%s')")%(v['tipo'],v['timestamp'])
                c.execute(sql)
                conn.commit()
                lrow=c.lastrowid
                c.close()
                conn.close()
                
                if ttype=='device':
                    data=json.loads(data)
                    data['Id_History_Event']=str(lrow)
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
        conn=sqlite3.connect(dbpath+'Autocashier.db')
    except Exception as e:
        print(e)
        return False
    finally:
        if conn:
            try:
                c=conn.cursor()
                v=event
                sql=("insert into TBL_Money_In_Device (ID_History_Event,Device,Channel_Device,Currency,Total_amount_local_currency) values('%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Device'],v['Channel'],v['Currency'],v['Total_amount_local_currency'])
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                return True
            except Exception as e:
                print(e)
                return False

def saveMoneyInProcess(event):
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
                v=event
                sql=("insert into TBL_Money_In_Process (ID_History_Event,Process,Pay_Method,Card,Card_Number,Total_amount_local_currency) values('%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Process'],v['Pay_Methods'],v['Currency'],v['Total_amount_local_currency'])
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                return True
            except Exception as e:
                print(e)
                return False

def saveSpecialOperation(event):
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
                v=event
                sql=("insert into TBL_Money_In_Device (ID_History_Event,Device,Channel_Device,Currency,Total_amount_local_currency) values('%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Device'],v['Channel'],v['Currency'],v['Total_amount_local_currency'])
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                return True
            except Exception as e:
                print(e)
                return False

def saveCloseTransaction(event):
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
                v=event
                sql=("insert into TBL_Money_In_Device (ID_History_Event,Device,Channel_Device,Currency,Total_amount_local_currency) values('%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Device'],v['Channel'],v['Currency'],v['Total_amount_local_currency'])
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                return True
            except Exception as e:
                print(e)
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
#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_local_currency":"2.0"}'
#process
eventProcess='{"Process":"Datacap","Pay_Method":"Debit","Card":"Visa","Card_Number":"1234","Total_amount_Local_Currency":10}'
#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
saveHistoryEvent(event,eventProcess,'process')
