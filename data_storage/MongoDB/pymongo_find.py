from pymongo_connect import *
# 查询 find_one()返回单个结果，dict类型，自动添加了_id属性
result = collection.find_one({'name':'Jordan'})
print("collection.find_one({'name':'Jordan'})")
print(result, type(result))

#根据_id字段的ObjectId查询
from bson.objectid import ObjectId

result = collection.find_one({'_id':ObjectId(str(result['_id']))})
print("collection.find_one({'_id':ObjectId('...')})")
print(result)

# find({filter})根据条件返回多个结果，Cursor对象(一个generator)
results = collection.find({'age':{'$gt':20}})
print("collection.find({'age':{'$gt':20}}):")
print(results) 
for result in results:
    print(result, type(result))

# 正则匹配查询 '$regex'
results = collection.find({'name':{'$regex':'^M.*'}})
print("collection.find({'name':{'$regex':'^M.*'}}):")
print(results)
for result in results:
    print(result, type(result))

# 计数 count()
count = collection.find().count()
print("collection.find().count(): (Deprecated)")
print(count)
count = collection.estimated_document_count()  # O(1)
print("collection.estimated_document_count():  O(1)")
print(count)
count = collection.count_documents({})  # O(n)
print("collection.count_documents({}):  O(n)")
print(count)

# 排序
results = collection.find().sort('name', pymongo.ASCENDING) 
print("collection.find().sort('name', pymongo.ASCENDING):")
print([result['name'] for result in results])

# 偏移 skip(n) 忽略前n个元素
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print("collection.find().sort('name', pymongo.ASCENDING).skip(2)")
print([result['name'] for result in results])

# 截取前n个 limit(n)
results = collection.find().sort('name', pymongo.ASCENDING).limit(2)
print("collection.find().sort('name', pymongo.ASCENDING).limit(2)")
print([result['name'] for result in results])

# 数据量庞大时如果使用大的偏移量查询数据可能导致内存溢出，采用条件筛选ObjectId的方法
object_id = str(collection.find_one({'name':'Jordan'})['_id'])
results = collection.find({'_id':{'$gt':ObjectId(object_id)}})
print("collection.find({'_id':{'$gt':ObjectId(object_id)}}):")
print([result['name'] for result in results])
