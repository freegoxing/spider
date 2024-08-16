
#（1）本地文件
#html_tree = etree.parse()
from lxml import etree

tree = etree.parse('xpath基本功能.html')
#tree.xpath('xpath路径)
#查找ul下的li
# li_list = tree.xpath('//body//ul/li')
# print(li_list)

#查找带id的li
#text()获取文本内容
# li_list = tree.xpath('//body//ul/li[@id]/text()')
# print(li_list)

#查找带id的li
# li_list = tree.xpath('//body//ul/li[@id="l1"]/text()')
# print(li_list)

#查找带id的li的class属性
# li = tree.xpath('//body//ul/li[@id="l1"]/@class')
# print(li)

#查找带id包含l的li标签
#contains()包含
# li_list = tree.xpath('//body//ul/li[contains(@id,"l")]/text()')
# print(li_list)
#starts-with()以什么开头
# li_list = tree.xpath('//body//ul/li[starts-with(@id,"l")]/text()')
# print(li_list)

#逻辑
#查找带id为l1   和  class为c1的li标签
# li_list = tree.xpath('//body//ul/li[@id="l1" and @class="c1"]/text()')
# print(li_list)
#查找带id为l1   或  者class为c1的li标签
# li_list = tree.xpath('//body//ul/li[@id="l2"]/text() | //body//ul/li[@class="c1"]/text()')
# print(li_list)





#（2）服务器响应数据    response.read().decode('utf-8')
#html_tree = etree.HTML(response.read().decode('utf-8'))