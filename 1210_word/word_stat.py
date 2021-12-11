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


def doStatistic(sampleFile, _wordInfo):
    totalCount = 0
    wordCount = 0
    notWordCount = 0
    _words = _wordInfo['result']
    _current_level_word_set = set()
    _illegal_word_set = set()
    with open(sampleFile, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            line = fls[i]
            lineList = line.split('/')
            for j, val in enumerate(lineList):
                if val == "":
                    continue
                for word in val:
                    if word in _words:
                        wordCount += 1
                        _current_level_word_set.add(word)
                    else:
                        notWordCount += 1
                        _illegal_word_set.add(word)
                    totalCount += 1
    return {
        "totalCount": totalCount,
        "wordCount": wordCount,
        "wordPercent": str(format(wordCount/totalCount, '.4f')),
        "notWordCount": notWordCount,
        "notWordPercent": str(format(notWordCount/totalCount, '.4f')),
        "words": _current_level_word_set,
        "illegal_words": _illegal_word_set
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
            src_count += 1
            if (_tmp == ""):
                continue
            real_count += 1
            result.append(_tmp)
    return {
        "type": type,
        "src_count": src_count,
        "real_count": real_count,
        "result": result
    }


def all(sampleFile, contentFile):
    _wordInfo = loadWords(contentFile)
    _statInfo = doStatistic(sampleFile, _wordInfo)
    return _statInfo
