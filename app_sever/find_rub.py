import requests
import re


def find_rub(thing):
    headers={'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    url1='https://lajifenleiapp.com/sk/{}'.format(thing)
    try:
        res=requests.get(url1,headers=headers, timeout=3)
        text=res.text
        #print(text)
        result=re.findall(r'属于&nbsp;</span><span style="color:#.*?">(.*?)</span></h1></div>',text)[0]
        #print(result)
    except:
        result=''
        #print('error')

    if '可回收物'  in result or '有害垃圾' in result or '湿垃圾'  in result or '干垃圾'  in result:
        if '可回收物'  in  result:
            form='可回收物'
            return  form
        if '有害垃圾'  in  result:
            form='有害垃圾'
            return  form
        if '湿垃圾'  in  result:
            form='湿垃圾'
            return  form
        if '干垃圾'  in  result:
            form='干垃圾'
            return  form

    url3='https://www.metalgearjoe.cn/mn/search?search={}'.format(thing)
    try:
        res3=requests.get(url3,headers=headers, timeout=3)
        text3=res3.text
        #print(text3)
        result3=re.findall(r'<div class="result result-cat-.*?">.*?&nbsp;(.*?)</div>',text3)
        name=re.findall(r'<div class="result result-cat-.*?">(.*?)&nbsp;.*?</div>',text3)[0]
        #print(name)
        #print(result3)
    except:
        #print('error')
        return None
    
    word3=str(result3)
    long4=len(result3)
    ke=0
    hai=0
    shi=0
    gan=0
    mx='v'
    mxn=0
    if '可回收物'  in word3 or '有害垃圾' in word3 or '湿垃圾'  in word3 or '干垃圾'  in word3:
        key_main=result3[0]
        if name == thing:
            #print('1')
            x=re.findall(r'\[(.*?)\]',key_main)[0]
            return x

        for q in range (long4):
            key_nor=result3[q]
            if '可回收物'  in  key_nor:
                ke=ke+1
            if '有害垃圾'  in  key_nor:
                hai=hai+1
            if '湿垃圾'  in  key_nor:
                shi=shi+1
            if '干垃圾'  in  key_nor:
                gan=gan+1

        if hai>ke and hai>gan and hai>shi:
            mx='有害垃圾'
            mxn=hai
        if shi>ke and shi>gan and shi>hai:
            mx='湿垃圾'
            mxn=shi
        if gan>ke and gan>hai and gan>shi:
            mx='干垃圾'
            mxn=gan
        if ke>hai and ke>gan and ke>shi:
            mx='可回收物'
            mxn=ke

        #print(ke,hai,shi,gan,mx,mxn,key_main)
        if mx in key_main:
            #print (mx)
            return mx
        if  mxn / long4 >= 0.9:
            #print (mx)
            return mx
        if '可回收物'  in  key_main:
            form='可回收物'
            return  form
        if '有害垃圾'  in  key_main:
            form='有害垃圾'
            return  form
        if '湿垃圾'  in  key_main:
            form='湿垃圾'
            return  form
        if '干垃圾'  in  key_main:
            form='干垃圾'
            return  form
    else:
        return False

#print(find_rub(''))