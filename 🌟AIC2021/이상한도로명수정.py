# -*- coding: utf-8 -*-

import pickle

with open("도로별_중학교_이름.pickle", "rb") as pickle_data:
    mid_data = pickle.load(pickle_data)

with open("도로별_고등학교_이름.pickle", "rb") as pickle_data:
    high_data = pickle.load(pickle_data)

change_needed = ['상원길 15', '신남1길 16', '오현로 58', '우현로 76', '현충로 50']
delete_mid = []
delete_high = []
# print(mid_data)
# print(len(mid_data))
# print(mid_data.keys())
# print(mid_data.values())

street = mid_data.keys()

street = list(street)
mid = mid_data.values()

mid = list(mid)
print(mid[0])



for name in change_needed:
    if type(mid_data[name]) == int:
        print(name + "is int error")
        pass
    else:
        delete_mid.extend(mid_data[name])
        delete_high.extend(high_data[name])

        del mid_data[name]
        del high_data[name]


delete_mid = set(delete_mid)
delete_mid = list(delete_mid)

delete_high = set(delete_high)
delete_high = list(delete_high)

print(delete_mid)
print(delete_high)

with open("중학교_리스트.pickle", "rb") as pickle_data:
    mid_list = pickle.load(pickle_data)

with open("고등학교_리스트.pickle", "rb") as pickle_data:
    high_list = pickle.load(pickle_data)

for i in range(0, len(delete_mid)):
    if delete_mid[i] in mid_list:
        mid_list.pop(mid_list.index(delete_mid[i]))
    else:
        print(delete_mid[i])

print(delete_mid[4] in mid_list)

for i in range(0, len(delete_high)):
    if delete_high[i] in high_list:
        high_list.pop(high_list.index(delete_high[i]))
    else:
        print(delete_high[i])

print(delete_high[4] in high_list)

with open("Final_중학교_리스트.pickle", "wb") as pickle_data:
    pickle.dump(mid_list, pickle_data)

with open("Final_고등학교_리스트.pickle", "wb") as pickle_data:
    pickle.dump(high_list, pickle_data)