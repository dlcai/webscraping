import requests

data = {
    'name': 'john',
    'age': 22
}

r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print(type(r.text)) # json格式的str
print(r.json()) # 将json格式的str转化为字典
print(type(r.json())) # dict

