from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import re
import pyautogui

browser = webdriver.Chrome("/Users/kunwoosmac/Downloads/chromedriver")

def Apart_Name(street_name):
    try:
        # 네이버에 검색해서 해당 아파트 이름 가져오기
        browser.get("https://www.naver.com")
        try:
            WebDriverWait(browser,10).until(ec.presence_of_element_located(By.ID, "query"))
        except:
            time.sleep(1)

        elem = browser.find_element_by_id("query")
        elem.send_keys(street_name)
        browser.find_element_by_id("search_btn").click()

        try:
            WebDriverWait(browser,10).until(ec.presence_of_element_located(By.CLASS_NAME, "ITiBH"))
        except:
            time.sleep(1)
        # print(browser.find_element_by_class_name("ITiBH").text)
        # print(browser.find_elements_by_class_name("_3rnws")[0].text)
        # print(browser.find_elements_by_class_name("_3rnws")[1].text)
        add = browser.find_element_by_class_name("ITiBH").text
        add = re.split(' ', add)[1]
        apart_name = browser.find_elements_by_class_name("_3rnws")[1].text
        apart_name = re.split('지번', apart_name)[0]
        add2 = browser.find_elements_by_class_name("_3rnws")[1].text
        add2 = re.split('서울특별시', add2)[1]
        match_add = "서울시" + str(re.split('\d', add2)[0])
        apart_name = str(add + apart_name)

        return apart_name, match_add
    except:
        return "Error", "Error"

def Search_Real(apart_name, match_add):
    try:
        # 부동산에서 검색
        browser.get("https://land.naver.com/")
        time.sleep(1)
        elem = browser.find_element_by_id("queryInputHeader")
        elem.send_keys(apart_name)
        browser.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div/div[1]/div/fieldset/a[1]").click()

        time.sleep(1)

        # 단지정보 클릭
        try:
            browser.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
            time.sleep(1)
        ####여기서 정보 바로 안드가져도 될 수 있게 보완 필요
        except:
            add = []
            elem = browser.find_elements_by_class_name("address")
            for i in range(0, len(elem)):
                add.append(re.sub(' ','', elem[i].text))
            # print(add)

            matchadd = re.sub(' ','',match_add)

            for i in range(0, len(add)):
                if add[i] == matchadd:
                    # print(add[i], match_add)
                    # print("YES")
                    try:
                        browser.find_elements_by_class_name("address")[i].click()
                    except:
                        pass

            time.sleep(1)
            try:
                browser.find_element_by_xpath(\
                    "/html/body/div[2]/div/section/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]").click()
            except:
                pyautogui.moveTo(x=133, y=452)
                pyautogui.click()

            time.sleep(1)

        #########################################
        info = browser.find_element_by_id("detailContents1").text
        info = re.split('\n', info)
        print(info)
        print("================================")
        info2 = []

        for i in range(0, len(info)):
            info2.extend(re.split(' ', info[i]))
        
        print(info2)
        print("================================")

        saedae = info2[info2.index("세대수")+1]
        parking = info2[info2.index("총주차대수") + 1] + info2[info2.index("총주차대수") + 2]
        yong = info2[info2.index("용적률") + 1]
        gun = info2[info2.index("건폐율") + 1]

        return saedae, parking, yong, gun


    except Exception as err:
        print(err)
        return "Error","Error","Error","Error"

print(Search_Real("서초구 삼정아파트", "ㅇ"))