#-*-coding:utf-8-*-

"""
    获取词性特征
"""

import word_feature
import  nltk,process,cross_validataion,bash_shell,evaluate
#词性标注
def pos_tokizen(filename):
    input = word_feature.sentence_to_word(filename)
    out_put=open("corpus/nltk_opennlp.txt","w+",encoding="utf-8")
    data_list = []
    for line in input:
        L = []
        sentences = nltk.pos_tag(line[-1])
        for raw in sentences:
            L.append(raw)
            out_put.write(str(raw[0])+"_"+str(raw[1])+"\t")
        out_put.write("\n")
        data_list.append([line[0], line[1], line[2],line[3],line[4], L])
    print(len(data_list))
    return data_list
#查询单词的位置
def word_index(word,data_list):
    sentence_tag=data_list[-1]
    for index in range(len(sentence_tag)):
        if word  in sentence_tag[index]:
            return index

#第一个微生物前的单词个数
def word_P1Before(data_list):
    bacteria_1=data_list[1]
    index_1=word_index(bacteria_1,data_list)
    if index_1==0:
        return 0
    elif index_1==1:
        return 1
    else:
        return 2
#第二个微生物后的单词个数
def word_P2After(data_list):
    bacteria_2=data_list[3]
    sentence_tag=data_list[-1]
    index_2=word_index(bacteria_2,data_list)
    if index_2==len(sentence_tag)-1:
        return 0
    elif index_2==len(sentence_tag)-2:
        return 1
    else:
        return 2

#微生物之间单词个数：
def word_P1P2(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    index_1 = word_index(bacteria_1, data_list)
    index_2 = word_index(bacteria_2, data_list)
    if index_1+1==index_2:
        return 0
    elif index_1+2==index_2:
        return 1
    elif index_1+3==index_2:
        return 2
    else:
        return 3


#feature_1
#第一个微生物前的第一个单词的词性
def POSF_P1B1(data_list):
    bacteria_1=data_list[1]
    sentence_tag=data_list[-1]
    if word_P1Before(data_list)!=0:
        index_1=word_index(bacteria_1,data_list)
        return "POSF_P1B1_"+sentence_tag[index_1-1][1]
    else:
        return None

#feature_2
#第一个微生物前的第二个单词的词性
def POSF_P1B2(data_list):
    bacteria_1 = data_list[1]
    sentence_tag = data_list[-1]
    if word_P1Before(data_list) == 2:
        index_1 = word_index(bacteria_1, data_list)
        return "POSF_P1B2_"+sentence_tag[index_1 - 2][1]
    else:
        return None

#feature_3
#第二个微生物后的第一个单词的词性
def POSF_P2A1(data_list):
    bacteria_2 = data_list[3]
    sentence_tag = data_list[-1]
    if word_P2After(data_list)!=0:
        index_2=word_index(bacteria_2,data_list)
        return "POSF_P2A1_"+sentence_tag[index_2+1][1]
    else:
        return None


#feature_4
#第二个微生物后的第二个单词的词性
def POSF_P2A2(data_list):
    bacteria_2 = data_list[3]
    sentence_tag = data_list[-1]
    if word_P2After(data_list) == 2:
        index_2 = word_index(bacteria_2, data_list)
        return "POSF_P2A2_"+sentence_tag[index_2 + 2][1]
    else:
        return None

#feature_5
#微生物实体对之间是否存在其他单词
def POSF_PNULL(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    index_1 = word_index(bacteria_1, data_list)
    index_2 = word_index(bacteria_2, data_list)
    if index_2==index_1+1:
        return False
    else:
        return True

#feature_6
#微生物实体对之间的第一个单词的词性
def POSF_PF(data_list):
    bacteria_1 = data_list[1]
    sentence_tag = data_list[-1]
    index_1 = word_index(bacteria_1, data_list)
    if word_P1P2(data_list)!=0:
        return "POSF_PF_"+sentence_tag[index_1+1][1]
    else:
        return None


#feature_7
#微生物实体对之间的最后一个单词的词性
def POSF_PL(data_list):
    bacteria_2 = data_list[3]
    sentence_tag = data_list[-1]
    index_2 = word_index(bacteria_2, data_list)
    if word_P1P2(data_list) != 0:
        return "POSF_PL_"+sentence_tag[index_2 - 1][1]
    else:
        return None


#feature_8
#微生物实体对之间除去第一个和最后一个单词的所有单词的词性
def POSF_PO(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    sentence_tag = data_list[-1]
    index_1=word_index(bacteria_1,data_list)
    index_2=word_index(bacteria_2,data_list)
    feature_list=[]
    if word_P1P2(data_list)==3:
        for i in range(index_1+2,index_2-1):
            word="POSF_PO_"+str(i)+"_"+sentence_tag[i][1]
            feature_list.append(word)
    return feature_list

def word_to_vec(data_list,word):
    # 字典
    voclibary = open("data/voc.txt", "w+", encoding="utf-8")
    data_list = list(data_list)
    [voclibary.write(str(i) + "\n") for i in data_list]

    if type(word) != list:
        word_list = []
        word_list.append(word)
    else:
        word_list = word
    return_vec = [0] * len(data_list)
    # 查字典
    if word_list:
        for j in word_list:
            for i in range(len(data_list)):
                if j == data_list[i]:
                    return_vec[i] = 1
                    break
    return return_vec

def word_list(tag_list):
    out_feature=open("feature/pos_feature.txt","w+",encoding="utf-8")
    list_1 = []
    for data_list in tag_list:
        out_feature.write(str(data_list[0])+"\t"+str(data_list[1])+"\t"+str(data_list[3])+"\t")
        posf_p1b1 = POSF_P1B1(data_list)
        if posf_p1b1!=None:
            list_1.append(posf_p1b1)
        posf_p1b2 = POSF_P1B2(data_list)
        if posf_p1b2!=None:
            list_1.append(posf_p1b2)
        posf_p2a1 = POSF_P2A1(data_list)
        if posf_p2a1!=None:
            list_1.append(posf_p2a1)
        posf_p2a2 = POSF_P2A2(data_list)
        if posf_p2a2!=None:
            list_1.append(posf_p2a2)
        posf_pnull = POSF_PNULL(data_list)

        posf_pf = POSF_PF(data_list)
        if posf_pf!=None:
            list_1.append(posf_pf)
        posf_pl = POSF_PL(data_list)
        if posf_pl!=None:
            list_1.append(posf_pl)
        posf_po = POSF_PO(data_list)
        if posf_po:
            for i in posf_po:
                list_1.append(i)
        out_feature.write(str(posf_p1b1)+"\t")
        out_feature.write(str(posf_p1b2) + "\t")
        out_feature.write(str(posf_p2a1) + "\t")
        out_feature.write(str(posf_p2a2) + "\t")
        out_feature.write(str(posf_pnull) + "\t")
        out_feature.write(str(posf_pf) + "\t")
        out_feature.write(str(posf_pl) + "\t")
        out_feature.write(str(posf_po) + "\n")
    return  list_1

def feature_vec(tag_list,list_1):
    output = open("data/pos_feature.txt", "w+", encoding="utf-8")
    for data_list in tag_list:
        L=[]
        output.write(str(data_list[0]) + "\t" )
        posf_p1b1 = POSF_P1B1(data_list)
        L.append(posf_p1b1)

        posf_p1b2 = POSF_P1B2(data_list)
        L.append(posf_p1b2)

        posf_p2a1 = POSF_P2A1(data_list)
        L.append(posf_p2a1)

        posf_p2a2 = POSF_P2A2(data_list)
        L.append(posf_p2a2)

        posf_pf = POSF_PF(data_list)
        L.append(posf_pf)


        posf_pl = POSF_PL(data_list)
        L.append(posf_pl)


        posf_po = POSF_PO(data_list)
        if posf_po:
            for i in posf_po:
                L.append(i)

        feature=word_to_vec(list_1,L)
        [output.write(str(i) + "\t") for i in feature]

        posf_pnull = POSF_PNULL(data_list)
        if posf_pnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        output.write("\n")


def word():
    tag_list = pos_tokizen("corpus/postive.txt")
    list_1 = word_list(tag_list)
    feature_vec(tag_list, list_1)
    cross_validataion.cross_validataion("data/pos_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("pos_feature")


if __name__=="__main__":
    process.precessing()
    word()













