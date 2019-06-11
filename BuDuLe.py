# coding:utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import collections
import numpy as np
import random



def load_w2c_textcn_dataset(path='./'):
    print("Load or Download chinese text corpus Dataset> {}".format(path))

    filename = 'alert.csv'
    word_list_all=[]
    with open(os.path.join(path, filename)) as f:
        for line in f:
            word_list=line.strip().split()
            for idx, word in enumerate(word_list):
                word_list[idx] = word_list[idx].encode('utf-8')
                #print word_list[idx]
                word_list_all.append(word_list[idx])
    return word_list_all

words=load_w2c_textcn_dataset(path='./')
print (len(words))



vocabulary_size = 200000
count = [['UNK', -1]]
count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
dictionary = dict()

for word, _ in count:
    dictionary[word] = len(dictionary)
data = list()
unk_count = 0
for word in words:
    if word in dictionary:
        index = dictionary[word]
    else:
        index = 0  # dictionary['UNK']
        unk_count = unk_count + 1
    data.append(index)

count[0][1] = unk_count
reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
del(words)


data_index = 0

def generate_batch(batch_size, num_skips, skip_window):
    global data_index
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1  # [ skip_window target skip_window ]
    buf = collections.deque(maxlen=span)
    for _ in range(span):
        buf.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    for i in range(batch_size // num_skips):
        target = skip_window  # target label at the center of the buffer
        targets_to_avoid = [ skip_window ]
        for j in range(num_skips):
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buf[skip_window]
            labels[i * num_skips + j, 0] = buf[target]
        buf.append(data[data_index])
        data_index = (data_index + 1) % len(data)

    print(batch,labels)
    return batch, labels

num_steps = 500001
generate_batch(10,150,10)
# with tf.Session() as session:
#     tf.global_variables_initializer().run()
#     average_loss = 0
#     for step in range(num_steps):
#         batch_data, batch_labels = generate_batch(batch_size, num_skips, skip_window)
#         feed_dict = {train_dataset : batch_data, train_labels : batch_labels}
#         _, l = session.run([optimizer, loss], feed_dict=feed_dict)
#         average_loss += l
#         if step % 100000 == 0 and step > 0:
#             print('Average loss at step %d: %f' % (step, average_loss / 100000))
#             average_loss = 0
#     word2vec = normalized_embeddings.eval()