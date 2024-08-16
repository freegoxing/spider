import requests

url = 'https://www.baidu.com/?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}

data = {
    'wd': 'ip'
}

p
roxy = {
    'http':'121.230.210.31:3256'
}

response = requests.get(url=url, headers=headers, params=data, proxies=proxy)

content = response.text

with open('dailii.html', 'w', encoding='utf-8') as f:
    f.write(content)



