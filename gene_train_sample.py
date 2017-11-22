import random
import pickle
import sys

# datalist=pickle.load(open("py_icd10data.txt","rb"))
datalist = pickle.load(open("py_icd10data4.txt", "rb"))
upper_bound = len(datalist)
f = open("train4.tsv", "w")
kase = 0
while kase < 20000:
    idx = random.randint(0, upper_bound - 1)
    if datalist[idx][0] and datalist[idx][1]:
        tlen = len(datalist[idx][1])
    idx2 = random.randint(0, tlen - 1)
    idx3 = random.randint(0, upper_bound - 1)
    if idx3 != idx:
        tlen = len(datalist[idx3][1])
        if tlen:
            idx4 = random.randint(0, tlen - 1)
            f.write("1" + "\t" + "\"" + str(datalist[idx][0][0]) + "\"" + "\t" + "\"" + str(
                datalist[idx][1][idx2]) + "\"" + "\n")
            f.write("0" + "\t" + "\"" + str(datalist[idx][0][0]) + "\"" + "\t" + "\"" + str(
                datalist[idx3][1][idx4]) + "\"" + "\n")
            kase = kase + 1
f.close()
#	            print('1\t%s\t%s\n' % (datalist[idx][0][0],datalist[idx][1][idx2]),file=f)
#	            print('0\t%s\t%s\n' % (datalist[idx][0][0],datalist[idx3][1][idx4]),file=f)
