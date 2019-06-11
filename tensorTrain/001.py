# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf



matrix1 = tf.constant([[3., 3.]])
#只是一个OP节点，一个Tensor的对象，并不是一个2*1矩阵
#constant 也是常量的意思


print(matrix1)
print(type(matrix1))

#一个 tensor 包含一个静态类型 rank, 和 一个 shape
print(matrix1.shape)
print(matrix1._rank())

matrix2 = tf.constant([[2.],[2.]])
#op节点,也是一个tensor

product = tf.matmul(matrix1, matrix2)
#op节点，也是一个tensor
#MATMUL 是tensorflow里定义的矩阵相乘的运算





print(product)

#构造阶段，我们定义了两个矩阵，和一个矩阵相乘的运算




#启动图


sess = tf.Session()

#默认图的启动方法

result = sess.run(product)
#调用图的sess.run方法来op运算。传入的参数是product 这个是矩阵相乘的输出，是你想拿到的值

print(result)
print(type(result))

#返回值 'result' 是一个 numpy `ndarray` 对象.

sess.close()
