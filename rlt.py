#-*-coding:utf-8-*- 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import re

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('E:/project/spider/Movie.csv',encoding = 'utf8')


num = []
for i in df[u'评分人数']:
    num.append(re.findall(r'\d+',i))
plt.figure(figsize=(8,6)) 
plt.scatter(num, df[u'排名'],color = 'cornflowerblue',alpha = 0.8)
plt.xlabel(u'评分人数',fontsize=16)
plt.ylabel(u'排名',fontsize=16)
plt.gca().invert_yaxis()
plt.show()