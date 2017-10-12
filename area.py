#-*-coding:utf-8-*- 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('E:/project/spider/Movie.csv',encoding = 'utf8')
area_split = df[u'地区'].str.split(' ').apply(pd.Series)
a = area_split.apply(pd.value_counts).fillna('0') 
a.columns = ['area_1','area_2','area_3','area_4','area_5']
#a
a['area_1'] = a['area_1'].astype(int)
a['area_2'] = a['area_2'].astype(int)
a['area_3'] = a['area_3'].astype(int)
a['area_4'] = a['area_4'].astype(int)
a['area_5'] = a['area_5'].astype(int)
a = a.apply(lambda x: x.sum(),axis = 1)#axis = 1,将一个矩阵的每一行向量相加.axis = 0,列相加
area_c = pd.DataFrame(a, columns = [u'数量'])


area_c.sort_values(by = u'数量',ascending = True).plot(kind ='barh', color = 'cornflowerblue',figsize = (10,6))

plt.legend(loc='lower right')
plt.title(u'电影国家/地区分布情况',fontsize=16)
plt.xlabel(u'电影数量',fontsize=16)
plt.ylabel(u'国家/地区',fontsize=16)
plt.show()