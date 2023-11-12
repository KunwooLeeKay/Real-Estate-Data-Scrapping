from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome("/Users/kunwoosmac/Library/Mobile Documents/com~apple~CloudDocs/Mac/LearnPython/🌟AIC2021/chromedriver")
browser.get("https://realty.daum.net/home/apt/")
browser.maximize_window()
elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/input")

from selenium.webdriver.common.keys import Keys
elem.send_keys("개포자이")
time.sleep(3)


elem.send_keys(Keys.ENTER)
elem.send_keys(Keys.ENTER)

time.sleep(1)

# 더보기란 클릭
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/\
    div[2]/div/div[3]/div[1]/div[1]/div/div[1]/div/div[1]/div/div[1]").click()

parkinglot = []
parkinglot.append(browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/\
    div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div/div[7]/div[2]/div[2]/div").text)

print(parkinglot)