import sqlite3

def DB_read(DB_name,table,name):
    db = sqlite3.connect(DB_name)
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

def posts_db():
    posts= [] 
    lens=len(DB_read('data.db','data','msg'))
    for i in range(lens):
        tpl=(DB_read('data.db','data','msg')[i])
        part_msg=' '.join(tuple(tpl))    
        posts.append({'name':'NONE', 'msg':part_msg})
    return posts
    
def db_delete(db_name,table):
    sql = sqlite3.connect(db_name)
    cur = sql.cursor()
    try:
        cur.execute('DELETE from {};'.format(table))
        sql.commit()
        sql.close()
    except:
        pass
 


def new_table(uid):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    sql = 'create table {} (msg string)'.format(uid)
    cursor.execute(sql)
    cursor.close()
    return

def db_join(uid,msg):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    sql = "INSERT INTO {} (msg) VALUES ('{}')".format(uid,msg)
    cursor.execute(sql)
    db.commit()


