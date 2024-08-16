from bs4 import BeautifulSoup
#默认编码格式我gbk
soup = BeautifulSoup(open('bs4.html',  encoding='utf-8'),'lxml')

# 根据标签名查找节点
#默认第一个符合条件
print(soup.a)
#获取标签的属性与属性值
print(soup.a.attrs)

# bs4的函数

#find
#返回第一个符合条件的结果
print(soup.find('a'))
#根据title值找到对应的a标签
print(soup.find('a',title='a2'))
#根据class值找到对应的a标签(class是python的保留字，所以用class_代替)
print(soup.find('a',class_='c2'))


#find_all
#返回一个列表，包含所有符合条件的标签
print(soup.find_all('a'))
#如果想返回多个标签，用列表包含想要的数据标签名
print(soup.find_all(['a','span']))
#limit(n)限制返回的个数,前n返回前n个
print(soup.find_all('li',limit=2))


#select
#返回一个列表，包含所有符合条件的标签
print(soup.select('a'))
#返回class为c2的标签(.代表class)
print(soup.select('.c2'))
#返回id为lo的标签(#代表id)
print(soup.select('#lo'))
#找到a标签与li标签
print(soup.select('a,li'))

#属性选择器-----通过属性来寻找对应的标签
#查找li标签中带id的标签
print(soup.select('li[id]'))
#查找li标签中id为lo的标签
print(soup.select('li[id="lo"]'))

#层级选择器
#   后代选择器(' '(空格)代表后代选择器)
#   div下的li标签
print(soup.select('div li'))
#   子代选择器(>代表子代选择器)------莫一个标签下一级的标签
#   跨级标签返回空列表
#   div下的直接子代li标签
print(soup.select('div>li'))

#节点信息

#   获取节点内容
#   如果标签中只有内容 string与get_text()都可以
#   如果标签中有内容与标签属性，string获取不到标签属性，get_text()可以获取到标签全部属性
#   推荐用get_text()
obj = soup.select('#l1')[0]
print(obj.get_text())

#   获取节点属性
#   name 为标签的名字
obj = soup.select('#p1')[0]
print(obj.name)
#   attrs为标签的属性（将属性封装成一个字典）
print(obj.attrs)
#   通过一个属性名获取另一个属性值
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])


