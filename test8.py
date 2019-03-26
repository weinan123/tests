from selenium import webdriver
import time
url = 'https://www.baidu.com/'
browser= webdriver.Chrome()
browser.get(url)
txt = browser.find_elements_by_id("kw")
serch = browser.find_elements_by_id("serch")
time.sleep(2)
txt.sendkeys("weinan")
serch.click()
browser.close()
browser.quit()