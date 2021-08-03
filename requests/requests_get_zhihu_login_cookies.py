import requests
import re

headers = {
    'Cookie':'KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1627843461|1627843404; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1627843439; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1627742912,1627831288; JOID=Wl8cA0vy7uOTJlCMQvrZMvXCZfVQpLDc138q4Xqikpf3ExPqG6oC7PohUYtLbDalMLju7s9FbseWNTBY7UiKROc=; SESSIONID=YP6DQuc1Xszm5KiW67Pz5dyvbTQdlIj68EYykpy9LsW; osd=UFgdAk346eKSIFqLQ_vfOPLDZPNao7Hd0XUt4HukmJD2EhXgHKsD6vAmUIpNZjGkMb7k6c5EaM2RNDFe50-LReE=; q_c1=f6aedf3e99f942f89c9be406d4694002|1627770274000|1508576983000; z_c0="2|1:0|10:1616780546|4:z_c0|92:Mi4xcDJJRkFBQUFBQUFBb09SUFg5dVdFQ1lBQUFCZ0FsVk5BbXRMWVFDazJYQjZmTlBPSUM3cnUxUFR4aG1fVEpOMy1R|981a521653884f433af0317dc90c42c955fa21b39698f859405e80fd806c2ef7"; _xsrf=WuyZVTpBwpT6S5qUmKc456ZodQ3BOzt8; _zap=e1e7b409-b59d-4ba0-9a22-72f83a4c82dc; d_c0="AKDkT1_blhCPTiBOK5RU3zylsLoJhj8Ekt8=|1577781743"',
    'Host': 'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '+\
        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
}

r = requests.get('https://www.zhihu.com/follow', headers=headers)
print(r.status_code)
print(r.text)
if re.search(r'登陆', r.text):
    print('login failed')
if re.search(r'<img class="Avatar AppHeader-profileAvatar.*?/>', r.text):
    print('logged in zhihu by Cookie in headers')
else:
    print('login failed')

with open('zhihu_login.html', 'w') as f:
    f.write(r.text)
