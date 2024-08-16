import urllib.request

url = 'https://ip.900cha.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http':'121.230.211.142:3256'
}

handler = urllib.request.ProxyHandler(proxies=proxies)
# handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('ipdaili.html', 'w', encoding='utf-8') as f:
    f.write(content)


