#解析服务器响应数据
from lxml import etree
import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
#解析服务器数据
tree = etree.HTML(content)
#获取想要数据
result = tree.xpath('//input[@id="su"]/@value')[-1]
print(result)



