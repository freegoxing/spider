# 导入urllib.request模块
import urllib.request
# 定义要访问的网址
url = 'http://www.baidu.com'
# 使用urllib.request.urlopen()方法打开网址，并将返回的响应赋值给response变量
response = urllib.request.urlopen(url)
# 打印response的类型
#<class 'http.client.HTTPResponse'>
print(type(response))


# 按照一个字节一个字节读取数据
#n为读多少字节，默认为-1，表示读取全部数据
# content = response.read(n)
# print(content)


# 按照一行一行读取数据
# content = response.readline()
# print(content)


# 按照一行一行读取数据，直到读取完所有数据
# content = response.readlines()
# print(content)


# 获取响应的状态码 200正常
# print(response.getcode())
#

# 获取响应的URL
# print(response.geturl())


# 获取响应的头部信息
# print(response.getheaders())
