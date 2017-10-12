#-*-coding:utf-8-*- 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('E:/project/spider/Movie.csv',encoding = 'utf8')
genre_split = df[u'类别'].str.split(' ').apply(pd.Series)
a = genre_split.apply(pd.value_counts).fillna('0') 

a.columns = ['type_1','type_2','type_3','type_4','type_5','type_6']
#a
a['type_1'] = a['type_1'].astype(int)
a['type_2'] = a['type_2'].astype(int)
a['type_3'] = a['type_3'].astype(int)
a['type_4'] = a['type_4'].astype(int)
a['type_5'] = a['type_5'].astype(int)
a['type_6'] = a['type_6'].astype(int)
a
a = a.apply(lambda x: x.sum(),axis = 1)#axis = 1,将一个矩阵的每一行向量相加.axis = 0,列相加
genre_split = pd.DataFrame(a, columns = [u'数量'])

genre_split.sort_values(by = u'数量',ascending = True).plot(kind ='barh', color = 'cornflowerblue',figsize = (10,6))

plt.legend(loc='lower right')
plt.title(u'电影类型分布情况',fontsize=16)
plt.xlabel(u'电影数量',fontsize=16)
plt.ylabel(u'类型',fontsize=16)
plt.show()