from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver') 

driver.get('https://www.cricbuzz.com/')

data = driver.find_element_by_xpath('//*[@id="cb-news-blck"]/div')

print(data.text)
