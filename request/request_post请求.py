import requests

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
data = {
    'kw':'spider'
}
#post 的参数
#url, data=None(参数）, json=None, **kwargs（字典）
response = requests.post(url=url, data=data, headers=headers)

content = response.text

print(content)





