import tensorflow as tf
# 创建自定义数值张量
print(tf.fill([1],-1))
print(tf.fill([2,2],99))
# 创建已知分布的张量
print(tf.random.normal([2,2])) # 创建标准正态分布的张量