#-*-coding:utf-8-*-

"""
   获取依存特征
"""


from nltk.parse.corenlp import CoreNLPDependencyParser
import os
from nltk.parse import stanford
import word_feature
from nltk import WordPunctTokenizer


#对句子进行依存语法分析
def depedency_tokenize(filename):
    data_list=[]
    output = open("corpus/word_to_dependency.txt", "w+", encoding="utf-8")

    with open(filename,"r",encoding="utf-8") as input:
        for  line in input:
            line=line.strip().split("\t")
            L=[]
            # 句法标注
            dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
            parse, = dep_parser.raw_parse(line[-1])
            output.write(str(line[0]) + "\t" + str(line[1]) + "\t" + str(line[2]) + "\t"+str(line[3]) + "\t"+str(line[4]) + "\t")
            for raw in parse.triples():
                output.write(str(raw) + "\t")
                L.append(raw)
            data_list.append([line[0],line[1],line[2],line[3],line[4],L])
            output.write("\n")


    return data_list

#查找某个单词的上一个依赖
"""
@:param
@:sentence: 每个句子的依存结果[(word1,param,word2),.......,]
@:word:要查询的单词
"""
def word_dependence_before(sentence,word):
    # print(sentence)
    root=sentence[0][0][0]
    flag=0
    if word==root:
        return None
    for i in sentence:
        if word == i[2][0]:
            flag=1
            return i[0]
    if flag==0:
        return None

"""
@:param
@:sentence: 每个句子的依存结果[(word1,param,word2),.......,]
@:word:要查询的单词
"""
#查找某个单词的下一个依赖
def word_dependency_after(sentence,word):
    L=[]
    for i in sentence:
        if word==i[0][0]:
            L.append(i[2])
    return L
"""
@:param
@:sentence: 每个句子的依存结果[(word1,param,word2),.......,]
@:word:要查询的单词
"""
#查找某个单词的依赖关系类型
def dependency_type(sentence,word):
    L=[]
    for i  in sentence:
        if  word in i[0] or word in i[2]:
            L.append(i[1])
    L=list(set(L))
    return L
"""
@:param
@:data_list: 每个句子[label,bacteria_1,bacteria_2,[(word1,param,word2),......]]
@:word:要查询的单词
"""
#查找某个单词的前向路径
def word_path(sentence,word):
    L=[]
    while word_dependence_before(sentence,word):
        pre_word=word_dependence_before(sentence,word)[0]
        word=pre_word
        L.insert(0, pre_word)
    return L

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]

"""
#feature_1
#第一个微生物依赖的单词
def DF_P1DW(data_list):
    bacteria_1=data_list[1]
    sentence=data_list[-1]
    L=[]
    pre=word_dependence_before(sentence,bacteria_1)
    nex=word_dependency_after(sentence,bacteria_1)
    if pre and nex:
        L.append("DF_P1DW_"+pre[0])
        for word in nex:
            L.append("DF_P1DW_"+word[0])
    elif pre:
        L.append("DF_P1DW_"+pre[0])
    elif nex:
        for word in nex:
            L.append("DF_P1DW_"+word[0])
    return L


"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_2
#第一个微生物的依赖关系类型
def DF_P1DT(data_list):
    bacteria_1 = data_list[1]
    sentence=data_list[-1]

    return ["DF_P1DT_"+i  for i in dependency_type(sentence,bacteria_1)]
"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]

"""
#feature_3
#第一个微生物的父亲
def DF_P1P(data_list):
    bacteria_1 = data_list[1]
    sentence=data_list[-1]
    if word_dependence_before(sentence,bacteria_1):
        return "DF_P1P_"+word_dependence_before(sentence,bacteria_1)[0]
    else:
        return None


"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_4
#第一个微生物到根节点的路径
def DF_P1ToROOT(data_list):
    bacteria_1 = data_list[1]
    sentence=data_list[-1]
    return word_path(sentence,bacteria_1)

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_5
#第二个微生物依赖的单词
def DF_P2DW(data_list):
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    L = []
    pre = word_dependence_before(sentence, bacteria_2)
    nex = word_dependency_after(sentence, bacteria_2)
    if pre and nex:
        L.append(pre[0])
        for word in nex:
            L.append(word[0])
    elif pre:
        L.append(pre[0])
    elif nex:
        for word in nex:
            L.append(word[0])
    return L

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_6
#第二个微生物的依赖关系类型
def DF_P2DT(data_list):
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    return dependency_type(sentence, bacteria_2)

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_7
#第二个微生物的父亲
def DF_P2P(data_list):
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    if word_dependence_before(sentence, bacteria_2):
        return word_dependence_before(sentence, bacteria_2)[0]
    else:
        return None

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[param,num1,num2],......]]
"""
#feature_8
#第二个微生物到根节点的路径
def DF_P2ToROOT(data_list):
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    return ["DF_P1ToROOT_"+i for i in word_path(sentence, bacteria_2)]

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_9
#两个微生物的公共祖先
def DF_LCS(data_list):
    bacteria_1=data_list[1]
    bacteria_2=data_list[3]
    sentence=data_list[-1]
    L1=word_path(sentence,bacteria_1)
    L2=word_path(sentence,bacteria_2)
    L=[x for x in L1 if x in L2]
    L3=[]
    for i in L:
        L3.append("DF_LCS_"+i)
    return L3
"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_10
#两个微生物是否直接依赖
def DF_directD(data_list):
    bacteria_1=data_list[1]
    bacteria_2=data_list[3]
    sentence=data_list[-1]
    flag=0
    for cp in sentence:
        if (bacteria_1 in cp[0] or bacteria_1 in cp[2]) and (bacteria_2 in cp[0] or bacteria_2 in cp[2]):
            flag=1
            return True
    if flag==0:
        return False

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]

"""
#feature_11
#两个微生物是否依赖同一个单词
def DF_existDSW(data_list):
    L1=DF_P1DW(data_list)
    L2=DF_P2DW(data_list)
    if [x for x in L1 if x in L2]:
        return True
    else:
        return False

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_12
#两个微生物依赖的同一个单词
def DF_DW(data_list):
    L1 = DF_P1DW(data_list)
    L2 = DF_P2DW(data_list)
    return ["DF_DW_"+x for x in L1 if x in L2]

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[param,num1,num2],......]]
"""
#feture_13
#两个微生物之间是否存在路径
def DF_existDP(data_list):
    bacteria_1=data_list[1]
    bacteria_2=data_list[3]
    sentence=data_list[-1]
    L1=word_path(sentence,bacteria_1)
    L2=word_path(sentence,bacteria_2)
    flag=0
    if len(L1)>=len(L2):
        for i in range(len(L2)-1,-1,-1):
            if L2[i] in L1:
                flag=1
                return True
    else:
        for i in range(len(L1)-1,-1,-1):
            if L1[i] in L2:
                flag=1
                return True
    if flag==0:
        return False

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_14
#两个微生物之间的路径
def DF_DP(data_list):
    if DF_existDP(data_list):
        bacteria_1 = data_list[1]
        bacteria_2 = data_list[3]
        sentence=data_list[-1]
        L1 = word_path(sentence,bacteria_1)
        L2 = word_path(sentence,bacteria_2)
        L=[]
        if len(L1)<len(L2):
            for i in L1:
                if i in L2:
                    for j in range(L2.index(i),len(L2)):
                        L.append("DF_DP_"+L2[j])
                    return L
        else:
            for i in L2:
                if i in L1:
                    for j in range(L1.index(i),len(L1)):
                        L.append("DF_DP_"+L1[j])
                    return L
    else:
        return None


"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[word1,param,word2],......]]
"""
#feature_15
#两个微生物之间的路径中的动词
def DF_DPVB(data_list):
    L=DF_DP(data_list)
    sentence=data_list[-1]
    if L:
        L1=[]
        for word in L:
            for cp in sentence:
                if word in cp[0] :
                    if cp[0][1] in ['VB','VBD','VBG','VBN','VBP','VBZ']:
                        L1.append("DF_DPVB_"+word)
        return L1
    else:
        return None

"""
@:param
@:data_list:每个句子[label,bacteria_1,bacteria_2,[[param,num1,num2],......]]
@:tag_list:每个句子的词性标记[label,bacteria_1,bacteria_2,[(param1,param2),.....,]]
"""
#feature_16
#两个微生物之间的路径中动词的数目
def DF_DPVBNum(data_list):
    if DF_DPVB(data_list):
     return len(DF_DPVB(data_list))
    else:
        return 0


def word_to_vec(data_list,word):
    # 字典
    # voclibary = open("data/voc.txt", "w+", encoding="utf-8")
    data_list = list(data_list)
    # [voclibary.write(str(i) + "\n") for i in data_list]

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
def word_list(dependency_list):
    list_1 = []
    for data in dependency_list:
        # print(data)
        df_p1dw = DF_P1DW(data)
        for word in df_p1dw:
            list_1.append(word)

        df_p1dt = DF_P1DT(data)
        for i in df_p1dt:
            list_1.append(i)

        df_p1p = DF_P1P(data)
        if df_p1p!=None:
            list_1.append(df_p1p)

        df_p1toroot = DF_P1ToROOT(data)
        if df_p1toroot:
            for i in df_p1toroot:
                list_1.append(i)

        df_p2dw = DF_P2DW(data)
        for i in df_p2dw:
            list_1.append(i)

        df_p2dt = DF_P2DT(data)
        for i in df_p2dt:
            list_1.append(i)

        df_p2p = DF_P2P(data)
        if df_p2p!=None:
            list_1.append(df_p2p)

        df_p2toroot = DF_P2ToROOT(data)
        if df_p2toroot:
            for i in df_p2toroot:
                list_1.append(i)

        df_lcs = DF_LCS(data)
        if df_lcs:
            for i in df_lcs:
                list_1.append(i)

        df_directD = DF_directD(data)


        df_existdsw = DF_existDSW(data)


        df_dw = DF_DW(data)
        if df_dw:
            for i in df_dw:
                list_1.append(i)

        df_existdp = DF_existDP(data)


        df_dp = DF_DP(data)
        if df_dp:
            for i in df_dp:
                list_1.append(i)

        df_dpvb = DF_DPVB(data)
        if df_dpvb:
            for i in df_dpvb:
                list_1.append(i)

        df_dpvbnum = DF_DPVBNum(data)


    return  list_1

def feature_vec(dependency_list,list_1):
    output = open("data/dependency_feature_2.txt", "w+", encoding="utf-8")
    for data in dependency_list:
        output.write(str(data[0]) + "\t")
        L=[]
        df_p1dw = DF_P1DW(data)
        for word in df_p1dw:
            L.append(word)

        df_p1dt = DF_P1DT(data)
        for i in df_p1dt:
            L.append(i)

        df_p1p = DF_P1P(data)
        L.append(df_p1p)


        df_p1toroot = DF_P1ToROOT(data)
        if df_p1toroot:
            for i in df_p1toroot:
                L.append(i)


        df_p2dw = DF_P2DW(data)
        for i in df_p2dw:
            L.append(i)


        df_p2dt = DF_P2DT(data)
        for i in df_p2dt:
            L.append(i)


        df_p2p = DF_P2P(data)
        L.append(df_p2p)

        df_p2toroot = DF_P2ToROOT(data)
        if df_p2toroot:
            for i in df_p2toroot:
                L.append(i)


        df_lcs = DF_LCS(data)
        if df_lcs:
            for i in df_lcs:
                L.append(i)

        df_dw = DF_DW(data)
        if df_dw:
            for i in df_dw:
                L.append(i)

        df_dp = DF_DP(data)
        if df_dp:
            for i in df_dp:
                L.append(i)

        df_dpvb = DF_DPVB(data)
        if df_dpvb:
            for i in df_dpvb:
                L.append(i)
        feature=word_to_vec(list_1,L)
        [output.write(str(i)+"\t") for i in feature]

        df_directD = DF_directD(data)
        if df_directD:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")

        df_existdsw = DF_existDSW(data)
        if df_existdsw:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")

        df_existdp = DF_existDP(data)
        if df_existdp:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")

        df_dpvbnum = DF_DPVBNum(data)
        output.write(str(df_dpvbnum) + "\n")




if __name__=="__main__":
    data_list=depedency_tokenize("corpus/postive.txt")
    list_1=word_list(data_list)
    feature_vec(data_list,list_1)


