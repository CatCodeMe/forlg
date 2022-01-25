import sys


level = ['一级', '二级', '三级', '四级', '五级', '六级']


def etl(_filepath):
    result = []
    with open(_filepath, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            ll = fls[i].split()
            for val in iter(ll):
                _tmp = val.strip()
                if _tmp != '':
                    result.append(_tmp)
    print(len(result))
    with open('words', 'w') as f:
        for val in iter(result):
            f.write(val+"\n")


if __name__ == '__main__':
    srcFile = sys.argv[1]
    etl(srcFile)
