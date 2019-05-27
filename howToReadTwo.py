import numpy as np

# ACTIONTIME,ACTIONCODE,NODE,NODEALIAS,SEVERITY,SUMMARY,CSL_COMPONENTTYPE = np.loadtxt('alert.csv', delimiter=',', unpack=True)
# a = np.loadtxt('alert.csv',dtype=str, delimiter=',', unpack=True,skiprows=1)
a = np.loadtxt('alert.csv',dtype=str)
print(a)
