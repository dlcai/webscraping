from pymongo_connect import *

student = {
    'id':'20170105',
    'name':'dogm',
    'age':29,
    'gender':'male'
}

result = collection.insert_one(student)
print("collection.insert_one(student):")
print(result)

result = collection.delete_one({'name':'dogm'})
print("collection.delete_one({'name':'dogm'}):")
print(result)
print(result.deleted_count)

result = collection.delete_many({'age':{'$lt':18}})
print("collection.delete_many({'age':{'$lt':18}}):")
print(result)
print(result.deleted_count)

# 还有 find_one_and_delete()  find_one_and_replace
# create_index() create_indexes() drop_index()等

