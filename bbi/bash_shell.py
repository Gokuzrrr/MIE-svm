#-*-coding:utf-8-*-

"""
    调用lib-svm-3.22
"""

import os
def bash_shell():
    for j in [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8]:
        for i in range(10):
            os.system("./libsvm-3.22/windows/svm-train.exe -h 0 -t 0 -c "+str(j)+" data/train_"+str(i)+".txt  data/train_"+str(j)+"_"+str(i)+"_model.txt")
            os.system("./libsvm-3.22/windows/svm-predict.exe "+"data/test_"+str(i)+".txt  data/train_"+str(j)+"_"+str(i)+"_model.txt data/word_feature_result_"+str(j)+"_"+str(i)+".txt")