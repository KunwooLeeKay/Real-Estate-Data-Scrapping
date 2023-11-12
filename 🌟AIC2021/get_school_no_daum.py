from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome("/Users/kunwoosmac/Downloads/chromedriver")
browser.get("https://schoolzone.emac.kr/gis/gis.do")
browser.maximize_window()

browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select").click()
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select/option[2]").click()


elem = browser.find_element_by_id("searchText")

from selenium.webdriver.common.keys import Keys
elem.send_keys("언주로 103")
elem.send_keys(Keys.ENTER)
browser.find_element_by_xpath("/html/body/div[1]/div[10]/div[1]/p/input").click()
browser.find_element_by_xpath("/html/body/div[1]/div[9]/div[1]/p/input").click()

browser.switch_to.frame(browser.find_element_by_name('searchIframe'))  # iframe있으면 이거 해줘야함..!

# WebDriverWait(browser,10).until(ec.presence_of_element_located((By.CLASS_NAME, "btn_school_search1")))

search1 = browser.find_elements_by_class_name("btn_school_search1")
search1[len(search1)-1].click()

# iframe 리스트 : 
# schoolAreaIframe, iframe_hakguInfo, iframe_schoolDetail2, iframe_schoolDetail3, iframe_schoolDetail4, iframe_schoolDetail5

browser.switch_to.default_content() #iframe 나가기
browser.switch_to.frame(browser.find_element_by_name('schoolAreaIframe'))

# 상세정보 누르기
# button = browser.find_elements_by_class_name("btn_style12")
# button[0].click()

# elem = browser.find_elements_by_class_name("table_s1")
elem = browser.find_element_by_xpath("/html/body/div[2]/div/dl/dd/table/tbody/tr/td[1]/a")
school1 = []
print(elem.text)
# for i in range(1, len(elem)):
#     print(elem[i].text)



# elem = browser.find_elements_by_tag_name("a")


# elem_real = []
# for i in range(0,len(elem)-1):
#     elem_real.append(elem[i].__getattribute__("href"))

# elem = browser.find_elements_by_name("elementSchoolRadio")

# for i in range(1, len(elem_real)):
#     school1.append(elem_real[i-1].text)
# print(school1)


