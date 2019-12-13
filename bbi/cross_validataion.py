#-*-coding:utf-8-*-

"""
    十折交叉验证
"""

#分层抽样
from  sklearn.model_selection import KFold
def cross_validataion(filename):
    postive_label=[]
    postive_feature=[]
    negative_label=[]
    negative_feature=[]
    with open(filename, "r", encoding="utf-8") as input_1:
        for line in input_1:
            line = line.strip().split("\t")
            if line[0]=="1":
                postive_label.append(int(line[0]))
                L = []
                for i in line[1:]:
                    L.append(int(i))
                postive_feature.append(L)
            else:
                negative_label.append(int(line[0]))
                L = []
                for i in line[1:]:
                    L.append(int(i))
                negative_feature.append(L)

    skf=KFold(n_splits=10,shuffle=True,random_state=0)
    j=0
    for train,test in  skf.split(postive_feature,postive_label):
        print(j)
        train_index=train
        test_index=test
        train_file=open("data/train_"+str(j)+".txt","w+",encoding="utf-8")
        test_file = open("data/test_" + str(j) + ".txt", "w+", encoding="utf-8")
        j+=1
        for i in train_index:
            f=postive_feature[i]
            train_file.write(str(postive_label[i])+"\t")
            for index in range(len(f)):
                if f[index]:
                    train_file.write(str(index)+":"+str(f[index])+"\t")
            train_file.write("\n")
        for k in test_index:
            f=postive_feature[k]
            test_file.write(str(postive_label[k])+"\t")
            for index in range(len(f)):
                if f[index]:
                    test_file.write(str(index)+":"+str(f[index])+"\t")
            test_file.write("\n")
    num=0
    for train,test in  skf.split(negative_feature,negative_label):
        print(num)
        train_index=train
        test_index=test
        train_file=open("data/train_"+str(num)+".txt","a+",encoding="utf-8")
        test_file = open("data/test_" + str(num) + ".txt", "a+", encoding="utf-8")
        num+=1
        for i in train_index:
            f=negative_feature[i]
            train_file.write(str(negative_label[i])+"\t")
            for index in range(len(f)):
                if f[index]:
                    train_file.write(str(index)+":"+str(f[index])+"\t")
            train_file.write("\n")
        for k in test_index:
            f=negative_feature[k]
            test_file.write(str(negative_label[k])+"\t")
            for index in range(len(f)):
                if f[index]:
                    test_file.write(str(index)+":"+str(f[index])+"\t")
            test_file.write("\n")

if __name__=="__main__":
    cross_validataion("data/word_pos_logistic_feature.txt")
    pass
