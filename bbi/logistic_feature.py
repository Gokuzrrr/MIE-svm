#-*-coding:utf-8-*-

"""
    获取逻辑特征
"""

import word_feature
import nltk,pos_feature
import process
def pos_tokizen(filename):
    input = word_feature.sentence_to_word(filename)
    output =open("corpus/word_to_pos.txt", "w+", encoding="utf-8")
    data_list = []
    for line in input:
        L = []
        sentences = nltk.pos_tag(line[-1])
        output.write(str(line[0]) + "\t" + str(line[1]) + "\t" + str(line[2]) + "\t"+str(line[3]) + "\t"+ str(line[4]) + "\t")
        for raw in sentences:
            output.write(str(raw) + "\t")
            L.append(raw)
        output.write("\n")
        data_list.append([line[0], line[1], line[2],line[3],line[4], L])
    return data_list
#feature_1
#微生物实体对之间的单词数目
def LF_distance(data_list):
    bacteria_1=data_list[1]
    bacteria_2=data_list[3]
    index_1=pos_feature.word_index(bacteria_1,data_list)
    index_2=pos_feature.word_index(bacteria_2,data_list)
    return index_2-index_1-1


#feature_2
#微生物实体对之间其他蛋白质个数
def LF_bacteriaNum(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    index_1 = bacteria_1.split("T")[1]
    index_2 = bacteria_2.split("T")[1]
    count=int(index_2)-int(index_1)-1
    return count
#feature_2

def LF_insert(data_list):
    bacteria_1 = data_list[2]
    bacteria_2 = data_list[4]
    if bacteria_1 in bacteria_2 or bacteria_2 in bacteria_1:
        return 1
    else:
        return 0


#feature_3
#微生物实体对之间是否存在动词
def LF_verbBT(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    sentence_tag = data_list[-1]
    index_1 = pos_feature.word_index(bacteria_1, data_list)
    index_2 = pos_feature.word_index(bacteria_2, data_list)
    flag=0
    for i in range(index_1+1,index_2):
        if sentence_tag[i][1] in ['VB','VBD','VBG','VBN','VBP','VBZ']:
            flag=1
            return True
    if flag==0:
        return False


#feature_4
#微生物实体对之间的标点数目
def  pumcNum(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    sentence_tag = data_list[-1]
    index_1 = pos_feature.word_index(bacteria_1, data_list)
    index_2 = pos_feature.word_index(bacteria_2, data_list)
    count=0
    for i in range(index_1 + 1, index_2):
       if sentence_tag[i][0] in [',','.',':',';']:
            count+=1
    return count


def feature_vec(data):
        output = open("data/logistic_feature.txt", "w+", encoding="utf-8")
        for data_list in data:
            output.write(str(data_list[0]) + "\t"+str(data_list[1])+"\t"+str(data_list[3])+"\t")
            lf_distance = LF_distance(data_list)
            output.write(str(lf_distance) + "\t")
            lf_bacterianum=LF_bacteriaNum(data_list)
            output.write(str(lf_bacterianum) + "\t")
            lf_insert = LF_insert(data_list)
            output.write(str(lf_insert) + "\t")
            lf_verbbt = LF_verbBT(data_list)
            if lf_verbbt:
                output.write("1" + "\t")
            else:
                output.write("0" + "\t")
            pumcnum = pumcNum(data_list)
            output.write(str(pumcnum) + "\n")


if __name__=="__main__":
    filename ="corpus/postive.txt"
    process.precessing()
    data_list=pos_tokizen(filename)
    feature_vec(data_list)




