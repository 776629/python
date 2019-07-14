
import requests
import base64,os

api_key= '2zph3UZGTXj1t8v1IBWpLyXt'
api_secret= 'ryAsQEuRDxyt9epnDbtPkmDjieth5WPs'

def api_to_access_token(api_key,api_secret):
    url='https://aip.baidubce.com/oauth/2.0/token'
    data={'grant_type':'client_credentials','client_id':api_key,'client_secret':api_secret}
    access_token=requests.post(url,data=data).json()['access_token']
    return access_token

access_token=api_to_access_token(api_key,api_secret)

def base64_encode(image_name):
    opener = open(image_name, 'rb')
    changer = base64.b64encode(opener.read())
    opener.close()
    image_base6_4 = changer
    return image_base6_4

def get_key(img_name):  
    url='https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token={}'.format(access_token)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    image_base64=base64_encode(img_name)
    data={'image':image_base64}
    try:
        result=requests.post(url,headers=headers,data=data).json()
        b = len(result['result'])
        key = ''
        list=[]
        for i in range(b):
            c = result['result'][i]['keyword']
            list.append(c)
        #print(key)
        return list
    except:
        pass

#print(get_key('obj/0.7719430696144804.jpg')[0])
