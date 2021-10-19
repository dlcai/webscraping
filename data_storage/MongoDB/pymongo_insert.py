from pymongo_connect import *
# 插入insert_one()  insert_many() 3.X之前：insert

result = collection.insert_one(student1)
print('collection.insert_one(dict):')
print(result)
inserted_id = result.inserted_id
print(inserted_id, type(inserted_id))  # 对象id，每条数据的唯一标识
print(str(inserted_id), type(str(inserted_id)))  

results = collection.insert_many([student2, student3, student4])
print('collection.insert_many([]):')
print(results)
print(results.inserted_ids)




