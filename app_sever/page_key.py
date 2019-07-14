import requests
import base64,os
from cutword import cut
from find_rub import find_rub

api_key='Ars3r1gZhRb5G8tbC3BasTFS'
api_secret='s5mofk0UGGkqMYK3aC60RXds2tsYpm29'
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

def get_word(img_name):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url="https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token={}".format(access_token)
    image_base64=base64_encode(img_name)
    data={'image':image_base64}
    result=requests.post(url,headers=headers,data=data).json()
    return result

def page_key(thing):
    info=get_word(thing)
    long=info['words_result_num']
    words=""
    list=[]
    list2=[]
    for i in range(long):
        word=info['words_result'][i]['words']
        list.append(word)
        words=words+word
    #print(list)
    word_cutted=cut(words)
    #print(word_cutted)

    long1=len(list)
    long2=len(word_cutted)

    for o in range(long2):
        sen1=word_cutted[o]
        for p in range(long1):
            sen2=list[p]
            if sen1 in sen2 :
                fr=find_rub(sen1)
                if fr == None:
                    pass
                else:
                    msg=sen2+'中的'+sen1+'是'+fr
                    list2.append(msg)

    return(list2)

#print(page_key('timg.jpeg'))

