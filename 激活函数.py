import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
x = tf.random.normal([2,2])
print(x)
# sigmoid 函数
s_x = tf.nn.sigmoid(x)
print(s_x)
# relu 函数
r_x = tf.nn.relu(x)
print(r_x)
# leaky_relu 函数
l_r_x = tf.nn.leaky_relu(x,alpha=0.01)
print(l_r_x)
# tanh激活函数
t_x = tf.nn.tanh(x)
print(t_x)
# softmax 函数
sf_x = tf.nn.softmax(x)
print(sf_x)