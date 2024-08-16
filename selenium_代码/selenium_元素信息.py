from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.headless = True
browser = Chrome()

url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element(By.ID, 'su')
#get_attribute()方法可以获取标签的属性值
print(input.get_attribute('type'))
#tag_name方法可以获取标签名
print(input.tag_name)
#.text获取元素文本
#eg:  <ul>freedom</ul>   其中freedom为被获取文本
a = browser.find_element(By.LINK_TEXT, '新闻')
print(a.text)







