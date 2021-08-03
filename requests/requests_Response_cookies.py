import requests

r = requests.get('https://www.baidu.com')
print(type(r.cookies)) # requests.cookies.RequestsCookieJar, python dict interface
print(r.cookies)

for key, value in r.cookies.items():  # list of key-value tuples
    print(f'{key} = {value}')
