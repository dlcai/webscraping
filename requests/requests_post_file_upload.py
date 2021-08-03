import requests

files = {'file':open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.status_code)
print(r.text)
files['file'].close()
