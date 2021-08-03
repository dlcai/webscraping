from requests import Request, Session

url = 'https://httpbin.org/post'
data = {'name':'丁', 'age':22}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}
req = Request('POST', url=url, data=data, headers=headers)
s = Session()
prepared_req = s.prepare_request(req)
r = s.send(prepared_req)
print(r.status_code)
print(r.text)
