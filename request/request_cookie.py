
#找登录接口
#可以输入错误的密码来查询登录接口（常见带有log_in, sign_in, auth等）

#获取登录接口的请求参数，很多
# __VIEWSTATE: 1GMfJLXLbp2J6tL6RLTeRiwTT4FJYbKvvgkgz42X6f4hAX6SlDiuXljiMPO/Qy5Zc7PVxVRaI0NmYJb5+NjdfbEW62jS8azAnlWFVc7jwxjwlR5jK0hK9xfg7KGCjj4eRLRm3TXbSOC/l1PCuYFywOkb9Kc=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://www.gushiwen.cn/user/collect.aspx
# email: 18107018986
# pwd: qwer1234QWE
# code: N3Z9
# denglu: 登录

#其中__VIEWSTATE， __VIEWSTATEGENERATOR，code是动态变化的，需要动态获取
#一般看不到的参数可从页面源码获取

from bs4 import BeautifulSoup
# import urllib.request
import requests

#登录页面url地址
url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

content = response.text

#获取__VIEWSTATE， __VIEWSTATEGENERATOR

soup = BeautifulSoup(content, 'lxml')

__VIEWSTATE = soup.select('#__VIEWSTATE')[0]['value']

__VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0]['value']
#获取验证码图片
code = soup.select('#imgCode')[0]['src']
code_url = 'https://www.gushiwen.cn' + code
#下载到本地，利用input赋值给code
#这个方法不行，因为验证码是动态变化的，每次刷新都会变，前面已经请求了一次，所以验证码已经失效了
# urllib.request.urlretrieve(code_url, 'code.jpg')
#利用request中session对象，可以保持会话，这样就可以获取到动态变化的验证码了
session = requests.session()
response_code = session.get(code_url)
#此时要用二进制保存图片
content_code = response_code.content
#wb表示写入二进制写入
with open('code.jpg', 'wb')as f:
    f.write(content_code)
#验证码图片下载成功后，手动输入验证码
code = input('请输入验证码：')

#登录请求参数
url_post = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '18107018986',
    'pwd': 'qwer1234QWER',
    'code': code,
    'denglu': '登录'
}

response_post = session.post(url=url_post, data=data_post, headers=headers)

content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as f:
    f.write(content_post)



