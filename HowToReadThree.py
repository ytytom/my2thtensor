# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

file_queue = tf.train.string_input_producer(['alert.csv'])

reader = tf.TextLineReader(skip_header_lines=1)
key ,value = reader.read(file_queue)

ACTIONTIME,ACTIONCODE,NODE,NODEALIAS,SEVERITY,SUMMARY,CSL_COMPONENTTYPE = tf.decode_csv(value,record_defaults=[['null'],['null'],['null'],['null'],[1.0],['null'],['null']])


get_data, get_label = tf.train.shuffle_batch(
         [[ACTIONTIME,ACTIONCODE,NODE,NODEALIAS,SEVERITY,SUMMARY],CSL_COMPONENTTYPE ],batch_size = 10,capacity=150, min_after_dequeue=10)


with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess, coord)
    try:
        data_value, label_value = sess.run([get_data, get_label])
    except tf.errors.OutOfRangeError:
        print("Done")
    finally:
        coord.request_stop()
    coord.join(threads)
