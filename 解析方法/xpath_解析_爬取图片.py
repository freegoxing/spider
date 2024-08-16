# 第一页
# https://sc.chinaz.com/tupian/qinglvtupian.html
# 第二页
# https://sc.chinaz.com/tupian/qinglvtupian_2.html

import urllib.request
from lxml import etree


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'

    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_{}.html'.format(page)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
#下载图片
#urllib.request.urlretetrive
#图片网站中有时会用懒加载，即图片的src属性有两个，一个为占位符，一个为真实地址，所以需要用真实地址，常见为src2的格式
#其在用户浏览时，会自动替换src的值，所以需要用真实地址
     tree = etree.HTML(content)
     name_list = tree.xpath('//body/div[@class="container"]//div/img/@alt')
     data_list = tree.xpath('//body/div[@class="container"]//div/img/@data-original')
     for i in range(len(name_list)):
         name = name_list[i]
         url = 'https:' + data_list[i]
         urllib.request.urlretrieve(url=url, filename='./img/' + name + '.jpg')


if __name__ == '__main__':
    start_page = input("请输入起始页：")
    end_page = input("请输入结束页：")

    for page in range(int(start_page), int(end_page)+1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)



