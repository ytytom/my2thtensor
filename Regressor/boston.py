# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['KERAS_BACKEND']='tensorflow'
import tensorflow as tf

from keras.datasets import boston_housing
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

print(x_train.shape)
print(y_train.shape)
print(type(x_train))

for i in x_train:
    plt.plot(i)

plt.show()
