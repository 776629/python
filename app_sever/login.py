import hashlib
from  login_db import db_read,db_join,db_delete

def hash(data):
    result = hashlib.md5(data.encode('utf-8'))
    return result.hexdigest()

def login(input_username,input_password):
    a=db_read('data','username')
    b=db_read('data','password')
    long=len(a)
    for i in range(long):
        c=str(a[i][0])
        #print(c) #检修口
        if c==input_username:
            real_password_hash=b[i][0]
            if str(hash(input_password))==str(real_password_hash):
                print('登陆成功，欢迎您'+input_username)
                return True
            else:
                print('密码错误')
                return False
        else:
            pass
    print('尚未注册')
    return False

def singup(username,password):
    a=db_read('data','username')
    long=len(a)
    for i in range(long):
        b=a[i][0]
        if str(username)==str(b):
            print('用户名重复')
            return False
    db_join(username, password)
    print('注册成功')
    return True

#login('裘成1','裘')
#db_delete('data')
#singup('裘成1','裘')
