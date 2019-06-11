#!coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def howToread(filename):
    dataMat = []
    with open(filename) as f:
        for line in f:
            trainingData = line.strip('\n').split(',')
            print(trainingData)

            # ReallyData = trainingData[2:4]
            # print(trainingData[2])

            plt.scatter(trainingData[2],trainingData[3],marker=2)
            # print(trainingData[1:2])
            # ReallyData = map(float, ReallyData)
            # print('ReallyData is %',ReallyData)

            # dataMat.append(ReallyData)
            # plt.show()

    plt.show()
    return dataMat


test = howToread('./iris.data')
print(test)



def distEclud(vecA,vecB):
    return np.sqrt(sum(pow(vecA-vecB,2)))


def randCenter(dataSet,k):
    n = np.shape(dataSet)[1]
    centrodis = np.mat(np.zeros(k,n))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(np.array(dataSet)[:,j]) - minJ)
        centrodis[:, j] = minJ + rangeJ * np.random.rand(k, 1)
    return centrodis


