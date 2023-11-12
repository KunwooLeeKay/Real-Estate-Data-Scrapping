# -*- coding: utf-8 -*-
import re

regex = "\(.*\)|\s-\s.*"
get_name = "개포자이(12-2)"
print(re.sub(regex,'', get_name))

name = "현대1차101동~106동"
print(re.split("아파트", name))
name = re.split("아파트", name)[0] + "아파트"
print(name)

import requests # 웹사이트에서 정보를 받아오기 위한 라이브러리

url = "https://realty.daum.net/home/apt/map"
res = requests.get(url)
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, "lxml")


def Test():
    return 4,0,3

result1, result2, result3 = Test()
if result1 == 0 or result2 ==0 or result3 ==0:
    print("hi")

for i in range(1,2):
    print("hi")

char ="세대당 1대 (총 56대)\
지상, 지하 주차장 있음"
print(char.split(')')[0])


llst = []
num = [1,2,10,6]
llst.extend(num)
print(llst)
import pickle
with open("초등학교_리스트.pickle", "rb") as pickle_data: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    print(pickle.load(pickle_data))

with open("중학교_리스트.pickle", "rb") as pickle_data: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    print(len(pickle.load(pickle_data)))

with open("고등학교_리스트.pickle", "rb") as pickle_data: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    print(len(pickle.load(pickle_data)))

with open("도로명_리스트.pickle", "rb") as pickle_data: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    street = pickle.load(pickle_data)

print(street[10])
print(street[11])
print(street[12])

with open("아파트별_데이터_사전.pickle", "rb") as pickle_data: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    street = pickle.load(pickle_data)

print(street)

wee = ['세대수 744세대(총10개동) 저/최고층 12층/12층', '사용승인일 1984년 10월 23일 총주차대수 744대(세대당 1대)', '용적률 165% 건폐율 -', '건설사 한양', '난방 지역난방, 열병합', '관리사무소 02-423-7427', '주소', '서울시 송파구 송파동 151', '서울시 송파구 가락로 192', '면적', '87㎡, 105㎡, 131㎡, 150㎡, 172㎡']
wee2 = re.split(' ',wee[0])

print(wee2[wee2.index('세대수')+1])

info = ['전경', '정문', '단지정보시세/실거래가동호수/공시가격학군정보사진', '평', '단지 정보', '서울시 건축물 대장 정보', '단지 정보', '세대수 744세대(총10개동) 저/최고층 12층/12층', '사용승인일 1984년 10월 23일 총주차대수 744대(세대당 1대)', '용적률 165% 건폐율 -', '건설사 한양', '난방 지역난방, 열병합', '관리사무소 02-423-7427', '주소', '서울시 송파구 송파동 151', '서울시 송파구 가락로 192', '면적', '87㎡, 105㎡, 131㎡, 150㎡, 172㎡', '재건축 정보', '재건축 정보', '사업단계 조합설립인가 선정시공사 -', '예상세대수 -세대 예상배정면적 -', '예상용적률 165% 추진회/조합전화 -', '단지 내 면적별 정보', '87㎡105㎡131㎡150㎡172㎡', '평형 정보', '공급/전용 87.87㎡/64.26㎡(전용률 73%)', '방수/욕실수 2개/1개', '해당면적 세대수 96세대', '현관구조 복도식', '해당면적 매물 매매 1전세 13월세 14단기 0', '매매 16억 5,000 (6,208만원/3.3㎡)', '전세 4억 8,000(1,806만원/3.3㎡)', '월세 3억/100', '전세가율 29%', '관리비 13만 9,753원', '2021년 06월', '연평균 관리비 16만 8,827원', '하절기평균(6~8월) 관리비 13만 8,994원', '동절기평균(12~2월) 관리비 21만 9,338원', '공시가격 해당면적 최고가 9억 2,500', '보유세 약 278만 7,600원', '재산세 268만 5,000원', '종합부동산세 10만 2,600원', '매물가격(중개소 매물 호가) 기준 / 국토교통부 관리비 기준 / 2021.01.01. 공시가격 기준', '단지 내부 시설', '전경', '30m', '© NAVER Corp.', '전경', '단지 전경입니다. 대로변에 위치한 단지이며 주변이 아파트 단지와 주택단지들이며 녹지로 둘러싸여 있으며 교통과 생활의 편리함을 주고 있습니다.', '현재페이지', '1/', '전체페이지', '20', '단지정보 수정제안단지정보 신규요청', '이용약관매물신고운영개인정보처리방침부동산 고객센터', '네이버부동산에서 제공하는 부동산 정보는 각 콘텐츠 제공업체로부터 받는 정보로 참고용입니다. 정보의 정확성이나 신뢰성을 보증하지 않으며, 서비스 이용의 결과에 대해서 어떠한 법적인 책임을 지지 않습니다. 게시된 정보는 무단으로 배포할 수 없습니다.', 'Copyright ⓒ NAVER Corp. All Rights Reserved.']
info2 = []

for i in range(0, len(info)):
    info2.extend(re.split(' ', info[i]))

print(info2)

saedae = info2[info2.index("세대수")+1]
parking = info2[info2.index("총주차대수") + 1] + info2[info2.index("총주차대수") + 2]
yong = info2[info2.index("용적률") + 1]
gun = info2[info2.index("건폐율") + 1]
company = info2[info2.index("건설사") + 1]

print(saedae, parking, yong, gun, company)

with open("도로명_리스트.pickle", "rb") as pickle_data: # profile.pickle 파일을 읽기로 읽어서 profile_with변수에 저장
    street = pickle.load(pickle_data)

print(street)
stree = {}
stree["언주로 103"] = [1,2,3,4,5]
stree["dsdsd"] = [123123123,1231]

print(stree)


with open("도로별_초등학교_이름.pickle", "rb") as pickle_data:
    print(pickle.load(pickle_data))

# with open("도로별_중학교_이름.pickle", "rb") as pickle_data:
#     print(pickle.load(pickle_data))

# with open("도로별_고등학교_이름.pickle", "rb") as pickle_data:
#     print(pickle.load(pickle_data))

st = '인천 중구 인현동 63-2'
if '서울' not in st:
    print("NO")

if '인천' not in st:
    print("YES")

dic = {1:10}
print(dic.get(1))

