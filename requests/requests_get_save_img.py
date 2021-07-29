import requests

r = requests.get('https://github.com/favicon.ico')
print(r.text)
print(r.content)  # response body in bytes

with open('favicon.ico', 'wb') as f:
    f.write(r.content)
