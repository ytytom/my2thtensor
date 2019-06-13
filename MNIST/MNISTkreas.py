#!coding:utf-8
import numpy as np
np.random.seed(1337)
import keras
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D,MaxPooling2D,Flatten
from keras.optimizers import Adam


(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 1,28, 28)/255.
x_test = x_test.reshape(-1, 1,28, 28)/255.
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

print(np.shape(x_train))
print(np.shape(x_test))

model = Sequential()

model.add(Convolution2D(
    filters=32,
    kernel_size=5,
    strides=1,
    padding='same'

))

model.add(Activation('relu'))

model.add(MaxPooling2D(
    pool_size=2,
    strides=2,
    padding='same',    # Padding method
    data_format='channels_first',
))


model.add(Convolution2D(64, 5, strides=1, padding='same', data_format='channels_first'))
model.add(Activation('relu'))


model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))

model.add(Dense(10))
model.add(Activation('softmax'))

adam = Adam(lr=1e-4)


model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training ------------')
# Another way to train the model
model.fit(x_train, y_train, epochs=5, batch_size=64,)

print('\nTesting ------------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(x_test, y_test)

print('\ntest loss: ', loss)
print('\ntest accuracy: ', accuracy)
