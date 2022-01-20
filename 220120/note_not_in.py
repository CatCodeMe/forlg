# -*- coding:utf-8 -*-
"""
 
 统计lg处理好的文件, 并和大纲词对比
 统计结果

 1. 总词数
 2. 大纲词数
   - 总占比
   - 分类别占比
 3. 超纲次数


"""
import sys
from LAC import LAC


def doStatistic(sampleFile, _wordInfo):

    # 带词性统计
    lac = LAC(mode="lac")

    totalCount = 0
    wordCount = 0
    notWordCount = 0
    _words = _wordInfo['result']
    _filterResult = []
    _current_level_word_set = set()

    legal_all_words = []
    with open(sampleFile, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            line = fls[i]
            lineList = line.split('/')
            for j, val in enumerate(lineList):
                if val == "":
                    continue
                _tmp = lac.run(val)
                wordList = _tmp[0]
                typeList = _tmp[1]
                for x, type in enumerate(typeList):
                    if type == 'w' or type.isdigit():
                        continue
                    realVal = wordList[x]
                    if realVal in _words:
                        _current_level_word_set.add(realVal)
                        wordCount += 1
                    else:
                        notWordCount += 1
                    totalCount += 1
                    legal_all_words.append(realVal+'/')
    return {
        "totalCount": totalCount,
        "wordCount": wordCount,
        "wordPercent": str(format(wordCount/totalCount, '.4f')),
        "notWordCount": notWordCount,
        "notWordPercent": str(format(notWordCount/totalCount, '.4f')),
        "words": _current_level_word_set,
        "legal_all_words": legal_all_words
    }


en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def loadWords(_filename):
    type = ""
    src_count = 0
    real_count = 0
    result = []
    with open(_filename, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            _tmp = fls[i].rstrip('\n')
            if (i == 0):
                type += _tmp
                continue
            if (i == 1):
                src_count = _tmp
                continue
            if _tmp in en:
                continue
            real_count += 1
            result.append(_tmp)
    name = {
        "a": "甲级词",
        "b": "乙级词",
        "c": "丙级词",
        "d": "丁级词",
        "all_unique": "全部大纲词"
    }

    return {
        "type": type,
        "src_count": src_count,
        "real_count": real_count,
        "result": result
    }


def all(sampleFile, contentFile):
    _wordInfo = loadWords(contentFile)
    _statInfo = doStatistic(sampleFile, _wordInfo)
#     print(_statInfo)
    return _statInfo
