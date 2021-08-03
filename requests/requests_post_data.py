import requests 

data = {'name':'丁', 'age':'22'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text) 
print(r.content.decode('unicode_escape'))
