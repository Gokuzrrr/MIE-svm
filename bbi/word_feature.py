#-*-coding:utf-8-*-

from nltk.tokenize import  WordPunctTokenizer
import cross_validataion
import process,evaluate,bash_shell

#将句子划分为单词
def sentence_to_word(filename):
    test_list=[]
    output=open("corpus/sentence_to_word.txt","w+",encoding="utf-8")
    with open(filename,"r",encoding="utf-8") as input_data:
        for each_line in input_data:
            each_line_split=each_line.strip().split("\t")
            sentence=each_line_split[-1]
            label=each_line_split[0]
            bacteria1=each_line_split[1]
            name_1=each_line_split[2]
            bacteria2=each_line_split[3]
            name_2=each_line_split[4]
            words=WordPunctTokenizer().tokenize(sentence)
            output.write(str(label)+"\t"+str(bacteria1)+"\t"+str(name_1)+"\t"+str(bacteria2)+"\t"+str(name_2)+"\t")
            for word in words:
                output.write(str(word)+"\t")
            output.write("\n")
            test_list.append([label,bacteria1,name_1,bacteria2,name_2,words])
    print(len(test_list))
    return test_list

#feature_1
#微生物实体对之间的第一个单词
def WF_PF(data_list):
    if not WF_NULL(data_list):
        bacteria_1=data_list[1]
        sentence=data_list[-1]
        index_1=sentence.index(bacteria_1)
        return "WF_PF_"+sentence[index_1+1]
    else:
        return None
#feature_2
#微生物实体对之间的最后一个单词
def WF_PL(data_list):
    if not WF_NULL(data_list):
        bacteria_2 = data_list[3]
        sentence = data_list[-1]
        index_2 = sentence.index(bacteria_2)
        return "WF_PL_"+sentence[index_2-1]
    else:
        return None
#feature_3
#微生物实体对之间除了第一个单词和最后一个单词的其他单词
def WF_PO(data_list):
    if not WF_NULL(data_list):
        if not WF_Pone(data_list):
            bacteria_1 = data_list[1]
            bacteria_2 = data_list[3]
            sentence = data_list[-1]
            index_1 = sentence.index(bacteria_1)
            index_2=sentence.index(bacteria_2)
            word_list=[]
            if index_1+3==index_2:
                return None
            else:
                j=1
                for i in range(index_1+2,index_2-1):
                    word=sentence[i]
                    word="WF_PO_"+str(j)+"_"+word
                    j+=1
                    word_list.append(word)
                return word_list
        else:
            return None
    else:
        return None
#feature_4
#微生物实体间仅存在一个单词
def WF_Pone(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    index_1 = sentence.index(bacteria_1)
    index_2 = sentence.index(bacteria_2)
    if index_1+2==index_2:
        return True
    else:
        return False
#feature_5
#微生物实体间不存在任何单词
def WF_NULL(data_list):
    bacteria_1 = data_list[1]
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    index_1 = sentence.index(bacteria_1)
    index_2 = sentence.index(bacteria_2)
    if index_1 + 1 == index_2:
        return True
    else:
        return False
#feature_6
#第一个微生物前的第一个单词
def WF_P1B1(data_list):
    if not WF_P1BNULL(data_list):
        bacteria_1 = data_list[1]
        sentence = data_list[-1]
        index_1 = sentence.index(bacteria_1)
        return "WF_P1B1_"+sentence[index_1-1]
    else:
        return None

#feature_7
#第一个微生物前的第二个单词
def WF_P1B2(data_list):
    if not WF_P1BNULL(data_list):
        if not WF_P1BOne(data_list):
            bacteria_1 = data_list[1]
            sentence = data_list[-1]
            index_1 = sentence.index(bacteria_1)
            return "WF_P1B2_"+sentence[index_1 - 2]
        else:
            return None
    else:
        return None

#feture_8
#第二个微生物后的第一个单词
def WF_P2A1(data_list):
    if not WF_P2ANULL(data_list):
        bacteria_2 = data_list[3]
        sentence = data_list[-1]
        index_2 = sentence.index(bacteria_2)
        return "WF_P2A1_"+sentence[index_2 +1]
    else:
        return None

#feature_9
#第二个微生物后的第二个单词
def WF_P2A2(data_list):
    if not WF_P2ANULL(data_list):
        if not WF_P2AOne(data_list):
            bacteria_2 = data_list[3]
            sentence = data_list[-1]
            index_2 = sentence.index(bacteria_2)
            return "WF_P2A2_"+sentence[index_2 + 2]
        else:
            return None
    else:
        return None

#feature_10
#第一个微生物前仅存在一个单词
def WF_P1BOne(data_list):
    bacteria_1 = data_list[1]
    sentence = data_list[-1]
    index_1 = sentence.index(bacteria_1)
    if index_1==1:
        return True
    else:
        return False

#feature_11
#第一个微生物之前不存在单词
def WF_P1BNULL(data_list):
    bacteria_1 = data_list[1]
    sentence = data_list[-1]
    index_1 = sentence.index(bacteria_1)
    if index_1 == 0:
        return True
    else:
        return False

#feature_12
#第二个微生物后仅存在一个单词
def WF_P2AOne(data_list):
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    index_2 = sentence.index(bacteria_2)
    if index_2 == len(sentence)-2:
        return True
    else:
        return False

#feature_13
#第二个微生物后不存在单词
def WF_P2ANULL(data_list):
    bacteria_2 = data_list[3]
    sentence = data_list[-1]
    index_2 = sentence.index(bacteria_2)
    if index_2 == len(sentence)-1:
        return True
    else:
        return False

def word_to_vec(data_list,word):
    #字典
    voclibary=open("data/voc.txt","w+",encoding="utf-8")
    data_list=list(data_list)
    [voclibary.write(str(i)+"\n") for i in data_list]

    if type(word) != list:
        word_list=[]
        word_list.append(word)
    else:
        word_list=word
    return_vec=[0]*len(data_list)
    #查字典
    if word_list:
        for j in word_list:
            for i in range(len(data_list)):
                if j==data_list[i]:
                    return_vec[i]=1
                    break
    return return_vec

def word_list(postive_list):
    list_1 = []
    feature_file = open("feature/word_feature.txt", "w+", encoding="utf-8")
    for data_list in postive_list:
        # 词汇特征
        list_1.append("MW1_" + data_list[2])
        list_1.append("MW2_" + data_list[4])
        wf_pf = WF_PF(data_list)
        if wf_pf!=None:
            list_1.append(wf_pf)
        wf_pl = WF_PL(data_list)
        if wf_pl!=None:
            list_1.append(wf_pl)
        wf_po = WF_PO(data_list)
        if wf_po:
            for i in wf_po:
                list_1.append(i)
        wf_null = WF_NULL(data_list)
        wf_p1b1 = WF_P1B1(data_list)
        if wf_p1b1!=None:
            list_1.append(wf_p1b1)
        wf_p1b2 = WF_P1B2(data_list)
        if wf_p1b2!=None:
            list_1.append(wf_p1b2)
        wf_p2a1 = WF_P2A1(data_list)
        if wf_p2a1!=None:
            list_1.append(wf_p2a1)
        wf_p2a2 = WF_P2A2(data_list)
        if wf_p2a2!=None:
            list_1.append(wf_p2a2)
        wf_p1bone = WF_P1BOne(data_list)
        wf_p1bnull = WF_P1BNULL(data_list)
        wf_p2aone = WF_P2AOne(data_list)
        wf_P2anull = WF_P2ANULL(data_list)
        feature_file.write(str(data_list[0])+"\t"+str(data_list[1])+"\t"+str(data_list[3])+"\t")
        feature_file.write(str(wf_pf)+"\t")
        feature_file.write(str(wf_pl)+"\t")
        feature_file.write(str(wf_po)+"\t")
        feature_file.write(str(wf_null)+"\t")
        feature_file.write(str(wf_p1b1)+"\t")
        feature_file.write(str(wf_p1b2)+"\t")
        feature_file.write(str( wf_p2a1)+"\t")
        feature_file.write(str(wf_p2a2)+"\t")
        feature_file.write(str(wf_p1bone)+"\t")
        feature_file.write(str(wf_p1bnull)+"\t")
        feature_file.write(str(wf_p2aone)+"\t")
        feature_file.write(str(wf_P2anull)+"\n")

    return list_1

def doc_vec(postive_list,list_1):
    output = open("data/word_feature.txt", "w+", encoding="utf-8")
    for data_list in postive_list:
        output.write(str(data_list[0]) + "\t" )
        L=[]
        L.append("MW1_" + data_list[2])
        L.append("MW2_" + data_list[4])
        wf_pf = WF_PF(data_list)
        L.append(wf_pf)

        wf_pl = WF_PL(data_list)
        L.append(wf_pl)

        wf_po = WF_PO(data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)

        wf_p1b1 = WF_P1B1(data_list)
        L.append(wf_p1b1)


        wf_p1b2 = WF_P1B2(data_list)
        L.append(wf_p1b2)


        wf_p2a1 = WF_P2A1(data_list)
        L.append(wf_p2a1)


        wf_p2a2 = WF_P2A2(data_list)
        L.append(wf_p2a2)


        feature = word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        wf_pone = WF_Pone(data_list)

        if wf_pone:
            output.write(str(1)+"\t")
        else:
            output.write(str(0) + "\t")


        wf_null = WF_NULL(data_list)

        if wf_null:
            output.write(str(1)+"\t")
        else:
            output.write(str(0) + "\t")


        wf_p1bone = WF_P1BOne(data_list)

        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        wf_p1bnull = WF_P1BNULL(data_list)

        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        wf_p2aone = WF_P2AOne(data_list)

        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        wf_P2anull = WF_P2ANULL(data_list)

        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        output.write("\n")

def word(filename):
    postive_list = sentence_to_word(filename)
    list_1 = word_list(postive_list)
    print("-----")
    doc_vec(postive_list, list_1)
    cross_validataion.cross_validataion("data/word_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_feature")



if __name__=="__main__":
    filename="corpus/postive.txt"
    process.precessing()
    word(filename)

