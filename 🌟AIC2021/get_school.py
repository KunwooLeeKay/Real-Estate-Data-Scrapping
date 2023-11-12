from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome("/Users/kunwoosmac/Downloads/chromedriver")
browser.get("https://realty.daum.net/home/apt/danjis/7611")
browser.maximize_window()
# elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/input")

# from selenium.webdriver.common.keys import Keys
# elem.send_keys("개포자이")
# time.sleep(3)


# elem.send_keys(Keys.ENTER)
# elem.send_keys(Keys.ENTER)

# time.sleep(1)

#초등학교
#elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div")

# 더보기 있으면 누르고 아님 패스
while True:
    try:
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]\
            /div[2]/div/div[14]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]").click()
    except:
        break

browser.implicitly_wait(10)
school1 = []
number = 3
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div["+str(number)+"]/div[1]/div[1]/div")
        school1.append(elem.text)
        number += 2
    except:
        break
print(school1)

# 중학교


# button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]")
# browser.execute_script("arguments[0].click();", button)
# elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div").click()
#WebDriverWait(browser,10).until(ec.element_to_be_clickable(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]"))
# browser.implicitly_wait(10)
elem = browser.find_element_by_xpath("//div[@data-testid='학군정보_탭_1_text']")

# elem.click()

while True:
    try:
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]").click()
    except:
        break


school2 = []
number = 3
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div["+str(number)+"]/div[1]/div[1]/div")
        school2.append(elem.text)
        number += 2
    except:
        break
print(school2)

# 고등학교

# button = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[3]/div/div[1]")
# browser.implicitly_wait(10)
# browser.execute_script("arguments[0].click();", button)


elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[1]/div[2]/div[3]/div/div[1]")
browser.implicitly_wait(10)
elem.click()
# elem = WebDriverWait(browser,10).until(ec.presence_of_element_located(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div"))
while True:
    try:
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]").click()
    except:
        break
browser.implicitly_wait(10)

school3 = []
number = 3
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[14]/div/div[1]/div[2]/div/div[2]/div[1]/div["+str(number)+"]/div[1]/div[1]/div")
        school3.append(elem.text)
        number += 2
    except:
        break
print(school3)