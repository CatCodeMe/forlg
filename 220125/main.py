# -*- coding:utf-8 -*-
import sys
import note as not_in
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
import os


def printTable(title, _sampleFiles, _contentFiles, _detailWordsDir,level):
    chqTable = PrettyTable(field_names=["样本文件", "样本词(字)数",
                                        "大纲词(字)", "总占比",
                                        "超纲词(字)", "超纲词(字)占比",
                                        # "定级","原始级别",
                                        "1", "1占比",
                                        "2", "2占比",
                                        "3", "3占比",
                                        "4", "4占比",
                                        "5", "5占比",
                                        "6", "6占比"])
    # chqTable.set_style(MSWORD_FRIENDLY)
    chqTable.align = 'l'
    chqTable.title = title

    for i, sample in enumerate(_sampleFiles):
        hasAdd = False
        _tmpResult = []
        for j, content in enumerate(_contentFiles):
            print("样本：", sample, "大纲：", content)
            _statInfo = not_in.all(sample, content)
            if j == 0 and not hasAdd:
                _tmpResult.append(sample)
                _tmpResult.append(_statInfo['totalCount'])
                hasAdd = True
                if content == 'words' or content == 'w_all':
                    _tmpResult.append(_statInfo['wordCount'])
                    _tmpResult.append(_statInfo['wordPercent'])
                    _tmpResult.append(_statInfo['notWordCount'])
                    _tmpResult.append(_statInfo['notWordPercent'])
                # _detailWordFile = _detailWordsDir[i]
                # if not os.path.exists(_detailWordFile):
                #     os.makedirs(_detailWordFile)
                # with open(_detailWordFile+content[-1], 'w') as f:
                #     for m, word in enumerate(_statInfo['illegal_words']):
                #         f.write(word+"\n")
            else:
                _tmpResult.append(_statInfo['wordCount'])
                _tmpResult.append(_statInfo['wordPercent'])
                # _tmpResult.append(len(_statInfo['words']))
                # _detailWordFile = _detailWordsDir[i]
                # if not os.path.exists(_detailWordFile):
                #     os.makedirs(_detailWordFile)
                # with open(_detailWordFile+content[-1], 'w') as f:
                #     for m, word in enumerate(_statInfo['illegal_words']):
                #         f.write(word+"\n")
        # c1 = float(_tmpResult[7])
        # c2 = float(_tmpResult[9])
        # c3 = float(_tmpResult[11])
        # c4 = float(_tmpResult[13])
        # c5 = float(_tmpResult[15])
        # c6 = float(_tmpResult[17])
        # degree = float(format(float(_tmpResult[3]) * 0.8,'.4f'))
        # calLevel = 1
        # if c1 > degree:
        #     calLevel = 1
        # elif (c1 + c2) >= degree:
        #     calLevel = 2
        # elif (c1 + c2 + c3) >= degree:
        #     calLevel = 3
        # elif (c1 + c2 + c3 + c4) >= degree:
        #     calLevel = 4
        # elif (c1 + c2 + c3 + c4 + c5) >= degree:
        #     calLevel = 5
        # else :
        #     calLevel = 6

        # _tmpResult.insert(6,calLevel)

        # src_level = level[sample]
        # _tmpResult.insert(7,src_level)

        chqTable.add_row(_tmpResult)
    print(chqTable)
    print(chqTable.get_csv_string())


def not_in_stat(_sampleFiles, _contentFiles):
    _content_set = set()
    for i, content in enumerate(_contentFiles):
        with open(content, 'r') as f:
            fls = f.readlines()
            for i in range(0, len(fls)):
                _content_set.add(fls[i].rstrip("\n"))
    for i, sample in enumerate(_sampleFiles):
        _newFile = ""
        with open(sample, 'r') as f:
            fls = f.readlines()
            for i in range(0, len(fls)):
                _newLine = ""
                line = fls[i].rstrip("\n")
                lineList = line.split('/')
                for j, val in enumerate(lineList):
                    if val == "":
                        continue
                    if val in _content_set:
                        _newLine += val + "/"
                    else:
                        _newLine += "【" + val + "】/"
                _newFile += _newLine + "\n"
        # # todo
        # with open('./hyf/not_in_hua_pi', 'w') as f:
        #     f.write(_newFile)


def writeNew(_srcSampleFiles, _newSampleFiles):
    for i, sample in enumerate(_srcSampleFiles):
        _statInfo = not_in.all(sample, '../all_unique')
        with open(_newSampleFiles[i], 'w') as f:
            for m, word in enumerate(_statInfo['legal_all_words']):
                f.write(word+"\n")


if __name__ == '__main__':

    """
      汉语风
    """
    sampleFiles = [
        # 'hyf/hyf_1.txt',
        # 'hyf/hyf_2.txt',
        # 'hyf/hyf_3.txt'

        # 'chq/chq_1.txt',
        # 'chq/chq_2.txt',
        # 'chq/chq_3.txt'

        # 'chq/bld_x.txt',
        # 'chq/byzq_x.txt',
        # 'chq/gonggong_x.txt',
        # 'chq/hml_x.txt',
        # 'chq/jiaoliu_x.txt',
        # 'chq/liwa_x.txt',
        # 'chq/nvwa_x.txt',
        # 'chq/qinshi_x.txt',
        # 'chq/woxxin_x.txt'

        # 'hyf_del/cuocuo.txt',
        # 'hyf_del/dianao.txt',
        # 'hyf_del/disanzhi.txt',
        # 'hyf_del/haizi.txt',
        # 'hyf_del/huapi.txt',
        # 'hyf_del/qingfeng.txt',
        # 'hyf_del/ruguo.txt',
        # 'hyf_del/tiaowu.txt',
        # 'hyf_del/yueliang.txt'

        'hyf_del/hyf_del_1',
        'hyf_del/hyf_del_2',
        'hyf_del/hyf_del_3'
    ]

    # 词
    title = '国际汉语通用教材-1~6级(词)'
    contentFiles = ['words', 'ws_1', 'ws_2', 'ws_3', 'ws_4', 'ws_5', 'ws_6']

    # title = '国际汉语通用教材-1~6级(词)【去重】'
    # contentFiles = ['words', 'ws_1', 'ws_2', 'ws_3', 'ws_4', 'ws_5', 'ws_6']


    detailWordFiles = [
        'hyf/hyf_1/',
        'hyf/hyf_2/',
        'hyf/hyf_3/',
        # 'chq/chq_1/',
        # 'chq/chq_2/',
        # 'chq/chq_3/'
    ]

    level = {
        # 'chq/bld_x.txt': 1,
        # 'chq/byzq_x.txt':2,
        # 'chq/gonggong_x.txt':1,
        # 'chq/hml_x.txt':2,
        # 'chq/jiaoliu_x.txt':2,
        # 'chq/liwa_x.txt':3,
        # 'chq/nvwa_x.txt': 1,
        # 'chq/qinshi_x.txt':3,
        # 'chq/woxxin_x.txt':3

        # 'hyf_del/cuocuo.txt':1,
        # 'hyf_del/dianao.txt':2,
        # 'hyf_del/disanzhi.txt':3,
        # 'hyf_del/haizi.txt':1,
        # 'hyf_del/huapi.txt':3,
        # 'hyf_del/qingfeng.txt':2,
        # 'hyf_del/ruguo.txt':2,
        # 'hyf_del/tiaowu.txt':1,
        # 'hyf_del/yueliang.txt':3
    }


    print("start")
    printTable(title, sampleFiles, contentFiles, detailWordFiles, level)

    delSignNewSampleFiles = [
        # 'chq/new/cuocuocuo.txt',
        # 'chq/new/cuocuo2.txt'
        # # 'chq/new/di_san_zhi.txt',
        # # 'chq/new/dian_nao.txt',
        # # 'chq/new/hua_pi.txt',
        # # 'chq/new/liang_ge_haizi.txt',
        # # 'chq/new/qing_feng.txt',
        # # 'chq/new/tiao_wu.txt',
        # # 'chq/new/yue_liang.txt'

        # 'hyf/new/ru_guo.txt'

        # 'chq/new/bld_x.txt',
        # 'chq/new/byzq_x.txt',
        # 'chq/new/gonggong_x.txt',
        # 'chq/new/hml_x.txt',
        # 'chq/new/jiaoliu_x.txt',
        # 'chq/new/liwa_x.txt',
        # 'chq/new/nvwa_x.txt',
        # 'chq/new/qinshi_x.txt',
        # 'chq/new/woxxin_x.txt'
    ]
    # writeNew(sampleFiles, delSignNewSampleFiles)
