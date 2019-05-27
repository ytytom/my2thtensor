import pandas as pd

csv_data = pd.read_csv('alert.csv',encoding='gbk') # 读取训练数据
# print(csv_data)
print(type(csv_data))

# print(csv_data['CSL_COMPONENTTYPE'])


fenzuduixiang = csv_data.groupby('CSL_COMPONENTTYPE')

# print(type(fenzuduixiang)) #pandas groupby 对象
# print(fenzuduixiang.count()) #对groupby 对象计数
# print(fenzuduixiang.head(1)) #选取每个groupby对象的第一个实例
# print(type(fenzuduixiang.CSL_COMPONENTTYPE))
# print(type(fenzuduixiang.CSL_COMPONENTTYPE))
print(fenzuduixiang.count())


# 只是拿到了数，分了组，怎么拿到分组后的数，和分后的具体某个列的数

# WLSB_ALERT = csv_data(['CSL_COMPONENTTYPE','NODE']).groupby(csv_data['NODE'])
# print(WLSB_ALERT.count())





