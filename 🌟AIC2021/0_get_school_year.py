import pickle

with open("final_중학교_리스트.pickle", "rb") as pickle_data: 
    mid = pickle.load(pickle_data)

print(len(mid))

with open("final_고등학교_리스트.pickle", "rb") as pickle_data: 
    high = pickle.load(pickle_data)

print(len(high))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

browser = webdriver.Chrome("/Users/kunwoosmac/Downloads/chromedriver")

# school_name = mid[0]
whole_data_mid = {}
for i in range(0, len(mid)):
    try:
        school_name = mid[i]
        # 네이버에 검색해서 해당 아파트 이름 가져오기
        browser.get("https://www.naver.com")
        time.sleep(1)

        elem = browser.find_element_by_id("query")
        elem.send_keys(school_name)
        browser.find_element_by_id("search_btn").click()

        time.sleep(1)
    except Exception as err:
        school_info = "Error_can't_search"
        print(err)
    try:
        school_info = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[1]/div[1]/ul/li[3]/span[2]/span").text
        print(school_info)
    except:
        school_info = "Error_different_form"
    
    whole_data_mid[school_name] = school_info

with open("중학교_개교.pickle", "wb") as pickle_data: 
    pickle.dump(whole_data_mid,pickle_data)

whole_data_high = {}
for i in range(0, len(high)):
    try:
        school_name = high[i]
        # 네이버에 검색해서 해당 아파트 이름 가져오기
        browser.get("https://www.naver.com")
        time.sleep(1)

        elem = browser.find_element_by_id("query")
        elem.send_keys(school_name)
        browser.find_element_by_id("search_btn").click()

        time.sleep(1)
    except Exception as err:
        school_info = "Error_can't_search"
        print(err)
    try:
        school_info = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[1]/div[1]/ul/li[3]/span[2]/span").text
        print(school_info)
    except:
        school_info = "Error_different_form"
    
    whole_data_high[school_name] = school_info

with open("고등학교_개교.pickle", "wb") as pickle_data: 
    pickle.dump(whole_data_high,pickle_data)