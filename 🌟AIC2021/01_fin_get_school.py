# Q. 학교까지의 거리도 가져와야할까?
# 실거래가 정보 당시에 존재하던 학교인지 조회해야함. 학교 개교일 가져와서 그 전이면 삭제 필요

from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/kunwoosmac/Downloads/chromedriver")
browser.get("https://schoolzone.emac.kr/gis/gis.do")
browser.maximize_window()

# 지역을 서울로 지정
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select").click()
browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select/option[2]").click()

# =====루프 시작부 ====
elem = browser.find_element_by_id("searchText")

from selenium.webdriver.common.keys import Keys
# 여기에 도로명 주소 입력해줘야함
elem.send_keys("언주로 103")
elem.send_keys(Keys.ENTER)

browser.find_element_by_css_selector("pre").clear()

elem.send_keys("언주로 103")
elem.send_keys(Keys.ENTER)

# 팝업창 닫음
try:
    browser.find_element_by_xpath("/html/body/div[1]/div[10]/div[1]/p/input").click()
    browser.find_element_by_xpath("/html/body/div[1]/div[9]/div[1]/p/input").click()
except: pass

browser.switch_to.frame(browser.find_element_by_name('searchIframe'))  # iframe있으면 이거 해줘야함..!

# WebDriverWait(browser,10).until(ec.presence_of_element_located((By.CLASS_NAME, "btn_school_search1")))

search1 = browser.find_elements_by_class_name("btn_school_search1")
search1[len(search1)-1].click() # 맨 마지막에 있는거 클릭해줌

# iframe 리스트 : 
# schoolAreaIframe, iframe_hakguInfo, iframe_schoolDetail2, iframe_schoolDetail3, iframe_schoolDetail4, iframe_schoolDetail5

browser.switch_to.default_content() #iframe 나가기

browser.switch_to.frame(browser.find_element_by_name('schoolAreaIframe')) # 학군 정보 있는 iframe

# 초등학교
elem = browser.find_element_by_xpath("/html/body/div[2]/div/dl/dd/table/tbody/tr/td[1]/a")
school1 = [elem.text]
browser.find_element_by_xpath("/html/body/div[2]/div/dl/dt/a").click()
print(school1)

# 중학교
browser.find_element_by_xpath("/html/body/div[3]/div/dl/dt/a").click()
num = 1
school2 = []
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[3]/div/dl/dd/table/tbody/tr["+str(num)+"]/td[1]/a")
        school2.append(elem.text)
        num += 1
    except:
        break
browser.find_element_by_xpath("/html/body/div[3]/div/dl/dt/a").click()
school2 = list(filter(None, school2))
print(school2)

# 고등학교
browser.find_element_by_xpath("/html/body/div[4]/div/dl/dt/a").click()
num = 2
school3 = []
while True:
    try:
        elem = browser.find_element_by_xpath("/html/body/div[4]/div/dl/dd/table/tbody/tr["+str(num)+"]/td[1]/a")
        school3.append(elem.text)
        num += 1
    except:
        break
browser.find_element_by_xpath("/html/body/div[4]/div/dl/dt/a").click()
school3 = list(filter(None, school3))
print(school3)
