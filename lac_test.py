from LAC import LAC

# 装载分词模型
lac = LAC(mode='lac')

# 单个样本输入，输入为Unicode编码的字符串
text = u"你们也会给我们方便,我很高兴"
seg_result = lac.run(text)

print("是否是数字:", text.isdigit())

print(seg_result)

# 批量样本输入, 输入为多个句子组成的list，平均速率会更快
texts = [u"LAC是个优秀的分词工具", u"百度是一家高科技公司"]
seg_result = lac.run(texts)
