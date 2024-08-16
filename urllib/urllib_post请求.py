import urllib.request
import json

url = 'https://fanyi.baidu.com/sug'

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

data = {
    'kw':'spider'
}

#post请求的参数，必须编码成bytes类型
#第一个参数是编码后的参数，第二个参数是编码格式
data = urllib.parse.urlencode(data).encode('utf-8')
#post请求的参数不会在url中显示，必须放在请求体中
request = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)