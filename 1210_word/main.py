# -*- coding:utf-8 -*-
import sys
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
import os
import word_stat as word_stat


def printTable(_sampleFiles, _contentFiles, _detailWordsDir):
    hyfTable = PrettyTable(field_names=["样本文件", "样本词数",
                                        "大纲词", "总占比",
                                        "超纲词", "超纲词占比",
                                        "甲", "甲占比",
                                        "乙", "乙占比",
                                        "丙", "丙占比",
                                        "丁", "丁占比"])
    # hyfTable.set_style(MSWORD_FRIENDLY)
    hyfTable.align = 'l'

    illegal_words_all_unique = {}

    for i, sample in enumerate(_sampleFiles):
        hasAdd = False
        _tmpResult = []
        for j, content in enumerate(_contentFiles):
            print("样本：", sample, "大纲：", content)
            # _statInfo = not_in.all(sample, content)
            _statInfo = word_stat.all(sample, content)
            if j == 0 and not hasAdd:
                _tmpResult.append(sample)
                _tmpResult.append(_statInfo['totalCount'])
                hasAdd = True
                if content == '../words_all_unique':
                    _tmpResult.append(_statInfo['wordCount'])
                    _tmpResult.append(_statInfo['wordPercent'])
                    _tmpResult.append(_statInfo['notWordCount'])
                    _tmpResult.append(_statInfo['notWordPercent'])
                    illegal_words_all_unique[sample] = _statInfo['illegal_words']
            # else:
            #     _tmpResult.append(_statInfo['wordCount'])
            #     _tmpResult.append(_statInfo['wordPercent'])
            #     _detailWordFile = _detailWordsDir[i]
            #     if not os.path.exists(_detailWordFile):
            #         os.makedirs(_detailWordFile)
            #     with open(_detailWordFile+content[-1], 'w') as f:
            #         for m, word in enumerate(_statInfo['words']):
            #             f.write(word+"\n")

        # hyfTable.add_row(_tmpResult)
    # print(hyfTable)
    # print(hyfTable.get_csv_string())
    print('###################################')
    for key, val in illegal_words_all_unique.items():
        print(key, ":", val, '\n')


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


if __name__ == '__main__':

    """
      彩虹桥
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

    # word
    contentFiles = [
        '../words_all_unique', '../words_a', '../words_b', '../words_c', '../words_d'
    ]

    detailWordFiles = [
        # 'hyf/cuocuo2_detail/',
        # 'hyf/di_san_zhi_detail/',
        # 'hyf/dian_nao_detail/',
        # 'hyf/hua_pi_detail/',
        # 'hyf/liang_ge_haizi_detail/',
        # 'hyf/qing_feng_detail/',
        # 'hyf/ru_guo_detail/',
        # 'hyf/tiao_wu_detail/',
        # 'hyf/yue_liang_detail/'

        # 'chq/bld_detail/',
        # 'chq/byzq_detail/',
        # 'chq/gonggong_detail/',
        # 'chq/hml_detail/',
        # 'chq/jiaoliu_detail/',
        # 'chq/liwa_detail/',
        # 'chq/nvwa_detail/',
        # 'chq/qinshi_detail/',
        # 'chq/woxxin_detail/'
    ]

    printTable(sampleFiles, contentFiles, detailWordFiles)
