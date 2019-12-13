#-*-coding:utf-8-*-

"""
    数据预处理，生成实例文件
"""

import  json
import numpy as np
import re
#实体对的替换
def insert_replace(each_line,entity_mapper,entity_list,filename,label):
    for mapper in entity_mapper:
        a=[]
        mapper_0_name = entity_list[mapper[0]][0]
        mapper_0_start = entity_list[mapper[0]][1]
        mapper_0_end = entity_list[mapper[0]][2]
        mapper_1_name = entity_list[mapper[1]][0]
        mapper_1_start = entity_list[mapper[1]][1]
        mapper_1_end = entity_list[mapper[1]][2]
        sent=each_line["sent"]
        if mapper_0_start>=mapper_1_start:
            sent=sent[:mapper_0_start]+mapper[0]+sent[mapper_0_end:]
            sent =sent[:mapper_1_start]+mapper[1]+sent[mapper_1_end:]
        else:
            sent = sent[:mapper_1_start] + mapper[1] + sent[mapper_1_end:]
            sent = sent[:mapper_0_start] + mapper[0] + sent[mapper_0_end:]
        for i in entity_list:
            if i not in mapper:
                a.append(i)
        if a:
            for j in a[-1::-1]:

                name=entity_list[j][0]
                sent=sent.replace(name,"BACTERIA_0")
        filename.write(str(label) + "\t" + str(mapper[0]) + "\t"+str(mapper_0_name)+"\t" + str(mapper[1]) + "\t"+str(mapper_1_name)+"\t" + str(sent) + "\n")





#实体对的组合
def couple_list(entity_list):
    # 提取实体列表中的实体id
    entity_key = []
    entity_couple = []  # 所有实体对的组合
    for k in entity_list.keys():
        entity_key.append(k)
    index=[]
    #对实体id进行排序
    entity_key_sort=[]
    for j in entity_key:
        index.append(int(j.split("T")[1]))
    sort_index=np.argsort(index)
    for n in sort_index:
        entity_key_sort.append(entity_key[n])
    # print("----")
    # print(entity_key,entity_key_sort)

    for i in range(len(entity_key_sort) - 1):
        for j in range(i + 1, len(entity_key_sort)):
            if entity_list[entity_key[i]][0] != entity_list[entity_key[j]][0]:
                entity_couple.append([entity_key_sort[i], entity_key_sort[j]])
            # else:
            #     print(entity_list[entity_key[i]][0],entity_list[entity_key[j]][0])

    return entity_couple,entity_key_sort

def precessing():
    AIMed_file = open("corpus/abstract_json_corpus.json", "r", encoding="utf-8")
    AIMed_data = json.load(AIMed_file)
    postive_file = open("corpus/postive.txt", "w+", encoding="utf-8")
    num=0
    for each_line in AIMed_data:

        relation_list=each_line["relation_list"]
        entity_list={}#所有实体的{id：[name,start,end]}
        entity_mapper=[]#有关系的实体对组合id

        #有关系的实体对
        if relation_list:
            #提取有关系的实体对
            for relation in relation_list:
                arg_1=relation["arg_1"]
                arg_2=relation["arg_2"]
                entity_mapper.append([arg_1,arg_2])
            #提取所有实体
            for entity in each_line["entity_list"]:
                entity_id = entity["entity_id"]
                entity_name = entity["entity_name"]
                start=entity["start_pos"]
                end=entity["end_pos"]
                entity_list[entity_id] = [entity_name,start,end]
            #去除自相互作用关系
            # for mapper in entity_mapper:
            #     if entity_list[mapper[0]][0] == entity_list[mapper[1]][0]:
            #         entity_mapper.remove(mapper)
            #实体对的组合
            entity_couple,entity_key=couple_list(entity_list)
            #替换有关系的实体对
            num+=len(entity_couple)
            insert_replace(each_line,entity_mapper,entity_list,postive_file,+1)
            #替换没有关系的组合对
            for mapper in entity_mapper:
                for cp in entity_couple:
                    if mapper[0] in cp and mapper[1] in cp:
                        entity_couple.remove(cp)
            L=[]
            #除去嵌套实体
            for cp in entity_couple:
                cp_0_name=entity_list[cp[0]][0]
                cp_0_start=entity_list[cp[0]][1]
                cp_0_end=entity_list[cp[0]][2]
                cp_1_name = entity_list[cp[1]][0]
                cp_1_start = entity_list[cp[1]][1]
                cp_1_end = entity_list[cp[1]][2]
                if len(cp_0_name)>=len(cp_1_name):
                    if cp_0_start<=cp_1_start and cp_0_end>=cp_1_end:
                        L.append(cp)
                else:
                    if cp_0_start >= cp_1_start and cp_0_end <= cp_1_end:
                        # print(cp[0], cp[1])
                        L.append(cp)
            for cp in L:
                entity_couple.remove(cp)
            insert_replace(each_line,entity_couple,entity_list,postive_file,-1)
        else:

            #提取没有关系的句子中的所有实体
            for entity in each_line["entity_list"]:
                name=entity["entity_name"]
                id=entity["entity_id"]
                start=entity["start_pos"]
                end=entity["end_pos"]
                entity_list[id]=[name,start,end]
                # print(entity_list)
            #如果实体个数小于两个则不考虑这个句子
            if len(entity_list)<2:
                continue
            else:
                entity_couple,entity_key=couple_list(entity_list)
                num+=len(entity_couple)
                L = []
                for cp in entity_couple:
                    cp_0_name = entity_list[cp[0]][0]
                    cp_0_start = entity_list[cp[0]][1]
                    cp_0_end = entity_list[cp[0]][2]
                    cp_1_name = entity_list[cp[1]][0]
                    cp_1_start = entity_list[cp[1]][1]
                    cp_1_end = entity_list[cp[1]][2]
                    if len(cp_0_name) >= len(cp_1_name):
                        if cp_0_start <= cp_1_start and cp_0_end >= cp_1_end:
                            L.append(cp)
                    else:
                        if cp_0_start >= cp_1_start and cp_0_end <= cp_1_end:
                            L.append(cp)
                for cp in L:
                    entity_couple.remove(cp)
                insert_replace(each_line, entity_couple, entity_list, postive_file, -1)

if __name__=="__main__":
    precessing()























