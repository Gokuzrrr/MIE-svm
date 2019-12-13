#-*-coding:utf-8-*-

"""
    主函数
"""

import word_feature #词汇特征
import dependency_feature#依存语法特征
#import phrase_feature#短语块特征
import pos_feature#词性特征
import logistic_feature#逻辑特征
import cross_validataion
import process,evaluate,bash_shell

def word_pos_vec(word_list,pos_list,list_1):
    output = open("data/word_pos_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list=word_list[i]
        pos_data_list=pos_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" + word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        #word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)
        # pos_feature_1
        posf_p1b1 = pos_feature.POSF_P1B1(pos_data_list)
        L.append(posf_p1b1)
        # pos_feature_2
        posf_p1b2 = pos_feature.POSF_P1B2(pos_data_list)
        L.append(posf_p1b2)
        # pos_feature_3
        posf_p2a1 = pos_feature.POSF_P2A1(pos_data_list)
        L.append(posf_p2a1)
        # pos_feature_4
        posf_p2a2 = pos_feature.POSF_P2A2(pos_data_list)
        L.append(posf_p2a2)
        # pos_feature_5
        posf_pf = pos_feature.POSF_PF(pos_data_list)
        L.append(posf_pf)

        # pos_feature_6
        posf_pl = pos_feature.POSF_PL(pos_data_list)
        L.append(posf_pl)

        # pos_feature_7
        posf_po = pos_feature.POSF_PO(pos_data_list)
        if posf_po:
            for i in posf_po:
                L.append(i)

        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # pos_feature_8
        posf_pnull = pos_feature.POSF_PNULL(pos_data_list)
        if posf_pnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        output.write("\n")
    cross_validataion.cross_validataion("data/word_pos_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_pos_feature")

def word_logistic(word_list,logistic_list,list_1):
    output = open("data/word_logistic_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list = word_list[i]
        logistic_data_list = logistic_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" +word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        # word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)


        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        lf_distance = logistic_feature.LF_distance(logistic_data_list)
        output.write(str(lf_distance) + "\t")

        lf_bacterianum = logistic_feature.LF_bacteriaNum(logistic_data_list)
        output.write(str(lf_bacterianum) + "\t")

        lf_insert = logistic_feature.LF_insert(logistic_data_list)
        output.write(str(lf_insert) + "\n")

        # lf_verbbt = logistic_feature.LF_verbBT(logistic_data_list)
        # if lf_verbbt:
        #     output.write("1" + "\t")
        # else:
        #     output.write("0" + "\t")
        # pumcnum = logistic_feature.pumcNum(logistic_data_list)
        # output.write(str(pumcnum) + "\n")
    cross_validataion.cross_validataion("data/word_logistic_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_logistic_feature")

def word_dependency(word_list,dependency_list,list_1):
    output = open("data/word_dependency_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list = word_list[i]
        dependency_data_list = dependency_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" + word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        # word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)

        # depedncy_feature_1
        df_p1dw = dependency_feature.DF_P1DW(dependency_data_list)
        for word in df_p1dw:
            L.append(word)
        # depedncy_feature_2
        df_p1dt = dependency_feature.DF_P1DT(dependency_data_list)
        for i in df_p1dt:
            L.append(i)
        # depedncy_feature_3
        df_p1p = dependency_feature.DF_P1P(dependency_data_list)
        L.append(df_p1p)
        # depedncy_feature_4
        df_p1toroot = dependency_feature.DF_P1ToROOT(dependency_data_list)
        if df_p1toroot:
            for i in df_p1toroot:
                L.append(i)
        # depedncy_feature_5
        df_p2dw = dependency_feature.DF_P2DW(dependency_data_list)
        for i in df_p2dw:
            L.append(i)
        # depedncy_feature_6
        df_p2dt = dependency_feature.DF_P2DT(dependency_data_list)
        for i in df_p2dt:
            L.append(i)
        # depedncy_feature_7
        df_p2p = dependency_feature.DF_P2P(dependency_data_list)
        L.append(df_p2p)
        # depedncy_feature_8
        df_p2toroot = dependency_feature.DF_P2ToROOT(dependency_data_list)
        if df_p2toroot:
            for i in df_p2toroot:
                L.append(i)
        # depedncy_feature_9
        df_lcs = dependency_feature.DF_LCS(dependency_data_list)
        if df_lcs:
            for i in df_lcs:
                L.append(i)
        # depedncy_feature_10
        df_dw = dependency_feature.DF_DW(dependency_data_list)
        if df_dw:
            for i in df_dw:
                L.append(i)
        # depedncy_feature_11
        df_dp = dependency_feature.DF_DP(dependency_data_list)
        if df_dp:
            for i in df_dp:
                L.append(i)
        # depedncy_feature_12
        df_dpvb = dependency_feature.DF_DPVB(dependency_data_list)
        if df_dpvb:
            for i in df_dpvb:
                L.append(i)

        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")


        # depedncy_feature_13
        df_directD = dependency_feature.DF_directD(dependency_data_list)
        if df_directD:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # depedncy_feature_14
        df_existdsw = dependency_feature.DF_existDSW(dependency_data_list)
        if df_existdsw:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # depedncy_feature_15
        df_existdp = dependency_feature.DF_existDP(dependency_data_list)
        if df_existdp:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # depedncy_feature_16
        df_dpvbnum = dependency_feature.DF_DPVBNum(dependency_data_list)
        output.write(str(df_dpvbnum) + "\n")
    cross_validataion.cross_validataion("data/word_dependency_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_dependency_feature")

def word_logistic_dependency(word_list,logistic_list,dependency_list,list_1):
    output = open("data/word_logistic_dependency_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list = word_list[i]
        logistic_data_list = logistic_list[i]
        dependency_data_list = dependency_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" + word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        # word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)
        # depedncy_feature_1
        df_p1dw = dependency_feature.DF_P1DW(dependency_data_list)
        for word in df_p1dw:
            L.append(word)
        # depedncy_feature_2
        df_p1dt = dependency_feature.DF_P1DT(dependency_data_list)
        for i in df_p1dt:
            L.append(i)
        # depedncy_feature_3
        df_p1p = dependency_feature.DF_P1P(dependency_data_list)
        L.append(df_p1p)
        # depedncy_feature_4
        df_p1toroot = dependency_feature.DF_P1ToROOT(dependency_data_list)
        if df_p1toroot:
            for i in df_p1toroot:
                L.append(i)
        # depedncy_feature_5
        df_p2dw = dependency_feature.DF_P2DW(dependency_data_list)
        for i in df_p2dw:
            L.append(i)
        # depedncy_feature_6
        df_p2dt = dependency_feature.DF_P2DT(dependency_data_list)
        for i in df_p2dt:
            L.append(i)
        # depedncy_feature_7
        df_p2p = dependency_feature.DF_P2P(dependency_data_list)
        L.append(df_p2p)
        # depedncy_feature_8
        df_p2toroot = dependency_feature.DF_P2ToROOT(dependency_data_list)
        if df_p2toroot:
            for i in df_p2toroot:
                L.append(i)
        # depedncy_feature_9
        df_lcs = dependency_feature.DF_LCS(dependency_data_list)
        if df_lcs:
            for i in df_lcs:
                L.append(i)
        # depedncy_feature_10
        df_dw = dependency_feature.DF_DW(dependency_data_list)
        if df_dw:
            for i in df_dw:
                L.append(i)
        # depedncy_feature_11
        df_dp = dependency_feature.DF_DP(dependency_data_list)
        if df_dp:
            for i in df_dp:
                L.append(i)
        # depedncy_feature_12
        df_dpvb = dependency_feature.DF_DPVB(dependency_data_list)
        if df_dpvb:
            for i in df_dpvb:
                L.append(i)

        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        # logistic_feature_1
        lf_distance = logistic_feature.LF_distance(logistic_data_list)
        output.write(str(lf_distance) + "\t")
        lf_bacterianum = logistic_feature.LF_bacteriaNum(logistic_data_list)
        output.write(str(lf_bacterianum) + "\t")
        lf_insert = logistic_feature.LF_insert(logistic_data_list)
        output.write(str(lf_insert) + "\t")
        # logistic_feature_2
        lf_verbbt = logistic_feature.LF_verbBT(logistic_data_list)
        if lf_verbbt:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # logistic_feature_3
        pumcnum = logistic_feature.pumcNum(logistic_data_list)
        output.write(str(pumcnum) + "\t")

        # depedncy_feature_13
        df_directD = dependency_feature.DF_directD(dependency_data_list)
        if df_directD:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # depedncy_feature_14
        df_existdsw = dependency_feature.DF_existDSW(dependency_data_list)
        if df_existdsw:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # depedncy_feature_15
        df_existdp = dependency_feature.DF_existDP(dependency_data_list)
        if df_existdp:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # depedncy_feature_16
        df_dpvbnum = dependency_feature.DF_DPVBNum(dependency_data_list)
        output.write(str(df_dpvbnum) + "\n")
    cross_validataion.cross_validataion("data/word_logistic_dependency_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_logistic_dependency_feature")

def word_pos_logistic_vec(word_list,pos_list,logistic_list,list_1):
    output = open("data/word_pos_logistic_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list=word_list[i]
        pos_data_list=pos_list[i]
        logistic_data_list=logistic_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" + word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        #word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)
        # pos_feature_1
        posf_p1b1 = pos_feature.POSF_P1B1(pos_data_list)
        L.append(posf_p1b1)
        # pos_feature_2
        posf_p1b2 = pos_feature.POSF_P1B2(pos_data_list)
        L.append(posf_p1b2)
        # pos_feature_3
        posf_p2a1 = pos_feature.POSF_P2A1(pos_data_list)
        L.append(posf_p2a1)
        # pos_feature_4
        posf_p2a2 = pos_feature.POSF_P2A2(pos_data_list)
        L.append(posf_p2a2)
        # pos_feature_5
        posf_pf = pos_feature.POSF_PF(pos_data_list)
        L.append(posf_pf)

        # pos_feature_6
        posf_pl = pos_feature.POSF_PL(pos_data_list)
        L.append(posf_pl)

        # pos_feature_7
        posf_po = pos_feature.POSF_PO(pos_data_list)
        if posf_po:
            for i in posf_po:
                L.append(i)

        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # pos_feature_8
        posf_pnull = pos_feature.POSF_PNULL(pos_data_list)
        if posf_pnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        lf_distance = logistic_feature.LF_distance(logistic_data_list)
        output.write(str(lf_distance) + "\t")
        lf_bacterianum = logistic_feature.LF_bacteriaNum(logistic_data_list)
        output.write(str(lf_bacterianum) + "\t")
        lf_insert = logistic_feature.LF_insert(logistic_data_list)
        output.write(str(lf_insert) + "\t")
        lf_verbbt = logistic_feature.LF_verbBT(logistic_data_list)
        if lf_verbbt:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        pumcnum = logistic_feature.pumcNum(logistic_data_list)
        output.write(str(pumcnum) + "\n")
    cross_validataion.cross_validataion("data/word_pos_logistic_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_pos_logistic_feature")

# 补
def word_pos_dependency_vec(word_list,pos_list,depdency_list,list_1):
    output = open("data/word_pos_dependency_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list = word_list[i]
        pos_data_list = pos_list[i]
        dependency_data_list=depdency_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" + word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        # word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)
        # pos_feature_1
        posf_p1b1 = pos_feature.POSF_P1B1(pos_data_list)
        L.append(posf_p1b1)
        # pos_feature_2
        posf_p1b2 = pos_feature.POSF_P1B2(pos_data_list)
        L.append(posf_p1b2)
        # pos_feature_3
        posf_p2a1 = pos_feature.POSF_P2A1(pos_data_list)
        L.append(posf_p2a1)
        # pos_feature_4
        posf_p2a2 = pos_feature.POSF_P2A2(pos_data_list)
        L.append(posf_p2a2)
        # pos_feature_5
        posf_pf = pos_feature.POSF_PF(pos_data_list)
        L.append(posf_pf)

        # pos_feature_6
        posf_pl = pos_feature.POSF_PL(pos_data_list)
        L.append(posf_pl)

        # pos_feature_7
        posf_po = pos_feature.POSF_PO(pos_data_list)
        if posf_po:
            for i in posf_po:
                L.append(i)
        #depedncy_feature_1
        df_p1dw = dependency_feature.DF_P1DW(dependency_data_list)
        for word in df_p1dw:
            L.append(word)
        #depedncy_feature_2
        df_p1dt = dependency_feature.DF_P1DT(dependency_data_list)
        for i in df_p1dt:
            L.append(i)
        #depedncy_feature_3
        df_p1p = dependency_feature.DF_P1P(dependency_data_list)
        L.append(df_p1p)
        #depedncy_feature_4
        df_p1toroot = dependency_feature.DF_P1ToROOT(dependency_data_list)
        if df_p1toroot:
            for i in df_p1toroot:
                L.append(i)
        #depedncy_feature_5
        df_p2dw = dependency_feature.DF_P2DW(dependency_data_list)
        for i in df_p2dw:
            L.append(i)
        #depedncy_feature_6
        df_p2dt = dependency_feature.DF_P2DT(dependency_data_list)
        for i in df_p2dt:
            L.append(i)
        #depedncy_feature_7
        df_p2p = dependency_feature.DF_P2P(dependency_data_list)
        L.append(df_p2p)
        #depedncy_feature_8
        df_p2toroot = dependency_feature.DF_P2ToROOT(dependency_data_list)
        if df_p2toroot:
            for i in df_p2toroot:
                L.append(i)
        #depedncy_feature_9
        df_lcs = dependency_feature.DF_LCS(dependency_data_list)
        if df_lcs:
            for i in df_lcs:
                L.append(i)
        #depedncy_feature_10
        df_dw = dependency_feature.DF_DW(dependency_data_list)
        if df_dw:
            for i in df_dw:
                L.append(i)
        #depedncy_feature_11
        df_dp = dependency_feature.DF_DP(dependency_data_list)
        if df_dp:
            for i in df_dp:
                L.append(i)
        #depedncy_feature_12
        df_dpvb = dependency_feature.DF_DPVB(dependency_data_list)
        if df_dpvb:
            for i in df_dpvb:
                L.append(i)

        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")

        # pos_feature_8
        posf_pnull = pos_feature.POSF_PNULL(pos_data_list)
        if posf_pnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")


        #depedncy_feature_13
        df_directD = dependency_feature.DF_directD(dependency_data_list)
        if df_directD:
            output.write("n1" + "\t")
        else:
            output.write("0" + "\t")
        #depedncy_feature_14
        df_existdsw = dependency_feature.DF_existDSW(dependency_data_list)
        if df_existdsw:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        #depedncy_feature_15
        df_existdp = dependency_feature.DF_existDP(dependency_data_list)
        if df_existdp:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        #depedncy_feature_16
        df_dpvbnum = dependency_feature.DF_DPVBNum(dependency_data_list)
        output.write(str(df_dpvbnum)+"\n")

    cross_validataion.cross_validataion("data/word_pos_dependency_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_pos_dependency_feature")


def word_pos_logistic_dependency_vec(word_list,pos_list,logistic_list,depdency_list,list_1):
    output = open("data/word_pos_logistic_dependency_feature.txt", "w+", encoding="utf-8")
    for i in range(len(word_list)):
        print(i)
        word_data_list = word_list[i]
        pos_data_list = pos_list[i]
        logistic_data_list = logistic_list[i]
        dependency_data_list=depdency_list[i]
        output.write(str(word_data_list[0]) + "\t")
        L = []
        L.append("MW1_" + word_data_list[2])
        L.append("MW2_" + word_data_list[4])
        # word_feature_1
        wf_pf = word_feature.WF_PF(word_data_list)
        L.append(wf_pf)
        # word_feature
        wf_pl = word_feature.WF_PL(word_data_list)
        L.append(wf_pl)
        # word_feature_3
        wf_po = word_feature.WF_PO(word_data_list)
        if wf_po:
            for i in wf_po:
                L.append(i)
        # word_feature_4
        wf_p1b1 = word_feature.WF_P1B1(word_data_list)
        L.append(wf_p1b1)
        # word_feature_5
        wf_p1b2 = word_feature.WF_P1B2(word_data_list)
        L.append(wf_p1b2)
        # word_feature_6
        wf_p2a1 = word_feature.WF_P2A1(word_data_list)
        L.append(wf_p2a1)
        # word_feature_7
        wf_p2a2 = word_feature.WF_P2A2(word_data_list)
        L.append(wf_p2a2)
        # pos_feature_1
        posf_p1b1 = pos_feature.POSF_P1B1(pos_data_list)
        L.append(posf_p1b1)
        # pos_feature_2
        posf_p1b2 = pos_feature.POSF_P1B2(pos_data_list)
        L.append(posf_p1b2)
        # pos_feature_3
        posf_p2a1 = pos_feature.POSF_P2A1(pos_data_list)
        L.append(posf_p2a1)
        # pos_feature_4
        posf_p2a2 = pos_feature.POSF_P2A2(pos_data_list)
        L.append(posf_p2a2)
        # pos_feature_5
        posf_pf = pos_feature.POSF_PF(pos_data_list)
        L.append(posf_pf)

        # pos_feature_6
        posf_pl = pos_feature.POSF_PL(pos_data_list)
        L.append(posf_pl)

        # pos_feature_7
        posf_po = pos_feature.POSF_PO(pos_data_list)
        if posf_po:
            for i in posf_po:
                L.append(i)
        #depedncy_feature_1
        df_p1dw = dependency_feature.DF_P1DW(dependency_data_list)
        for word in df_p1dw:
            L.append(word)
        #depedncy_feature_2
        df_p1dt = dependency_feature.DF_P1DT(dependency_data_list)
        for i in df_p1dt:
            L.append(i)
        #depedncy_feature_3
        df_p1p = dependency_feature.DF_P1P(dependency_data_list)
        L.append(df_p1p)
        #depedncy_feature_4
        df_p1toroot = dependency_feature.DF_P1ToROOT(dependency_data_list)
        if df_p1toroot:
            for i in df_p1toroot:
                L.append(i)
        #depedncy_feature_5
        df_p2dw = dependency_feature.DF_P2DW(dependency_data_list)
        for i in df_p2dw:
            L.append(i)
        #depedncy_feature_6
        df_p2dt = dependency_feature.DF_P2DT(dependency_data_list)
        for i in df_p2dt:
            L.append(i)
        #depedncy_feature_7
        df_p2p = dependency_feature.DF_P2P(dependency_data_list)
        L.append(df_p2p)
        #depedncy_feature_8
        df_p2toroot = dependency_feature.DF_P2ToROOT(dependency_data_list)
        if df_p2toroot:
            for i in df_p2toroot:
                L.append(i)
        #depedncy_feature_9
        df_lcs = dependency_feature.DF_LCS(dependency_data_list)
        if df_lcs:
            for i in df_lcs:
                L.append(i)
        #depedncy_feature_10
        df_dw = dependency_feature.DF_DW(dependency_data_list)
        if df_dw:
            for i in df_dw:
                L.append(i)
        #depedncy_feature_11
        df_dp = dependency_feature.DF_DP(dependency_data_list)
        if df_dp:
            for i in df_dp:
                L.append(i)
        #depedncy_feature_12
        df_dpvb = dependency_feature.DF_DPVB(dependency_data_list)
        if df_dpvb:
            for i in df_dpvb:
                L.append(i)

        feature = word_feature.word_to_vec(list_1, L)
        [output.write(str(i) + "\t") for i in feature]

        # word_feature_8
        wf_pone = word_feature.WF_Pone(word_data_list)
        if wf_pone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_9
        wf_null = word_feature.WF_NULL(word_data_list)
        if wf_null:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_10
        wf_p1bone = word_feature.WF_P1BOne(word_data_list)
        if wf_p1bone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_11
        wf_p1bnull = word_feature.WF_P1BNULL(word_data_list)
        if wf_p1bnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_12
        wf_p2aone = word_feature.WF_P2AOne(word_data_list)
        if wf_p2aone:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # word_feature_13
        wf_P2anull = word_feature.WF_P2ANULL(word_data_list)
        if wf_P2anull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        # pos_feature_8
        posf_pnull = pos_feature.POSF_PNULL(pos_data_list)
        if posf_pnull:
            output.write(str(1) + "\t")
        else:
            output.write(str(0) + "\t")
        #logistic_feature_1
        lf_distance = logistic_feature.LF_distance(logistic_data_list)
        output.write(str(lf_distance) + "\t")
        lf_bacterianum = logistic_feature.LF_bacteriaNum(logistic_data_list)
        output.write(str(lf_bacterianum) + "\t")
        lf_insert = logistic_feature.LF_insert(logistic_data_list)
        output.write(str(lf_insert) + "\t")
        #logistic_feature_2
        lf_verbbt = logistic_feature.LF_verbBT(logistic_data_list)
        if lf_verbbt:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        # logistic_feature_3
        pumcnum = logistic_feature.pumcNum(logistic_data_list)
        output.write(str(pumcnum) + "\t")

        #depedncy_feature_13
        df_directD = dependency_feature.DF_directD(dependency_data_list)
        if df_directD:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        #depedncy_feature_14
        df_existdsw = dependency_feature.DF_existDSW(dependency_data_list)
        if df_existdsw:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        #depedncy_feature_15
        df_existdp = dependency_feature.DF_existDP(dependency_data_list)
        if df_existdp:
            output.write("1" + "\t")
        else:
            output.write("0" + "\t")
        #depedncy_feature_16
        df_dpvbnum = dependency_feature.DF_DPVBNum(dependency_data_list)
        output.write(str(df_dpvbnum)+"\n")
    cross_validataion.cross_validataion("data/word_pos_logistic_dependency_feature.txt")
    bash_shell.bash_shell()
    evaluate.evaluate("word_pos_logistic_dependency_feature")



if __name__=="__main__":
    filename ="corpus/postive.txt"
    process.precessing()
    print("词汇特征")
    word_list = word_feature.sentence_to_word(filename)
    word_feature_list=word_feature.word_list(word_list)
    print("词性特征")
    tag_list=pos_feature.pos_tokizen(filename)
    pos_feature_list=pos_feature.word_list(tag_list)
    print("逻辑特征")
    logistic_list = logistic_feature.pos_tokizen(filename)
    print("依存句法分析")
    dependency_list=dependency_feature.depedency_tokenize(filename)
    dependency_feature_list=dependency_feature.word_list(dependency_list)
    #只有单词特征
    word_feature.word(filename)
    #单词+词性特征
    word_pos_vec(word_list,tag_list,word_feature_list+pos_feature_list)
    #单词+逻辑特征
    word_logistic(word_list,logistic_list,word_feature_list)
    #单词+依存句法
    word_dependency(word_list,dependency_list,word_feature_list+dependency_feature_list)
    #单词+词性+逻辑
    word_pos_logistic_vec(word_list,tag_list,logistic_list,word_feature_list+pos_feature_list)
    #单词+逻辑+依存句法
    word_logistic_dependency(word_list,logistic_list,dependency_list,word_feature_list+dependency_feature_list)
    #单词+词性+逻辑+依存句法
    word_pos_logistic_dependency_vec(word_list,tag_list,logistic_list,dependency_list,word_feature_list+pos_feature_list+dependency_feature_list)
    ## 单词+词性+依存句法
    word_pos_dependency_vec(word_list, tag_list, dependency_list,
                            word_feature_list + pos_feature_list + dependency_feature_list)







