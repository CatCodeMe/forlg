from LAC import LAC
import sys

# lac = LAC(mode='seg')

# with open('qf.txt', 'r') as f:
#     fls = f.readlines()
#     for i in range(0, len(fls)):
#         print(lac.run(fls[i].rstrip('\n')))
#         print("#################################\n")

# 装载分词模型
en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def doSplit(_filename):
    # 带词性统计
    lac = LAC(mode='lac')

    legalResult = []
    illegalResult = []
    legalCount = 0
    with open(_filename, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            _tmp = lac.run(fls[i].rstrip('\n'))
            _tmpFilter = doFilterByLine(_tmp)
            legalResult.extend(_tmpFilter['legal'])
            illegalResult.extend(_tmpFilter['exception'])
            legalCount += len(_tmpFilter['legal'])
    return {
        "file_name": _filename,
        "src_split_count": len(legalResult) + len(illegalResult),
        "legal_count": len(legalResult),
        "illegal_count": len(illegalResult),
        "result": legalResult
    }


def doFilterByLine(_lacResult):
    result = []
    splits = _lacResult[0]
    types = _lacResult[1]
    except_word = []
    for i, val in enumerate(types):
        if val == 'w' or val.isdigit() or val in en:
            except_word.append(splits[i])
            continue
        result.append(splits[i])
    return {"legal": result, "exception": except_word}


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
    return {
        "type": type,
        "src_count": src_count,
        "real_count": real_count,
        "result": result
    }


"""
splits: 语料分词后的list

type_contents: 甲乙丙丁四种词汇

statFile: 统计明细
"""


def doStatistic(_splitInfo, _wordInfo, _statFilePrefix):
    map = {}
   #  print(_splitInfo)
   #  print(_wordInfo)
    for i, sVal in enumerate(_splitInfo['result']):
        for j, cVal in enumerate(_wordInfo['result']):
            # if sVal == '有的' and cVal == '有的':
            #     print("有的")
            if sVal == cVal:
                map[sVal] = map.get(cVal, 0) + 1
    with open(_statFilePrefix+"_detail", 'w') as f:
        for key in map:
            f.write(key + "," + str(map[key]) + '\n')

    with open(_statFilePrefix+"_total", 'w') as f:
        f.write("样本文件：" + _splitInfo['file_name'] +
                " ,原始切词数量：" + str(_splitInfo['src_split_count']) + '\n')
        f.write("大纲文件：" + _wordInfo['type'] + ",规定数量：" + str(
            _wordInfo['src_count']) + ",实际数量(百度文库、去重)：" + str(_wordInfo['real_count']) + '\n')
        f.write("样本中包含大纲词汇: " + str(len(map)) + '\n')
        totalCount = 0
        for key in map:
            totalCount += map[key]
        f.write("在文章中总共出现的次数: " + str(totalCount))


if __name__ == '__main__':
    srcFile = sys.argv[1]
    contentFile = sys.argv[2]
    _statFilePrefix = sys.argv[3]
    _splitInfo = doSplit(srcFile)
    _wordInfo = loadWords(contentFile)
    doStatistic(_splitInfo, _wordInfo, _statFilePrefix)
    print("success")
