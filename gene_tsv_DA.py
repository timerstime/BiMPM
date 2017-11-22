import random
import pickle
import sys

# datalist=pickle.load(open("py_icd10data.txt","rb"))
def gene_file(filename,dom_class):
    datalist = pickle.load(open(filename, "rb"))
    upper_bound = len(datalist)
    f = open("{}.tsv".format(filename.split(".")[0]), "a")
    kase = 0
    print(upper_bound)
    for idx in range(upper_bound):
        # idx = random.randint(0, upper_bound - 1)
        print (datalist[idx][1])
        print(idx)
        if datalist[idx][0]==[] or datalist[idx][1]==[]:
            continue
        tlen1 = len(datalist[idx][1])
        tlen0 = len(datalist[idx][0])
        print("len :",tlen1)
        idx2 = random.randint(0, tlen1 - 1)
        print("idx2:",idx2)
        idx3 = random.randint(0, upper_bound - 1)
        if idx3 != idx:
            tlen = len(datalist[idx3][1])
            if tlen:
                idx4 = random.randint(0, tlen - 1)
                print("hhhh:",datalist[idx][1][idx2])
                f.write(dom_class+"\t"+"1" + "\t" + "\"" + str(datalist[idx][0][0]) + "\"" + "\t" + "\"" + str(
                    datalist[idx][1][idx2]) + "\"" + "\n")
                f.write(dom_class+"\t"+"0" + "\t" + "\"" + str(datalist[idx][0][0]) + "\"" + "\t" + "\"" + str(
                    datalist[idx3][1][idx4]) + "\"" + "\n")
                kase = kase + 1
    f.close()
    #	            print('1\t%s\t%s\n' % (datalist[idx][0][0],datalist[idx][1][idx2]),file=f)
    #	            print('0\t%s\t%s\n' % (datalist[idx][0][0],datalist[idx3][1][idx4]),file=f)
