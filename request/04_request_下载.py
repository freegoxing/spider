import asyncio

import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

"""
图片
"""

# url = 'https://p1.music.126.net/Ihj9xqzH8wSNf6R0LiuMcg==/109951169108036775.jpg?param=130y130'
# res = requests.get(url, headers=headers)
# with open('test.jpg', 'wb') as f:
#     f.write(res.content)

"""
mp3
"""

# url = 'https://m704.music.126.net/20240827155804/d969d825b048d0c3b8735f1a7777d079/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/19557253809/087d/4cf7/a874/107710b990d0875794a14fca6bd4c86e.m4a?authSecret=0000019192c0a52600370a3b1d828978'
#
# res = requests.get(url, headers=headers)
# with open('红与黑.mp3', 'wb') as f:
#     f.write(res.content)

"""
mp4
"""

# url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/MSBmMDAkZGQjIjk0IWEwMA==/mv/393006/2a5eecbb0ed246dd63f967075eca143c.mp4?wsSecret=20ea6e213b449967c1084a65bde6dfc7&wsTime=1724744414'
# res = requests.get(url, headers=headers)
# with open('see you again.mp4', 'wb') as f:
#     f.write(res.content)

"""
html
"""

# url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%8D%97%E6%98%8C%E5%A4%A7%E5%AD%A6'
# res = requests.get(url, headers=headers)
# with open('test.html', 'wb') as f:
#     f.write(res.content)

"""
多面html
"""

# class类封装
# class Tieba:
#     def __init__(self):
#         self.url = 'http://tieba.baidu.com/f'
#         self.haeders = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
#         }
#
#
#     def send(self, params):
#         res = requests.get(url=self.url, headers=self.haeders, params=params)
#         return res.content
#
#
#     def save(self, name, page, con):
#         for page in range(1, page + 1):
#             with open(f'test/{name}_{page}.html', 'wb') as f:
#                 f.write(con)
#
#
#     def run(self):
#         name = input('the name of the object you need search:')
#         page = int(input('the page you want to search:'))
#
#         params = {
#             'ie': 'utf-8',
#             'kw': name,
#             'page': page*50
#         }
#
#         con = self.send(params)
#         self.save(name, page, con)
#
#
# if __name__ == '__main__':
#     a = Tieba()
#     a.run()



