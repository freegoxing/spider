from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
import time
#创建一个浏览器对象
opt = ChromeOptions()
opt.headless = True
browser = Chrome()
#访问网站
url = 'https://www.baidu.com'
browser.get(url)
#find_element(s)方法,有s表示返回的是一个列表，把所有符合的对象返回
# #元素id定位
# button= browser.find_element(By.ID,'su')
# print(button)
#
# #根据标签的属性值定位
# button = browser.find_element(By.NAME, 'wd')
# print(button)
#
# #利用xpath语句定位
# button = browser.find_element(By.XPATH, '//input[@type= "submit"]')
# print(button)
#
# #利用标签名（tag_name）定位
# button = browser.find_elements(By.TAG_NAME, 'input')
# print(button)
#
# #利用css定位（bs4的语法）
# button = browser.find_element(By.CSS_SELECTOR, '#su')
# print(button)

##利用链接文本（link_text, 即html中a标签)定位
# button = browser.find_element(By.LINK_TEXT, 'hao123')
# print(button)



