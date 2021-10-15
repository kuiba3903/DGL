import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 创建自定义数值张量
print(tf.fill([1],-1))
print(tf.fill([2,2],99))
# 创建已知分布的张量
print(tf.random.normal([2,2])) # 创建标准正态分布的张量