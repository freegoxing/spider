import requests

url = 'https://cn.bing.com/search?'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
}

date = {
    'q':'北京'
}

#get 有三个参数 url headers data（**kwargs：字典
response = requests.get(url=url, headers=headers, params=date)

content = response.text

print(content)


#get请求中的参数data不需要encode或quote




























