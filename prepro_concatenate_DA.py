import pickle
import random
from gene_tsv_DA import gene_file
th = 0.7
thh = th+0.15
datalist1 = pickle.load(open("py_coref.txt", "rb"))
datalist0 = pickle.load(open("py_icd10data4.txt", "rb"))
train_list=[]
dev_list_0=[]
dev_list_1=[]
test_list_0=[]
test_list_1=[]
num0=len(datalist0)
num1=len(datalist1)

for item0 in datalist0[:int(num0*th)]:
    train_list.append(item0)
pickle.dump(train_list, open("train_DA.txt", "wb"))
gene_file("train_DA.txt","0")

for item1 in datalist1[:int(num1*th)]:
    train_list.append(item1)
pickle.dump(train_list, open("train_DA.txt", "wb"))
gene_file("train_DA.txt","1")

for item0 in datalist0[int(num0*th):int(num0*thh)]:
    dev_list_0.append(item0)
pickle.dump(dev_list_0, open("dev_0_DA.txt", "wb"))
gene_file("dev_0_DA.txt","0")

for item1 in datalist1[int(num1*th):int(num1*thh)]:
    dev_list_1.append(item1)
pickle.dump(dev_list_1, open("dev_1_DA.txt", "wb"))
gene_file("dev_1_DA.txt","1")

for item0 in datalist0[int(num0*thh):]:
    test_list_0.append(item0)
pickle.dump(test_list_0, open("test_0_DA.txt", "wb"))
gene_file("test_0_DA.txt","0")

for item1 in datalist1[int(num1*thh):]:
    test_list_1.append(item1)
pickle.dump(test_list_1, open("test_1_DA.txt", "wb"))
gene_file("test_1_DA.txt","1")


#pickle.dump(datalist, open("py_mixed.txt", "wb"))


