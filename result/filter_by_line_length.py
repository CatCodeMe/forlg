
import sys


def stat(_filename):
    count = 0
    lenmap = {}
    wordmap = {}
    with open(_filename, 'r') as f:
        fls = f.readlines()
        for i in range(0, len(fls)):
            word = fls[i].rstrip('\n')
            lenline = len(fls[i].rstrip('\n'))
            count += 1
            # map[sVal] = map.get(cVal, 0) + 1
            lenmap[lenline] = lenmap.get(lenline, 0) + 1
            if lenline >= 3:
                wordmap[word] = ""
    print("total count: ", count)
    print("different length word: ", lenmap)
    print("length >=3 :", len(wordmap))


if __name__ == '__main__':
    srcFile = sys.argv[1]
    stat(srcFile)
    print("success")
