from __future__ import print_function
import re
import sys
import pickle

f = open("icd10data2.txt", 'r')
ft = open("obs.txt", "w")
# f=open("icdtest.txt","r")

icd10data = []
pattern = re.compile(r'([\'\"])(.*?)\1')
while 1:
    line = f.readline()
    if not line:
        break
    print(line, file= ft)
    print('#######', file=ft)
    sin_phrase = []
    ori = []
    syn = []
    tmp_item_list = re.findall(pattern, line)
    if tmp_item_list:
        ori.append(tmp_item_list[0][1])
    sin_phrase.append(ori)
    if len(tmp_item_list) > 1:
        for item in tmp_item_list[1:]:
            syn.append(item[1])
    sin_phrase.append(syn)
    # print(sin_phrase)
    icd10data.append(sin_phrase)
pickle.dump(icd10data, open("py_icd10data4.txt", "wb"))
