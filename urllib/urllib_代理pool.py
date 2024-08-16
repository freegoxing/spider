import random
import urllib.request

proxies_pool = [
    {'http':''},
    {'http':''}
]

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/w?=ip'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
with open('ip.html','w',encoding='utf-8') as f:
    f.write(content)
