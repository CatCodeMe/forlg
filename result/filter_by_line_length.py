
count = 0
map = {}
with open('./chq/bao_lian_deng/bld-all_in_sample_notin_content', 'r') as f:
    fls = f.readlines()
    for i in range(0, len(fls)):
        word = fls[i].rstrip('\n')
        if len(fls[i].rstrip('\n')) >= 3:
            count += 1
            map[word] = ""
print(count)
print(len(map))
