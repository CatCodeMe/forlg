"""
 echo手动处理超纲词, 再统计这里边可能包含的大纲词
"""
import sys


def load(_filename):
    result = []
    with open(_filename, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            _tmp = fls[i].rstrip('\n')
            result.append(_tmp)
    return {"result": result}


if __name__ == '__main__':
    notin = sys.argv[1]
    content = sys.argv[2]

    notinResult = load(notin)["result"]
    contentResult = load(content)["result"]

    count = 0
    for i, val in enumerate(notinResult):
        if str(val) in contentResult:
            print(str(val))
            count += 1
    print(count)
    print("success")
