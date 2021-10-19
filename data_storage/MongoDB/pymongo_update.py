from pymongo_connect import *

condition = {'name':'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set':student})
print("collection.update_one(condition, {'$set':student}):")
print(result)
print(f'UpdateResult.matched_count: {result.matched_count}')
print(f'UpdateResult.modified_count: {result.modified_count}')

# 按条件更新 {'$inc':{'age':1}}
condition = {'age':{'$gt':20}}
result = collection.update_many(condition, {'$inc':{'age':1}}) # 年龄+1
print("collection.update_many(condition, {'$inc':{'age':1}}):")
print(result)
print(f'UpdateResult.matched_count: {result.matched_count}')
print(f'UpdateResult.modified_count: {result.modified_count}')
# $inc可以接收负值
condition = {'age':{'$gt':20}}
result = collection.update_many(condition, {'$inc':{'age':-1}}) # 年龄-1
print("collection.update_many(condition, {'$inc':{'age':-1}}):")
print(result)
print(f'UpdateResult.matched_count: {result.matched_count}')
print(f'UpdateResult.modified_count: {result.modified_count}')


