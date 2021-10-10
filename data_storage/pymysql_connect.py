import pymysql

# connect()方法创建Connection对象db
db = pymysql.connect(host='localhost', 
                     user='root', 
                     password='caonima110', 
                     port=3306)
cursor = db.cursor()  # Connection.cursor()方法获得操作游标，用于执行SQL语句
cursor.execute('SELECT VERSION()')
data = cursor.fetchone() # fetchone() 返回下一行数据，这里获得select到的第一条数据
print('Database version:', data)
cursor.execute('CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8')
db.close()
# 创建表
db = pymysql.connect(host='localhost', 
                     user='root', 
                     password='caonima110', 
                     port=3306,
                     db='spiders') # 额外的connect参数db，连接到创建的数据库
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students ' +\
      '(id VARCHAR(255) NOT NULL, ' + \
      'name VARCHAR(255) NOT NULL, ' +\
      'age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)

# 插入数据
id1 = '20120001'
name1 = 'Bob'
age1 = 20
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id1, name1, age1))
    db.commit()  # 数据插入、更新、删除都要Connection.commit()才能生效
except:  # 异常处理：若执行失败进行数据回滚
    db.rollback() # 保证事务的原子性：插入数据要么全都插入，要么全不插入，不存在插入一半的情况
db.close() # insert/update/delete都是对数据库更改的操作，必须为事务，都要采用rollback()异常处理






