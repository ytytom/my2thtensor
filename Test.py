# coding:utf-8
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print(tf.__version__)


sess = tf.InteractiveSession()

x = tf.Variable([1.0,2.0])
a = tf.constant([3.0,4.0])


x.initializer.run()


sub = tf.subtract(x,a)

print(sub.eval())