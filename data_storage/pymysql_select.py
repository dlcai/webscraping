import pymysql

conn = pymysql.connect(host='localhost',
                user='root',
                password='caonima110',
                port=3306,
                db='spiders')
cursor = conn.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    next_one = cursor.fetchone()  
    print('cursor.fetchone():', next_one)
    results = cursor.fetchall() # 取一次后偏移指针指向下一条数据
    print('cursor.fetchall():')
    print('Results:', results)
    print('Results type:', type(results))
    for row in results:
        print(row)
except Exception as e:
    print(repr(e))   # 查询操作不需要commit()和rollback()保证一致性

# while循环 + fetchone() 逐条读取，数据量大时可减少内存开销
print('while + fetchone():')
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except Exception as e:
    print(repr(e))

conn.close()
