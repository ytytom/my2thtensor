#! coding:utf-8
import os

stop_words = []
with open('stop_words.txt',encoding='gbk') as f:
    line = f.readline()
    while line:
        stop_words.append(line[:-1])
        line = f.readline()
    stop_words = set(stop_words)
    print('停用词读取完毕，共{n}个单词'.format(n=len(stop_words)))