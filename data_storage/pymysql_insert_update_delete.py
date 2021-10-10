import pymysql

conn = pymysql.connect(host='localhost',
                user='root',
                password='caonima110',
                port=3306,
                db='spiders')
cursor = conn.cursor()             

# SQL插入语句模版
data = {
    'id':'20120002',
    'name':'John',
    'age':'24',
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))
sql = f'INSERT INTO {table}({keys}) VALUES({values})'
print(sql)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('INSERT successfully')
        conn.commit()
except Exception as e:
    print(repr(e))
    print('INSERT failed')
    conn.rollback()

# 更新数据
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    if cursor.execute(sql, (25, 'Bob')):
        print('UPDATE successfully')
        conn.commit()
    else:
        print('No rows affected')
except Exception as e:
    print(repr(e))
    print('UPDATE failed')
    conn.rollback()

# 主键不存在时插入，主键已存在时更新
data = {
    'id':'20120002',
    'name':'John',
    'age':'30',
}
sql = f'INSERT INTO {table}({keys}) VALUES({values}) ON DUPLICATE KEY UPDATE'
update_sql = ','.join([f' {key} = %s' for key in data])
sql += update_sql
print(sql)
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('INSERT INTO ... ON DUPLICATE KEY UPDATE successfully')
        conn.commit()
    else:
        print('No rows affected')
except Exception as e:
    print(repr(e))
    print('INSERT ON DUPLICATE KEY UPDATE failed')
    conn.rollback()

# 删除数据
condition = "name = 'John'"
sql = f'DELETE FROM {table} WHERE {condition}'
try:
    if cursor.execute(sql):
        print('DELETE row successfully')
        conn.commit()
except Exception as e:
    print(repr(e))
    print('DELETE row failed')
    conn.rollback()

conn.close()
