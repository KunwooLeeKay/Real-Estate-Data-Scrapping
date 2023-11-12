from selenium import webdriver
import re
browser = webdriver.Chrome("/Users/kunwoosmac/Downloads/chromedriver")

def Get_Data(street):

    browser.get("https://schoolzone.emac.kr/gis/gis.do")
    # 지역을 서울로 지정
    try:
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select").click()
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select/option[2]").click()
    except: 
        print("에러 line 17")
        return 0,0,0
    # 도로명 주소 검색부
    elem = browser.find_element_by_id("searchText")
    from selenium.webdriver.common.keys import Keys
    # 여기에 도로명 주소 입력해줘야함
    try:
        elem.send_keys(street)
    except:
        print(street + "sendkeys 오류!")
        return 0,0,0
    if len(street)<=2:
        return 0,0,0
    try:
        elem.send_keys(Keys.ENTER)
    except:
        print(street + "엔터 오류!")
        return 0,0,0

    # 팝업창 닫음
    try:
        browser.find_element_by_xpath("/html/body/div[1]/div[10]/div[1]/p/input").click()
        browser.find_element_by_xpath("/html/body/div[1]/div[9]/div[1]/p/input").click()
    except: pass

    browser.switch_to.frame(browser.find_element_by_name('searchIframe'))  # iframe있으면 이거 해줘야함..!

    # WebDriverWait(browser,10).until(ec.presence_of_element_located((By.CLASS_NAME, "btn_school_search1")))
    try:
        try:
            browser.find_element_by_xpath("/html/body/div[5]/div/ul[2]/li[1]/input").click()
            #/html/body/div[5]/div/ul[2]/li[1]/input
        except:
            browser.find_element_by_xpath("/html/body/div[5]/div[1]/ul[2]/li[1]/input").click()
    ### 검색 안될때!!!!!
    except:
        browser.get("https://schoolzone.emac.kr/gis/gis.do")
        # 지역을 서울로 지정
        try:
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select").click()
            browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div/span[1]/select/option[2]").click()
        except: 
            print("에러 line 17")
            return 0,0,0
        elem = browser.find_element_by_id("searchText")

        if '-' in street:
            st = re.split('-', street)[0]
            street = st
        elif '길' in street:
            st = re.split('길', street)[0] + '길'
            street = st
        elem.send_keys(street)
        elem.send_keys(Keys.ENTER)
        try:
            try:
                browser.find_element_by_xpath("/html/body/div[5]/div/ul[2]/li[1]/input").click()
                #/html/body/div[5]/div/ul[2]/li[1]/input
            except:
                browser.find_element_by_xpath("/html/body/div[5]/div[1]/ul[2]/li[1]/input").click()
        except:
            pass


    try:
        # iframe 리스트 : 
        # schoolAreaIframe, iframe_hakguInfo, iframe_schoolDetail2, iframe_schoolDetail3, iframe_schoolDetail4, iframe_schoolDetail5

        browser.switch_to.default_content() #iframe 나가기

        browser.switch_to.frame(browser.find_element_by_name('schoolAreaIframe')) # 학군 정보 있는 iframe

        # 초등학교
        try:
            elem = browser.find_element_by_xpath("/html/body/div[2]/div/dl/dd/table/tbody/tr/td[1]/a")
            school1 = [elem.text]
            browser.find_element_by_xpath("/html/body/div[2]/div/dl/dt/a").click()
            #print(school1)

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
            #print(school2)

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
        except:
            print(street+"에러!")
            return 0,0,0
    except:
        return 0,0,0
        
    #print(school3)
    return school1, school2, school3

import pickle

with open("도로명_리스트.pickle", "rb") as pickle_data:
    street = pickle.load(pickle_data)

elem_street = {}
mid_street = {}
high_street = {}

for i in range(0, len(street)):
    try:
        elem, mid, high = Get_Data(street[i])
        elem_street[street[i]] = elem
        mid_street[street[i]] = mid
        high_street[street[i]] = high
    except:
        print(street[i] + "error")
        pass

with open("도로별_초등학교_이름.pickle", "wb") as pickle_data:
    pickle.dump(elem_street, pickle_data)

with open("도로별_중학교_이름.pickle", "wb") as pickle_data:
    pickle.dump(mid_street, pickle_data)

with open("도로별_고등학교_이름.pickle", "wb") as pickle_data:
    pickle.dump(high_street, pickle_data)