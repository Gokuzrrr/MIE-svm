#-*-coding:utf-8-*-

"""
    计算结果
"""

import numpy as np
def evaluate(filename):
    p_list = []
    r_list = []
    f_list = []
    output = open("evaluate/" + filename + "_evaluate.txt", "w+", encoding="utf-8")
    for k in [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8]:
        print(k)
        for j in range(10):
            fp1 = open("data/word_feature_result_" + str(k) + "_" + str(j) + ".txt", "r", encoding="utf-8")
            fp2 = open("data/test_" + str(j) + ".txt", "r", encoding="utf-8")
            astr = []
            bstr = []
            TPFP = 0
            TPFN = 0
            TP = 0
            for eachline in fp1.readlines():
                eachline = eachline.strip().split()
                astr.append(eachline[0])
            for line in fp2.readlines():
                line = line.strip().split("\t")
                bstr.append(line[0])

            for s1 in astr:
                if s1 == "1":
                    TPFP += 1
            for s2 in bstr:
                if s2 == "1":
                    TPFN += 1

            for i in range(len(astr)):
                if astr[i] == "1" and bstr[i] == "1":
                    TP += 1


            P = TP / (TPFP + 0.0)
            R = TP / (TPFN + 0.0)
            F = 2 * P * R / (P + R)

            # print('P: ', "%.3f%%" % (P * 100))
            # print('R: ', "%.3f%%" % (R * 100))
            # print('F: ', "%.3f%%" % (F * 100))
            p_list.append(P)
            r_list.append(R)
            f_list.append(F)
        output.write("c="+str(k)+"\t"+str(np.array(p_list).mean())+"\t"+str(np.array(r_list).mean())+"\t"+str(2 * np.array(p_list).mean() * np.array(r_list).mean() / (np.array(r_list).mean() + np.array(p_list).mean()))+"\n")
        print(np.array(p_list).mean())
        print(np.array(r_list).mean())
        print(2 * np.array(p_list).mean() * np.array(r_list).mean() / (np.array(r_list).mean() + np.array(p_list).mean()))
if __name__=="__main__":
    # evaluate("word_feature_result")
    pass