"""
 lac分词训练
"""
from lac import LAC

# 选择使用分词模型
lac = LAC(mode='seg')

# 训练和测试数据集，格式一致
train_file = "a_space"
test_file = "./data/seg_test.tsv"
lac.train(model_save_dir='./my_seg_model/',
          train_data=train_file, test_data=test_file)

# 使用自己训练好的模型
my_lac = LAC(model_path='my_seg_model')
