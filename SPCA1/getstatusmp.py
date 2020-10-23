def GetStatusMP(product,token):
    try:
        if producto!='':
                envia='external_reference='+str(producto)+'&status=approved&access_token='+str(token)
            else:
                envia='status=approved&access_token='+str(token)
            url = 'https://api.mercadopago.com/v1/payments/search?'+envia+'&limit=1&criteria=desc'    
            r=requests.get(url)
            data2=json.loads(str(r.text))
            return(data2)
    except:
        return('error')
