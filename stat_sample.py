from LAC import LAC
import sys

en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def doSplit(_filename, _statFilePrefix):
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

    with open(_statFilePrefix+"_normal_" + str(len(legalResult)), 'w') as f:
        f.write("正常词总计(未去重): " + str(len(legalResult)) + "\n")
        f.write("================================\n")
        for i, val in enumerate(legalResult):
            f.write(val+'\n')

    with open(_statFilePrefix+"_except_" + str(len(illegalResult)), 'w') as f:
        f.write("异常词(标点符号、数字、大写字母)总计(未去重): " + str(len(illegalResult)) + "\n")
        f.write("================================\n")
        for i, val in enumerate(illegalResult):
            f.write(val+'\n')


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


"""
  统计样本文件的分词情况, 分别输出异常词, 和正常词性的词
  1: 文件路径
  2: 结果文件的名字 
"""

if __name__ == '__main__':
    sampleFile = sys.argv[1]
    _statFilePrefix = sys.argv[2]
    doSplit(sampleFile, _statFilePrefix)
    print("success")
