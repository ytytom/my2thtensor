# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

intermed = tf.add(input2,input3)
#2+5


mul = tf.multiply(input1,intermed)
#3*7


with tf.Session() as sess:
    result = sess.run([mul,intermed])
    #获取多个tensor的值
    print(result)