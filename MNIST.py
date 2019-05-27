# coding:utf-8
import tensorflow as tf
import os
import csv
import collections
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def readData():
    filename = "alert.csv"
    file_queue = tf.train.string_input_producer([filename])
    reader = tf.TextLineReader(skip_header_lines=1)
    key , value =  reader.read(file_queue)

    defaults = [[0.], [0.], [0.], [0.], [0.], [0.], [0.]]
    ACTIONTIME, ACTIONCODE, NODE, NODEALIAS, SEVERITY, SUMMARY, CSL_COMPONENTTYPE = tf.decode_csv(value,defaults)
    vertor_example = tf.stack([ACTIONTIME, ACTIONCODE, NODE, NODEALIAS, SEVERITY, SUMMARY, CSL_COMPONENTTYPE])
    vertor_label = tf.stack([SUMMARY])
    example_batch, label_batch = tf.train.shuffle_batch([vertor_example, vertor_label], batch_size=10,capacity=100, min_after_dequeue=10)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(coord=coord)
        print (sess.run(tf.shape(example_batch)))
        print (sess.run(tf.shape(label_batch)))
        print (sess.run(example_batch[5]))
        coord.request_stop()
        coord.join(threads)

    # print (key,value)
    pass

readData()
print ('hello')