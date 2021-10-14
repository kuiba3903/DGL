import numpy as np
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.test.is_gpu_available())
print(tf.config.list_physical_devices("GPU"))
a = tf.constant(123456789,dtype=tf.int32)
print(a)
import tensorflow as tf
a = tf.test.is_built_with_cuda()  # 判断CUDA是否可以用
b = tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None) # 判断GPU是否可以用
print(a)
print(b)

from sortedcontainers import SortedList
s = SortedList([1,2,3])
# 添加元素
s.add(3)
s.add(7)
s.add(23)
print(s)
