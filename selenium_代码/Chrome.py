from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
#
# path = r'D:\Daily software\Google\Chrome\Application\chrome.exe'
# chrome_options.binary_location = path
#
# browser = Chrome(chrome_options)

# url = 'https://baidu.com'
#
# browser.get(url)
#
# browser.save_screenshot('baidu.png')


def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    path = r'D:\Daily software\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = Chrome(chrome_options)

    return browser
























