from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.sina.com.cn")

driver.page_source
