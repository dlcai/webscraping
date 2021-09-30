import json

json_str = '''
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
}, {
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
'''
# loads() 把json字符串转成python数据结构
data = json.loads(json_str)
print(type(data))
print(data)

print(data[1]['name'])
print(data[1].get('name'))
print(data[0].get('age')) # python dict get 如果key不存在不会报错，返回None

with open('data.json', 'r') as f:
    json_str = f.read() # 返回str 至多读取[size]个字节
    data = json.loads(json_str)
    print(data)

# load() 把json文件直接转成python数据结构
with open('data.json', 'r') as f:
    data = json.load(f, parse_int=int)
    print(data)
    
# dumps() 把python数据结构转成json字符串
data = [{
    'name':'王伟',
    'gender':'男',
    'birthday':'1992-12-18'
}]

with open('data_chinese.json', 'w') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))
