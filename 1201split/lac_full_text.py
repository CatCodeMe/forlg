from LAC import LAC
import sys
import os

# 装载分词模型
en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def doSplit(_filePath, _resultDir, _resultFileName, _wordInfo):
    # 带词性统计
    lac = LAC(mode="lac")
    # lac.load_customization('all_unique', sep=None)

    lineListWithSuffix = []

    _contentWordList = _wordInfo['result']
    with open(_filePath, 'r') as f:
        fls = f.readlines()
        # result = lac.run(fls)
        # print(result)
        # for i, lineList in enumerate(result):
        for i in range(0, len(fls)):
            _tmp = lac.run(fls[i].rstrip('\n'))
            wordList = _tmp[0]
            typeList = _tmp[1]
            _lineStr = ""
            for j, type in enumerate(typeList):
                if type == 'w' or type.isdigit() or type in en:
                    _lineStr += wordList[j]
                else:
                    if wordList[j] in _contentWordList:
                        _lineStr += wordList[j] + "/"
                    else:
                        _lineStr += "【" + wordList[j] + "】"

            lineListWithSuffix.append(_lineStr)

    if not os.path.exists('1201split/'+_resultDir):
        os.makedirs('1201split/'+_resultDir)

    with open('1201split/'+resultDir+'/' + _resultFileName, 'w') as f:
        for i, val in enumerate(lineListWithSuffix):
            f.write(val+'\n')


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
        "d": "丁级词"
    }

    return {
        "type": type,
        "src_count": src_count,
        "real_count": real_count,
        "result": result
        # "zh_name": name[_filename]
    }


if __name__ == '__main__':
    srcFile = sys.argv[1]
    resultDir = sys.argv[2]
    resultFileName = sys.argv[3]
    contentFile = sys.argv[4]

    # _statFilePrefix = sys.argv[3]
    # _splitInfo = doSplit(srcFile, contentFile)
    # _wordInfo = loadWords(contentFile)
    # doStatistic(_splitInfo, _wordInfo, _statFilePrefix)
    _wordInfo = loadWords(contentFile)
    # print(_wordInfo)
    doSplit(srcFile, resultDir, resultFileName, _wordInfo)
    print("success")
