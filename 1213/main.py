# -*- coding:utf-8 -*-
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
import word_stat as word_stat


def printTable(_sampleFiles):
    hyfTable = PrettyTable(field_names=["样本文件", "总字数", "句子数", "平均句长"])

    hyfTable.align = 'l'

    illegal_words_all_unique = {}

    for i, sample in enumerate(_sampleFiles):
        hasAdd = False
        _tmpResult = []

        result = word_stat.doStatistic(sample)
        _tmpResult.append(sample)
        _tmpResult.append(result['totalCount'])
        _tmpResult.append(result['endSignCount'])
        _tmpResult.append(result['avgLength'])
        hyfTable.add_row(_tmpResult)
    print(hyfTable)
    print(hyfTable.get_csv_string())


if __name__ == '__main__':

    sampleFiles = [
        '../docs/hyf/cuocuo_2.txt',
        '../docs/hyf/di_san_zhi.txt',
        '../docs/hyf/dian_nao.txt',
        '../docs/hyf/hua_pi.txt',
        '../docs/hyf/liang_ge_haizi.txt',
        '../docs/hyf/qing_feng.txt',
        '../docs/hyf/ru_guo.txt',
        '../docs/hyf/tiao_wu.txt',
        '../docs/hyf/yue_liang.txt',

        '../docs/chq/bao_lian_deng.txt',
        '../docs/chq/bo_ya_shuai_qin_xie_zhi_yin.txt',
        '../docs/chq/gonggong_x.txt',
        '../docs/chq/hml_x.txt',
        '../docs/chq/jiaoliu_x.txt',
        '../docs/chq/liwa_x.txt',
        '../docs/chq/nvwa_x.txt',
        '../docs/chq/qinshi_x.txt',
        '../docs/chq/woxxin_x.txt'
    ]

    printTable(sampleFiles)
