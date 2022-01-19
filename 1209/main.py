# -*- coding:utf-8 -*-
import sys
import note_not_in as not_in
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
import os


def printTable(_sampleFiles, _contentFiles, _detailWordsDir):
    chqTable = PrettyTable(field_names=["样本文件", "样本词数",
                                        "大纲词", "总占比",
                                        "超纲词", "超纲词占比",
                                        "甲", "甲占比","甲_unique",
                                        "乙", "乙占比","乙_unique",
                                        "丙", "丙占比","丙_unique",
                                        "丁", "丁占比",'丁_unique'])
    # chqTable.set_style(MSWORD_FRIENDLY)
    chqTable.align = 'l'

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
                if content == '../all_unique':
                    _tmpResult.append(_statInfo['wordCount'])
                    _tmpResult.append(_statInfo['wordPercent'])
                    _tmpResult.append(_statInfo['notWordCount'])
                    _tmpResult.append(_statInfo['notWordPercent'])
            else:
                _tmpResult.append(_statInfo['wordCount'])
                _tmpResult.append(_statInfo['wordPercent'])
                _tmpResult.append(len(_statInfo['words']))
                _detailWordFile = _detailWordsDir[i]
                # if not os.path.exists(_detailWordFile):
                #     os.makedirs(_detailWordFile)
                # with open(_detailWordFile+content[-1], 'w') as f:
                #     for m, word in enumerate(_statInfo['words']):
                #         f.write(word+"\n")

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
        # 'hyf/cuocuo_2.txt',
        # 'hyf/di_san_zhi.txt',
        # 'hyf/dian_nao.txt',
        # 'hyf/hua_pi.txt',
        # 'hyf/liang_ge_haizi.txt',
        # 'hyf/qing_feng.txt',
        # 'hyf/ru_guo.txt',
        # 'hyf/tiao_wu.txt',
        # 'hyf/yue_liang.txt'


        'chq/bld_x.txt',
        'chq/byzq_x.txt',
        'chq/gonggong_x.txt',
        'chq/hml_x.txt',
        'chq/jiaoliu_x.txt',
        'chq/liwa_x.txt',
        'chq/nvwa_x.txt',
        'chq/qinshi_x.txt',
        'chq/woxxin_x.txt'
    ]

    # words
    contentFiles = ['../all_unique', '../a', '../b', '../c', '../d']

    detailWordFiles = [
        'chq/bld_detail/',
        'chq/byzq_detail/',
        'chq/gonggong_detail/',
        'chq/hml_detail/',
        'chq/jiaoliu_detail/',
        'chq/liwa_detail/',
        'chq/nvwa_detail/',
        'chq/qinshi_detail/',
        'chq/woxxin_detail/'

        # 'hyf/cuocuo_2.txt',
        #         'hyf/di_san_zhi.txt',
        #         'hyf/dian_nao.txt',
        #         'hyf/hua_pi.txt',
        #         'hyf/liang_ge_haizi.txt',
        #         'hyf/qing_feng.txt',
        #         'hyf/tiao_wu.txt',
        #         'hyf/yue_liang.txt'

        # 'hyf/cuocuo_2_detail/',
        # 'hyf/di_san_zhi_detail/',
        # 'hyf/dian_nao_detail/',
        # 'hyf/hua_pi_detail/',
        # 'hyf/liang_ge_haizi_detail/',
        # 'hyf/qing_feng_detail/',
        # 'hyf/ru_guo_detail/',
        # 'hyf/tiao_wu_detail/',
        # 'hyf/yue_liang_detail/'
    ]

    print("start")
    printTable(sampleFiles, contentFiles, detailWordFiles)


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
