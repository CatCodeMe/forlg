from LAC import LAC
import sys
import os

# 装载分词模型
en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def doSplit(_filePath, _resultDir, _resultFileName):
    # 带词性统计
    lac = LAC(mode="lac")
    # lac.load_customization('all_unique', sep=None)

    lineListWithSuffix = []
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
                    _lineStr += wordList[j] + "/"
            lineListWithSuffix.append(_lineStr)

    if not os.path.exists('1201split/'+_resultDir):
        os.makedirs('1201split/'+_resultDir)

    with open('1201split/'+resultDir+'/'+resultFileName, 'w') as f:
        for i, val in enumerate(lineListWithSuffix):
            f.write(val+'\n')


if __name__ == '__main__':
    srcFile = sys.argv[1]
    resultDir = sys.argv[2]
    resultFileName = sys.argv[3]
    # _statFilePrefix = sys.argv[3]
    # _splitInfo = doSplit(srcFile, contentFile)
    # _wordInfo = loadWords(contentFile)
    # doStatistic(_splitInfo, _wordInfo, _statFilePrefix)
    doSplit(srcFile, resultDir, resultFileName)
    print("success")
