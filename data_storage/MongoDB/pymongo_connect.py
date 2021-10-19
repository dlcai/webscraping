import pymongo
# 连接
print('Connecting to mongo client...use test ; db.students')

client = pymongo.MongoClient(host='localhost', port=27017)
#client = pymongo.MongoClient('mongodb://localhost:27017/')
print(type(client))
# 指定数据库
db = client.test
# db = client['test']
print(type(db))
# 指定集合(类似关系型数据库中的表)
collection = db.students
print(type(collection))

# 数据
student1 = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2 = {
    'id':'20170102',
    'name':'Mike',
    'age':21,
    'gender':'male'
}
student3 = {
    'id':'20170103',
    'name':'Kevin',
    'age':23,
    'gender':'male'
}
student4 = {
    'id':'20170104',
    'name':'Page',
    'age':26,
    'gender':'female'
}
