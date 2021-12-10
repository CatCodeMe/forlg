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
                                        "甲", "甲占比",
                                        "乙", "乙占比",
                                        "丙", "丙占比",
                                        "丁", "丁占比"])
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
                _detailWordFile = _detailWordsDir[i]
                if not os.path.exists(_detailWordFile):
                    os.makedirs(_detailWordFile)
                with open(_detailWordFile+content[-1], 'w') as f:
                    for m, word in enumerate(_statInfo['words']):
                        f.write(word+"\n")

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
      彩虹桥
    """
    sampleFiles = [
        # 'chq/cuocuocuo.txt',
        # 'chq/di_san_zhi.txt',
        # 'chq/dian_nao.txt',
        # 'chq/hua_pi.txt',
        # 'chq/liang_ge_haizi.txt',
        # 'chq/qing_feng.txt',
        # 'chq/tiao_wu.txt',
        # 'chq/yue_liang.txt'

        'chq/new/cuocuocuo.txt',
        'chq/new/di_san_zhi.txt',
        'chq/new/dian_nao.txt',
        'chq/new/hua_pi.txt',
        'chq/new/liang_ge_haizi.txt',
        'chq/new/qing_feng.txt',
        'chq/new/tiao_wu.txt',
        'chq/new/yue_liang.txt'
    ]
    # 'hml_x.txt',
    #  'jiaoliu_x.txt']
    contentFiles = ['../all_unique', '../a', '../b', '../c', '../d']

    detailWordFiles = [
        'chq/cuocuocuo_detail/',
        'chq/di_san_zhi_detail/',
        'chq/dian_nao_detail/',
        'chq/hua_pi_detail/',
        'chq/liang_ge_haizi_detail/',
        'chq/qing_feng_detail/',
        'chq/ru_guo_detail/',
        'chq/tiao_wu_detail/',
        'chq/yue_liang_detail/'
    ]

    delSignNewSampleFiles = [
        'chq/new/cuocuocuo.txt',
        'chq/new/di_san_zhi.txt',
        'chq/new/dian_nao.txt',
        'chq/new/hua_pi.txt',
        'chq/new/liang_ge_haizi.txt',
        'chq/new/qing_feng.txt',
        'chq/new/tiao_wu.txt',
        'chq/new/yue_liang.txt'

    ]

    printTable(sampleFiles, contentFiles, detailWordFiles)

    # writeNew(sampleFiles, delSignNewSampleFiles)
