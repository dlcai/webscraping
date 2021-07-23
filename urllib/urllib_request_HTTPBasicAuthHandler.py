from urllib.request import HTTPBasicAuthHandler, build_opener, HTTPPasswordMgrWithDefaultRealm
from urllib.error import URLError

username = 'john' 
password = 'password'
url = 'http://pythonscraping.com/pages/auth/login.php'

pw_mgr = HTTPPasswordMgrWithDefaultRealm()
pw_mgr.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(pw_mgr)
opener = build_opener(auth_handler)

try:
    response = opener.open(url)
    html = response.read().decode('utf-8')
    print(response.status)
    print(html)
    print(response.getheaders())
except URLError as e:
    print(e.reason)
