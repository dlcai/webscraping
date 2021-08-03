import requests

#requests.packages.urllib3.disable_warnings()
r = requests.get('https://kyfw.12306.cn', verify=False)
#r = requests.get('https://www.12388.gov.cn')
print(r.status_code)
