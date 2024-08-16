import Chrome
from selenium.webdriver.common.by import By

broswer = Chrome.browser()

url = "https://cn.58.com/quanzhizhaopin/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=strategy%2Cuuid_88985d81501a4c9e93193cbae32b2437%2Cdisplocalid_2258%2Cfrom_674%2Cto_jump%2Ctradeline_job%2Cclassify_B&search_uuid=88985d81501a4c9e93193cbae32b2437&final=1"

broswer.get(url)

button = broswer.find_element(By.XPATH, '//div[@id="filter"]/div[@class="tags"]/a/span')
print(button)