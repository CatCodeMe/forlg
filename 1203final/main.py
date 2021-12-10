# -*- coding:utf-8 -*-
import split_and_stat as split
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
            #     print("样本：", sample, "大纲：", content)
            _statInfo = split.all(sample, content)
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


if __name__ == '__main__':

    """
      彩虹桥
    """
    sampleFiles = [
        'chq1-u/bld_x.txt',
        'chq1-u/gongong_x.txt',
        'chq1-u/nvwa-x.txt',
        'chq2-u/byzq_x.txt',
        'chq2-u/hml_x.txt',
        'chq2-u/jiaoliu_x.txt',
        'chq3-u/liwa_x.txt',
        'chq3-u/qinshi_x.txt',
        'chq3-u/woxxin_x.txt'
    ]
    # 'hml_x.txt',
    #  'jiaoliu_x.txt']
    contentFiles = ['../all_unique', '../a', '../b', '../c', '../d']

    detailWordFiles = [
        'chq1-u/bld_detail/',
        'chq1-u/gonggong_detail/',
        'chq1-u/nvwa_detail/',
        'chq2-u/byzq_detail/',
        'chq2-u/hml_detail/',
        'chq2-u/jiaoliu_detail/',
        'chq3-u/liwa_detail/',
        'chq3-u/qinshi_detail/',
        'chq3-u/woxxin_detail/'
    ]

    printTable(sampleFiles, contentFiles, detailWordFiles)


#     print(chqTable.get_html_string())
