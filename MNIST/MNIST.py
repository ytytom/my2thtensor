from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print(mnist.train.images.shape,mnist.train.lables.shape)
print(mnist.test.images.shape,mnist.test.lables.shape)
print(mnist.validation.images.shape,mnist.validation.lables.shape)