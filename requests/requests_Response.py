import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

r = requests.get('https://www.jianshu.com', headers=headers)
if not r.status_code == requests.codes.ok:
    exit()
else:
    print('Request successfully.')
print(r.status_code, type(r.status_code))
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)


