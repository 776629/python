import hashlib,sqlite3

def hash(data):
    result = hashlib.md5(data.encode('utf-8'))
    return result.hexdigest()

def db_join(username,password):
    password_hash=hash(password)
    db = sqlite3.connect('login.db')
    cursor = db.cursor()
    try:
        sql = "INSERT INTO data(username,password) VALUES ('" + username + "','" + password_hash + "')"
        cursor.execute(sql)
        db.commit()
    except:
        pass

def db_read(table,name):
    db = sqlite3.connect('login.db')
    cursor = db.cursor()
    select_sql = 'SELECT {} FROM {}'.format(name,table)
    try:
        cursor.execute(select_sql)
        result = cursor.fetchall()
        return result
    except:
        print("Select is failed")
        cursor.close()
        db.close()
        return

def db_delete(table):
    sql = sqlite3.connect('login.db')
    cur = sql.cursor()
    try:
        cur.execute('DELETE from {};'.format(table))
        sql.commit()
        sql.close()
    except:
        print('no')
