import tensorflow as tf
from tensorflow.keras import layers,Sequential
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
x = tf.random.normal([4,28*28])
# 张量方式的实现
# 隐藏层1张量
w1 = tf.Variable(tf.random.truncated_normal([784,256],stddev=0.1))
b1 = tf.Variable(tf.zeros([256]))
# 隐藏层2张量
w2 = tf.Variable(tf.random.truncated_normal([256,128],stddev=0.1))
b2 = tf.Variable(tf.zeros([128]))
# 隐藏层3张量
w3 = tf.Variable(tf.random.truncated_normal([128,64],stddev=0.1))
b3 = tf.Variable(tf.zeros([64]))
# 隐藏层4张量
w4 = tf.Variable(tf.random.truncated_normal([64,10],stddev=0.1))
b4 = tf.Variable(tf.zeros([10]))
with tf.GradientTape() as tape:# 梯度记录器
    # 隐藏层1 前向计算
    # 也可以写成： h1 = x@w1+tf.broadcast_to(b1,[x.shape[0],256])
    h1 = x@w1+b1# 自动广播
    h1 = tf.nn.relu(h1)
    # 隐藏层2 前向计算
    h2 = h1@w2+b2
    h2 = tf.nn.relu(h2)
    # 隐藏层3 前向计算
    h3 = h2 @ w3 + b3
    h3 = tf.nn.relu(h3)
    # 隐藏层4 前向计算
    h4 = h3 @ w4 + b4
    # h4 = tf.nn.relu(h4) 最后一层是否加激活函数视情况而定
print(h4)

# 层方式实现
# 通过 Sequential 容器封装为一个网络类
model = Sequential([
    layers.Dense(256,activation= tf.nn.relu),
    layers.Dense(128,activation= tf.nn.relu),
    layers.Dense(64,activation= tf.nn.relu),
    layers.Dense(10,activation=None)]
)
output = model(x)
print(output)
