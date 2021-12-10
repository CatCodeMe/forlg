# -*- coding:utf-8 -*-
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
            #     print("样本：", sample, "大纲：", content)
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

        # todo
        with open('./hyf/not_in_hua_pi', 'w') as f:
            f.write(_newFile)


if __name__ == '__main__':

    """
      彩虹桥
    """
    sampleFiles = [
        'hyf/hua_pi'
    ]
    # 'hml_x.txt',
    #  'jiaoliu_x.txt']
    contentFiles = ['../all_unique']
    #  '../a', '../b', '../c', '../d']

    detailWordFiles = [
        'hyf/not_in/',
    ]

    # printTable(sampleFiles, contentFiles, detailWordFiles)

    not_in_stat(sampleFiles, contentFiles)

#     print(chqTable.get_html_string())
