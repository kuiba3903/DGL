import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 1. 创建自定义数值张量
print(tf.fill([1],-1))# tf.Tensor([-1], shape=(1,), dtype=int32)
print(tf.fill([2,2],99))# tf.Tensor([[99 99],[99 99]], shape=(2, 2), dtype=int32)
print("-------------------------------")

# 2. 创建已知分布的张量
tf.random.set_seed(5)
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
print("-------------------------------")

# 3. 创建序列
# 创建步长为3,0~100的序列
print(tf.range(start=0,limit=100,delta=3))
print("-------------------------------")

# 4. 拼接操作 concat
a = tf.random.normal([4,32,8])
b = tf.random.normal([6,32,8])
print(tf.concat([a,b],axis=0))# shape=(10, 32, 8)
print("-------------------------------")

# 5. 堆叠操作 stack
c = tf.random.normal([4,32,8])
print(tf.stack([a,c],axis=0))# shape=(2, 4, 32, 8)
print("-------------------------------")

# 6. 分割操作
# split (value, num_or_size_splits, axis=0, num=None, name="split")
x = tf.random.normal([10,35,8])
# 均匀分割成10份
result = tf.split(x,num_or_size_splits=10,axis=0)
print(len(result))# 10
print(result[0])# shape=(1, 35, 8)

# print(x.shape)
# 自定义长度的切割，切割为 4 份，返回 4 个张量的列表 result
result = tf.split(x, num_or_size_splits=[4,2,2,2] ,axis=0)
print(len(result))# 4
print(result[0])# shape=(4, 35, 8)

#  tf.unstack 固定切割的长度为1,维度会消失
result = tf.unstack(x,axis=0) # Unstack 为长度为 1 的张量
print(len(result)) # 返回 10个张量的列表
print(result[0]) # shape=(35, 8)
print("-------------------------------")


# 7. 向量范数

# L1范数: 所有元素绝对值的和
x = tf.ones([2,2])
print(tf.norm(x,ord=1))
# L2范数: 所有元素平方和，开根号
print(tf.norm(x,ord=2))
# 无穷范数: 所有元素绝对值的最大值
import numpy as np
print(tf.norm(x,ord=np.inf))
print("-------------------------------")

# 8. 最值、均值、和
x = tf.random.normal([4,10])
print(tf.reduce_max(x,axis=1))# 最大值
print(tf.reduce_min(x,axis=1))# 最小值
print(tf.reduce_mean(x,axis=1))# 均值
# 不指定维度,tf.reduce_*统计全局的最值、均值
print(tf.reduce_max(x))# 全局最大值
print(tf.reduce_min(x))# 全局最小值
print(tf.reduce_mean(x))# 全局均值
# 目标值索引
print(tf.argmax(x,axis=1))
print(tf.argmin(x,axis=1))
print("-------------------------------")

# 9. 数据限幅
# 可以通过 tf.maximum(x, a)实现数据的下限幅，即𝑥 ∈ [𝑎, +∞)
x = tf.range(10)
print(tf.maximum(x,3))
# 通过 tf.minimum(x, a)实现数据的上限幅，即𝑥 ∈ (−∞,𝑎]
print(tf.minimum(x,7))
# 使用tf.clip_by_value 函数实现上下限幅
print(tf.clip_by_value(x,2,7))
print("-------------------------------")

# 10. 数据收集
x = tf.random.normal([4,35,8])
print(tf.gather(x,[0,1],axis=0))# shape=(2, 35, 8)
# 乱序返回的结果也与输入的索引顺序对应
print(tf.gather(x,[0,3,6,9,12,8],axis=1))# shape=(4, 6, 8)
# tf.gather_nd 可以根据多维坐标收集数据
print(tf.gather_nd(x,[[1,1],[2,2],[3,3]]))# shape=(3, 8)
print(tf.gather_nd(x,[[1,1,2],[2,2,3],[3,3,4]]))# shape=(3,)
print("-------------------------------")

# 11. 掩码方式进行数据提取
print(tf.boolean_mask(x,mask=[False,True,True,False],axis=0))# shape=(2, 35, 8)
# 多维掩码采样
x = tf.random.uniform([2,3,8],maxval=100,dtype=tf.int32)
print(tf.gather_nd(x,[[0,0],[0,1],[1,1],[1,2]]))# 多维坐标采样 shape=(4, 8)
print(tf.boolean_mask(x,[[True,True,False],[False,True,True]]))
print("11：-------------------------------")
# 12. tf.where()
# 通过 tf.where(cond, a, b)操作可以根据 cond 条件的真假从参数𝑨或𝑩中读取数据，条件
# 判定规则如下：如果cond为True取a,False取b;
a = tf.ones([3,3])
b = tf.zeros([3,3])
cond = tf.constant([[True,True,False],[False,True,False],[False,False,True]])
print(tf.where(cond,a,b))# shape (3,3)
# 当参数 a=b=None 时，即 a 和 b 参数不指定，
# tf.where 会返回 cond 张量中所有 True 的元素的索引坐标
print(tf.where(cond))
print("12：-------------------------------")
# 13.tf.scatter_nd(indices, updates, shape)
# 对白板张量上执行刷新数据
# 通过 tf.scatter_nd(indices, updates, shape)函数可以高效地刷新张量的部分数据
indices = tf.constant([[4],[3],[1],[7]])
updates = tf.constant([4.4,3.3,1.1,7.7])
print(tf.scatter_nd(indices,updates,[8]))# 输出：tf.Tensor([0.  1.1 0.  3.3 4.4 0.  0.  7.7], shape=(8,), dtype=float32)

indices = tf.constant([[1],[3]])
updates = tf.constant([# 构造写入数据，即 2 个矩阵
 [[5,5,5,5],[6,6,6,6],[7,7,7,7],[8,8,8,8]],
 [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
])
# 在 shape 为[4,4,4]白板上根据 indices 写入 updates
"""
tf.Tensor(
[[[0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]]

 [[5 5 5 5]
  [6 6 6 6]
  [7 7 7 7]
  [8 8 8 8]]

 [[0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]
  [0 0 0 0]]

 [[1 1 1 1]
  [2 2 2 2]
  [3 3 3 3]
  [4 4 4 4]]], shape=(4, 4, 4), dtype=int32)
"""
print(tf.scatter_nd(indices,updates,[4,4,4]))