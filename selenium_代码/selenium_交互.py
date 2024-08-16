from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
import time

opt = ChromeOptions()
opt.headless = True
browser = Chrome()

url = 'https://www.baidu.com'
browser.get(url)

time.sleep(2)

#获取文本框的对象
input = browser.find_element(By.ID, 'kw')
#send_keys发送文本
input.send_keys('周杰伦')

time.sleep(2)

#获取百度一下按钮的对象
button = browser.find_element(By.ID, 'su')
#点击按钮
button.click()

time.sleep(2)

#滑到底部
js_bottom = ("document.documentElement.scrollTop = 100000")
browser.execute_script(js_bottom)

time.sleep(2)

#获取下一页按钮的对象
next = browser.find_element(By.LINK_TEXT, '下一页 >')
next.click()

time.sleep(2)

#回到上一页
browser.back()

time.sleep(2)

#回去
browser.forward()

time.sleep(2)

#退出
browser.quit()
