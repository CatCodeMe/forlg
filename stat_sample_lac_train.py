from LAC import LAC
import sys

en = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def doSplit(_filename, _modelfile, _statFilePrefix):
    # 带词性统计
    lac = LAC(mode='lac')
    lac.load_customization(_modelfile, sep=None)

    # 切词
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

    # 大纲词
    contentWords = []
    with open(_modelfile, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            _tmp = fls[i].rstrip('\n')
            if _tmp in en:
                continue
            contentWords.append(_tmp)

    # 切词工具的切词结果
    with open(_statFilePrefix+"_normal_" + str(len(legalResult)), 'w') as f:
        f.write("正常词总计(未去重): " + str(len(legalResult)) + "\n")
        f.write("================================\n")
        for i, val in enumerate(legalResult):
            f.write(val+'\n')

    legal_notin_content_count = 0
    # 切词结果 & 不在大纲词里
    with open(_statFilePrefix+"_in_sample_notin_content", 'w') as f:
        f.write("=============正常切词结果 && 不在大纲词里===================\n")
        for i, val in enumerate(legalResult):
            if val not in contentWords:
                f.write(val+'\n')
                legal_notin_content_count += 1

    legal_in_content_count = 0
    # 切词结果 & 在大纲词里
    with open(_statFilePrefix+"_in_sample_in_content", 'w') as f:
        f.write("=============正常切词结果 && 在大纲词里===================\n")
        for i, val in enumerate(legalResult):
            if val in contentWords:
                f.write(val+'\n')
                legal_in_content_count += 1

    # 非法切词结果
    with open(_statFilePrefix+"_except_" + str(len(illegalResult)), 'w') as f:
        f.write("异常词(标点符号、数字、大写字母)总计(未去重): " + str(len(illegalResult)) + "\n")
        f.write("================================\n")
        for i, val in enumerate(illegalResult):
            f.write(val+'\n')

    # 数量统计
    with open(_statFilePrefix + "_total", 'w') as f:
        f.write("===============总计(未去重)=================\n")
        f.write("样本文件合法词数量: " + str(legalCount) + '\n')
        f.write("样本文件合法词, 但是不是大纲词: " + str(legal_notin_content_count) + '\n')
        f.write("样本文件合法词, 又是大纲词: " + str(legal_in_content_count)
                + " --> (" + str(legal_in_content_count) + "/"
                + str(legalCount) + ")="
                + str(format(legal_in_content_count / legalCount, '.4f')) + '\n')
        f.write("样本文件非法词(标点、字母、人名、地名): " + str(len(illegalResult)) + '\n')

    print({"legalResult": legalCount,
           "legal_notin_content": legal_notin_content_count,
           "legal_in_content": legal_in_content_count,
           "illegal": len(illegalResult)})


def doFilterByLine(_lacResult):
    result = []
    splits = _lacResult[0]
    types = _lacResult[1]
    except_word = []
    for i, val in enumerate(types):
        if val == 'w' or val == 'PER' or val == 'LOC' or val.isdigit() or val in en:
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
    contentFile = sys.argv[2]
    _statFilePrefix = sys.argv[3]
    doSplit(sampleFile, contentFile, _statFilePrefix)
    print("success")
