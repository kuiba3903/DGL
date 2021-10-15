import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 1. 创建自定义数值张量
print(tf.fill([1],-1))
print(tf.fill([2,2],99))


# 2. 创建已知分布的张量
print(tf.random.normal([2,2])) # 创建标准正态分布的张量
# 创建均值为1,方差为2的正态分布
print(tf.random.normal([2,2],mean=1,stddev=2))

#通过 tf.random.uniform(shape, minval=0, maxval=None, dtype=tf.float32)
# 可以创建采样自 [minval, maxval)区间的均匀分布的张量
print(tf.random.uniform([2,2],minval=5,maxval=10))

# 创建采样自[0,1)均匀分布的矩阵
print(tf.random.uniform([2,2]))
# 创建采样自[0,100)均匀分布的整型矩阵
print(tf.random.uniform([2,2],maxval=100,dtype=tf.int32))

# 3. 创建序列
# 创建步长为3,0~100的序列
print(tf.range(start=0,limit=100,delta=3))