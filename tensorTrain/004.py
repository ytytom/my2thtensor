# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import keras
from keras.datasets import cifar10

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

print(x_train.shape)
print(x_test.shape)


import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

fig = plt.figure(figsize=(20,5))
for i in range(36):
    ax = fig.add_subplot(3,12,i+1)
    ax.imshow(np.squeeze(x_train[i]))