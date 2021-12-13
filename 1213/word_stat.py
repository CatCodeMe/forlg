# -*- coding:utf-8 -*-
"""
统计平均句长

- 。！ ? ...... 4种符合作为断句的标点符号
- 总字数不包含标点
"""
from LAC import LAC


def doStatistic(sampleFile):
    # 统计词性
    lac = LAC(mode="lac")
    totalCount = 0
    endSignCount = 0
    with open(sampleFile, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            line = fls[i].rstrip('\n')
            for singleChar in line:
                if singleChar.strip() != '':
                    _tmp = lac.run(singleChar.strip())
                    # print(_tmp)
                    word = _tmp[0][0]
                    type = _tmp[1][0]
                    if type == 'w':
                        if word == '?' or word == '!' or word == '。' or word == '......':
                            endSignCount += 1
                    else:
                        totalCount += 1
    return {
        "totalCount": totalCount,
        "endSignCount": endSignCount,
        "avgLength": str(format(totalCount/endSignCount, '.4f'))
    }
