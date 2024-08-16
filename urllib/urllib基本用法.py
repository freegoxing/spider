import urllib.request
# 定义要访问的URL
url = "https://www.baidu.com"
# 打开URL
response = urllib.request.urlopen(url)
# 读取URL的内容
#read方法   返回子节形式的二进制代码（b开头）
#b'<html>\r\n<head>\r\n\t<script>\r\n\t\tlocation.replace(location.href.replace("https://","http://"));\r\n\t</script>\r\n</head>\r\n<body>\r\n\t<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>\r\n</body>\r\n</html>'
#二进制--->字符串    decode方法
content = response.read().decode("utf-8")
# 打印URL的内容
print(content)


