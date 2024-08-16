import urllib.request

url = "https://www.baidu.com"

#url组成
#https://www.bing.com/search?wd=周杰伦
#http/https    www.bing.com     80/443         s       wd=周杰伦
#   协议             域名          端口号        路径        参数       锚点
#   http    80
#   https   443
#   mysql   3306

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

#因为urlopen不能存储字典，headers需要转换
#因为Request参数顺序，不能直接将headers传入，要用关键子传参
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
coontent = response.read().decode("utf-8")
print(coontent)
