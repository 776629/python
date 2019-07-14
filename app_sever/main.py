
from flask import Flask,render_template,request,session,url_for
import sqlite3,os,random
from find_rub import  find_rub
from img_key import get_key
from page_key import page_key
from login import login,singup
from db import new_table,db_join,DB_read


#主网站
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)



@app.route('/', methods=['GET', 'POST'])
@app.route('/back', methods=['GET', 'POST'])
@app.route('/search', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/grade', methods=['GET', 'POST'])
def grade():
  posts= []
  if 'username' in session: 
    uid=session.get('username')
    info=DB_read('data.db',uid,'msg')
    lens=len(info)
    for i in range(lens):
      inf=info[i][0]
        #print(inf
      posts.append({'msg':inf})
  return render_template('grade.html',posts=posts)

@app.route('/memory', methods=['GET', 'POST'])
def memory():
    return render_template('memory.html')


@app.route('/account', methods=['GET', 'POST'])
def account():
    if 'username' in session: 
      uid=session.get('username')
      print(uid)
      return render_template('account_logined.html',posts=uid)
    else:
      return render_template('account.html')

@app.route('/ser_text', methods=['POST'])
def ser_text():
    ser_text = request.form.get('ser_text')
    #print(ser_text)
    msg=str(ser_text)+'是'+str(find_rub(ser_text))
    #print(msg)
    if 'username' in session: 
      uid=session.get('username')
      db_join(uid,msg)
    return render_template('return.html',post_msg=msg)

@app.route('/obj_photo', methods=['post'])
def obj_photo():
  key=''
  img = request.files.get('obj_photo')
  name=str(random.random())
  img.save('obj/{}.jpg'.format(name))
  key=get_key('obj/{}.jpg'.format(name))[0]
  msg=key+'是'+str(find_rub(key))
  if 'username' in session: 
      uid=session.get('username')
      db_join(uid,msg)
  return render_template('return.html',post_msg=msg)

@app.route('/page_photo', methods=['post'])
def page_photo():
  img = request.files.get('page_photo')
  name=str(random.random())
  img.save('page/{}.jpg'.format(name))
  list=page_key('page/{}.jpg'.format(name))
  long=len(list)
  msg=''
  for i in range(long):
    wor=list[i]
    if 'username' in session: 
      uid=session.get('username')
      try:
        db_join(uid,msg)
      except:
        pass
    msg=msg+wor+'，'
  return render_template('return.html',post_msg=msg)

@app.route('/login', methods=[ 'POST'])
def login1():
    uid=request.form.get('username')
    psw=request.form.get('password')
    #print(uid,psw)
    if login(uid,psw) == True:
      username=request.values.get('username') 
      session['username']=username 
      #print('ok')
      return render_template('account_logined.html',posts=uid)
    else:
       return render_template('account.html')

@app.route('/singup', methods=[ 'POST'])
def singup1():
    uid=request.form.get('username')
    psw=request.form.get('password')
    #print(uid,psw)
    if singup(uid,psw)==True:
      #print('ok') 
      new_table(uid)
      return render_template('account_logined.html',posts='您的新账号：'+uid+',您的密码：'+psw)

if __name__ == '__main__':
    app.run()

