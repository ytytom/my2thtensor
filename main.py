# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf


print(tf.__version__)


matrix1 = tf.constant([[3., 3.]])

matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1, matrix2)


sess = tf.Session()


result = sess.run(product)

print (result)

sess.close()