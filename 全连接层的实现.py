import tensorflow as tf
import os
from tensorflow.keras import layers
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 1. 张量方式实现
x = tf.random.normal([4,28*28])
w1 = tf.Variable(tf.random.truncated_normal([784,512],stddev=0.1))
b1 = tf.Variable(tf.zeros([512]))
o1 = tf.matmul(x,w1)+b1 # 线性变换
o1 = tf.nn.relu(o1)# 激活函数
print(o1)# shape=(4, 512)

# 2. 层方式实现
fc = layers.Dense(512,activation=tf.nn.relu)
h1 = fc(x)
print(h1)
print(fc.kernel)
print(fc.bias)
print(fc.trainable_variables)