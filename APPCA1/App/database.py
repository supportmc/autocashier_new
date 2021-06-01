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
                    data=json.loads(data)
                    data['Id_History_Event']=str(lrow)
                    saveMoneyInProcess(data)
                if ttype=='special':
                    data=json.loads(data)
                    data['Id_History_Event']=str(lrow)
                    saveSpecialOperation(data)
                if ttype=='close':
                    data=json.loads(data)
                    data['Id_History_Event']=str(lrow)
                    saveCloseTransaction(data)
                if ttype=='collect':
                    data=json.loads(data)
                    data['Id_History_Event']=str(lrow)
                    saveCollect(data)



                
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
                sql=("insert into TBL_Money_In_Process (ID_History_Event,Process,Pay_Method,Card,Card_Number,Total_amount_local_currency) values('%s','%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Process'],v['Pay_Method'],v['Card'],v['Card_Number'],v['Total_amount_local_currency'])
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
                sql=("insert into TBL_Special_Operations (ID_History_Event,App_Version_Name,App_Version_Number,Event,Loc_Currency_Type) values('%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['App_Version_Name'],v['App_Version_Number'],v['Event'],v['Loc_Currency_Type'])
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
                sql=("insert into TBL_Close_Transaction (ID_History_Event,Reader,MPL,MPL_Number,System,Total_amount_local_currency) values('%s','%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Reader'],v['MPL'],v['MPL_Number'],v['System'],v['Total_amount_local_currency'])
                c.execute(sql)
                conn.commit()
                c.close()
                conn.close()
                return True
            except Exception as e:
                print(e)
                return False
            #resuelvo

def saveCollect(event):
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
                sql=("insert into TBL_Collect (ID_History_Event,Bill1_Local_Currency,Bill2_Local_Currency,Coin_Local_Currency,ProcessCollect_Local_Currency,Details,Total_Collect_Local_Currency) values('%s','%s','%s','%s','%s','%s','%s')")%(v['Id_History_Event'],v['Bill1_Local_Currency'],v['Bill2_Local_Currency'],v['Coin_Local_Currency'],v['ProcessCollect_Local_Currency'],v['Details'],v['Total_Collect_Local_Currency'])
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
#Device
#Process
#Collect
#Close






""" #Special
event='{"tipo":"Special","timestamp":"'+str(datetime.now())+'"}'
eventSpecial='{"App_Version_Name":"*-*","App_Version_Number":"1.0","Event":"Open_App","Loc_Currency_Type":"Pesos"}'#eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_Local_Currency":"2.0"}'
saveHistoryEvent(event,eventSpecial,'special')

#device example
event='{"tipo":"Device","timestamp":"'+str(datetime.now())+'"}'
eventDevice='{"Device":"bill1","Channel":"ch80","Currency":"2.0","Total_amount_local_currency":"2.0"}'
saveHistoryEvent(event,eventDevice,'device')

#process
event='{"tipo":"Process","timestamp":"'+str(datetime.now())+'"}'
eventProcess='{"Process":"Datacap","Pay_Method":"Debit","Card":"Visa","Card_Number":"1234","Total_amount_local_currency":10}'
saveHistoryEvent(event,eventProcess,'process')


#Close_Transaction
event='{"tipo":"Close","timestamp":"'+str(datetime.now())+'"}'
eventClose='{"Reader":"Datacap","MPL":"mpl","MPL_Number":"1234567890123","System":"Autocashier","Total_amount_local_currency":10}'
saveHistoryEvent(event,eventClose,'close')

#Collect_Transaction
event='{"tipo":"Collect","timestamp":"'+str(datetime.now())+'"}'
eventCollect='{"Bill1_Local_Currency":"5.0","Bill2_Local_Currency":"5.0","Coin_Local_Currency":"5.0","ProcessCollect_Local_Currency":"0.0","Details":"-","Total_Collect_Local_Currency":15.0}'
saveHistoryEvent(event,eventCollect,'collect')

print("fin") """
